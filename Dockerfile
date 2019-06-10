FROM centos/python-27-centos7

WORKDIR /tmp
USER root

RUN yum update -y 

ADD getJenkinsHistory.py /usr/local/bin/getJenkinsHistory.py

ENTRYPOINT ["/usr/local/bin/getJenkinsHistory.py"]
