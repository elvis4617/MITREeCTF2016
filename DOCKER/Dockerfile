## Ubuntu Image (Get by calling "docker pull ubuntu")
FROM ubuntu

MAINTAINER Keith Miller

RUN apt-get update

RUN apt-get install -y python python-dev python-pip

RUN pip install twisted 

# RUN pip install pyopenssl

ADD /dockCTF /dockCTF

WORKDIR /dockCTF

EXPOSE 9500

CMD python server.py
