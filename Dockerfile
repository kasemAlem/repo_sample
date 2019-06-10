FROM centos/python-27-centos7

WORKDIR /tmp
USER root

RUN yum update -y 
RUN /bin/bash -c 'pip install jenkinsapi'

ADD getJenkinsHistory.py /usr/local/bin/getJenkinsHistory.py

ENV PYTHONPATH /opt/rh/rh-nodejs10/root/usr/lib/python2.7/site-packages:/opt/app-root/lib64/python27.zip:/opt/app-root/lib64/python2.7:/opt/app-root/lib64/python2.7/plat-linux2:/opt/app-root/lib64/python2.7/lib-tk:/opt/app-root/lib64/python2.7/lib-old:/opt/app-root/lib64/python2.7/lib-dynload:/opt/rh/python27/root/usr/lib/python2.7:/opt/app-root/lib/python2.7/site-packages
ENV LD_LIBRARY_PATH /opt/rh/python27/root/usr/lib64

ENTRYPOINT ["/usr/local/bin/getJenkinsHistory.py"]
