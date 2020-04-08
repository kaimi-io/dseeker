FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 LC_ALL=C.UTF-8 LANGUAGE=en_US.UTF-8
RUN apt-get update
RUN apt-get -y install python3-coloredlogs python3-urllib3 python3-netaddr
COPY src /src
ENTRYPOINT [ "python3", "/src/dseeker.py" ]
