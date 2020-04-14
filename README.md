Domain Seeker
=====================
[![Python 3](https://img.shields.io/badge/python-3%20%2B-green.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-red.svg)](https://raw.githubusercontent.com/kaimi-io/dseeker/master/LICENSE)

# Usage
```bat
usage: dseeker.py [-h] -d DOMAINS -i IPS [--https] [--codes CODES]
                  [--separator SEPARATOR] [--include INCLUDE]
                  [--exclude EXCLUDE] [--agent AGENT] [--http-port HTTP_PORT]
                  [--https-port HTTPS_PORT] [--timeout TIMEOUT]
                  [--threads THREADS]

Domain Seeker v0.1 (c) Kaimi (kaimi.io)

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAINS, --domains DOMAINS
                        Domain list to discover (default: None)
  -i IPS, --ips IPS     IP list (ranges) to scan for domains (default: None)
  --https               Check HTTPS in addition to HTTP (default: False)
  --codes CODES         HTTP-codes list that will be considered as good
                        (default: 200,301,302,401,403)
  --separator SEPARATOR
                        IP/Domain/HTTP-codes list separator (default: ,)
  --include INCLUDE     Show results containing provided string (default:
                        None)
  --exclude EXCLUDE     Hide results containing provided string (default:
                        None)
  --agent AGENT         User-Agent value for HTTP-requests (default:
                        Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0)
                        Gecko/20100101 Firefox/40.1)
  --http-port HTTP_PORT
                        HTTP port (default: 80)
  --https-port HTTPS_PORT
                        HTTPS port (default: 443)
  --timeout TIMEOUT     HTTP-request timeout (default: 5)
  --threads THREADS     Number of threads (default: 2)
```

For further assistance don't hesitate to ask for help in GitHub issues or on the blog: https://kaimi.io
