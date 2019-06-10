FROM centos/python-27-centos7

WORKDIR /tmp
USER root

RUN yum update -y 
RUN yum install -y  python2-pip
RUN pip install jenkinsapi

ADD getJenkinsHistory.py /usr/local/bin/getJenkinsHistory.py

ENTRYPOINT ["/usr/local/bin/getJenkinsHistory.py"]
