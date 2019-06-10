FROM centos/python-27-centos7

RUN yum update -y 


ADD getJenkinsHistory.py /usr/local/bin/getJenkinsHistory.py


WORKDIR /tmp
USER root

ENTRYPOINT ["/usr/local/bin/getJenkinsHistory.py"]
