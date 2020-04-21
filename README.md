Domain Seeker
=====================
[![Python 3](https://img.shields.io/badge/python-3%20%2B-green.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-red.svg)](https://raw.githubusercontent.com/kaimi-io/dseeker/master/LICENSE)

Simple script for domain discovery within specified IP ranges.

## Contents
- [Requirements](#Requirements)
  - [Environment](#Environment)
  - [Python modules](#Python-modules)
- [Installation](#Installation)
  - [Ubuntu / Debian](#ubuntu--debian)
  - [MacOS](#MacOS)
  - [Windows](#Windows)
  - [Docker](#Docker)
- [Usage](#Usage)
- [Contribute](#Contribute)
- [License](#License)

## Requirements
### Environment
* Linux/Windows/MacOS (anything, that runs Python)
* Python >= 3

### Python modules
* coloredlogs==14.0
* urllib3==1.25.8
* netaddr==0.7.19

## Installation
### Ubuntu / Debian
```bash
# Prerequisites
sudo apt-get update
sudo apt-get -y install python3 python3-coloredlogs python3-urllib3 python3-netaddr

# Get a copy and run
git clone https://github.com/kaimi-io/dseeker.git
cd dseeker/src
python3 dseeker.py -h
```
### MacOS
1. Install brew (https://brew.sh/)
2. Run:
```bash
brew update
brew install python3

git clone https://github.com/kaimi-io/dseeker.git
cd dseeker/src
pip3 install -r requirements.txt

python3 dseeker.py -h
```
### Windows
With WSL (Windows Subsystem for Linux) installation will be similar to [Ubuntu / Debian](#ubuntu--debian).
Otherwise:
1. Download and install Python 3 (http://python.org/)
2. Ensure, that Python was added to system `PATH` environment variable
3. From Windows command line run:
```python3 --version```

It should output Python version. If not, refer to Python distribution documentation about adding Python to your `PATH` environment variable.

4. Download and unpack Domain Seeker (https://github.com/kaimi-io/dseeker/archive/master.zip)
5. Install required modules:
```bash
cd dseeker/src
pip3 install -r requirements.txt
```
6. Run:
```bash
python3 dseeker.py -h
```

### Docker
1. Install Docker (https://docs.docker.com/get-docker/)
2. Run:
```bash
git clone https://github.com/kaimi-io/dseeker.git
cd dseeker
docker build --tag dseeker:1.0 .
docker run --rm --name dseeker dseeker:1.0 -h
```

## Usage
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

## Contribute
If you want to help make Domain Seeker better the easiest thing you can do is to report issues and feature requests. Or you can help in development.

## License
Domain Seeker Copyright © 2016-2020 by Kaimi (Sergey Belov) - https://kaimi.io

Domain Seeker is free software: you can redistribute it and/or modify it under the terms of the Massachusetts Institute of Technology (MIT) License.

You should have received a copy of the MIT License along with Domain Seeker. If not, see [MIT License](LICENSE)
