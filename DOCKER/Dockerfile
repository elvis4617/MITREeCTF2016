## Ubuntu Image (Get by calling "docker pull ubuntu")
FROM ubuntu

MAINTAINER Keith Miller

RUN apt-get update

RUN apt-get install -y python python-dev python-pip python-openssl

RUN apt-get -y upgrade

RUN pip install twisted service_identity

#RUN pip install pyopenssl

ADD /door_app /door_app

WORKDIR /door_app

EXPOSE 9500

CMD ["python", "server.py"]
