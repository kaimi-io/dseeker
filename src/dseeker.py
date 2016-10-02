import argparse
import logging
import coloredlogs
import ssl

import concurrent.futures
import urllib.request

from netaddr import IPNetwork
from collections import deque


VERSION = 0.1


def main():
	args = setup_args()
	coloredlogs.install()

	logging.info("Starting...")
	try:
		check_loop(args)
	except Exception as exception:
		logging.error(exception)
	logging.info("Finished")


def check_loop(args):
	with concurrent.futures.ThreadPoolExecutor(max_workers = args.threads) as pool:
		domains = args.domains.split(args.separator)
		ips = args.ips.split(args.separator)
		codes = args.codes.split(args.separator)

		tasks = deque([])
		for entry in ips:
			ip_list = IPNetwork(entry)
			for ip in ip_list:
				for domain in domains:
					tasks.append(
						pool.submit(
							check_ip, domain, ip, args, codes
						)
					)
		

		for task in concurrent.futures.as_completed(tasks):
			try:
				result = task.result()
			except Exception as exception:
				logging.error(exception)
			else:
				if result != None:
					data = str(result[0])
					if(
						( args.exclude == None and args.include == None )
						or
						( args.exclude and args.exclude not in data )
						or
						( args.include and args.include in data )
					):
						logging.critical("[+] " + args.separator.join(result[1:]))


def check_ip(domain, ip, args, codes):
	ip = str(ip)
	check_https = False

	logging.info("Checking " + args.separator.join([ip, domain]))

	while True:
		schema = 'https://' if check_https else 'http://';
		port = str(args.https_port) if check_https else str(args.http_port)

		request = urllib.request.Request(
			schema + ip + ':' + port + '/', 
			data = None,
			headers = {
				'User-Agent': args.agent,
				'Host': domain
			}
		)

		try:
			response = urllib.request.urlopen(
				request,
				data = None,
				timeout = args.timeout,
				context = ssl._create_unverified_context()
			)
			data = response.read()
			return [data, ip, domain]
		except urllib.error.HTTPError as exception:
			if str(exception.code) in codes:
				data = exception.fp.read()
				return [data, ip, domain]
		except Exception:
			pass

		if args.https and not check_https:
			check_https = True
			continue

		return None


def setup_args():
	parser = argparse.ArgumentParser(
		description = 'Domain Seeker v' + str(VERSION) + ' (c) Kaimi (kaimi.io)',
		epilog = '',
		formatter_class = argparse.ArgumentDefaultsHelpFormatter
	)
	parser.add_argument(
		'-d',
		'--domains',
		help = 'Domain list to discover',
		type = str,
		required = True
	)
	parser.add_argument(
		'-i',
		'--ips',
		help = 'IP list (ranges) to scan for domains',
		type = str,
		required = True
	)
	parser.add_argument(
		'--https',
		help = 'Check HTTPS in addition to HTTP',
		action = 'store_true'
	)
	parser.add_argument(
		'--codes',
		help = 'HTTP-codes list that will be considered as good',
		type = str,
		default = '200,301,302,401,403'
	)
	parser.add_argument(
		'--separator',
		help = 'IP/Domain/HTTP-codes list separator',
		type = str,
		default = ','
	)
	parser.add_argument(
		'--include',
		help = 'Show results containing provided string',
		type = str
	)
	parser.add_argument(
		'--exclude',
		help = 'Hide results containing provided string',
		type = str
	)
	parser.add_argument(
		'--agent',
		help = 'User-Agent value for HTTP-requests',
		type = str,
		default = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
	)
	parser.add_argument(
		'--http-port',
		help = 'HTTP port',
		type = int,
		default = 80
	)
	parser.add_argument(
		'--https-port',
		help = 'HTTPS port',
		type = int,
		default = 443
	)
	parser.add_argument(
		'--timeout',
		help = 'HTTP-request timeout',
		type = int,
		default = 5
	)
	parser.add_argument(
		'--threads',
		help = 'Number of threads',
		type = int,
		default = 2
	)

	args = parser.parse_args()

	return args


if __name__ == '__main__':
	main()
