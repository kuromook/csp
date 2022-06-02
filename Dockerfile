FROM ubuntu:latest

RUN apt update -y ; apt upgrade -y
RUN apt install -y vim python3
RUN apt install -y python3-distutils
RUN apt install -y mecab
RUN cp /etc/mecabrc /usr/local/etc/mecabrc
RUN apt install -y curl


WORKDIR /csp
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python3 get-pip.py
RUN pip install mecab-python3

CMD python3 convertTextFile.py
