#!/bin/python2.7

from jenkinsapi.jenkins import Jenkins
import os
from traceback import format_exc

url_get_all_builds = "http://18.222.147.201:8080//job/{}/api/json?tree=allBuilds[*]&depth=2"
version_base = "1.0.0"


def get_server_instance():

    server = Jenkins(jenkins_url, username = 'kasema', password = 'admin')
    return server


def getSCMInfroFromLatestGoodBuild(url, jobName, tags, username=None, password=None):
    specific_url = url_get_all_builds.format(jobName)
    j = Jenkins(url, username, password)
    job = j[jobName]
    lgb = job.get_last_good_build()
    last_build_number = job.get_last_buildnumber()
    last_build_tag = tags[-1]

    #new_tag = (int(''.join(last_build_tag.split('.'))) + 1)
    # lf = open('/home/ec2-user/workspace/piplineJob/logfile.log', 'w')
    if not last_build_number:
        return
    for i in range(last_build_number, 0, -1):
        try:
            build = job.get_build(i)
            print build.get_timestamp()
            # lf.write('{}'.format(build.get_timestamp()))
            # lf.write('\n')
            print build.get_timestamp()
        except KeyError:
            break


if __name__ == '__main__':
    # lf = open('/home/ec2-user/workspace/piplineJob/logfile.log', 'w')
    # try:
        #job_name = 'testing'
        job_name = 'testing'#os.environ['JOB_NAME']
        username = 'kasema'#os.environ['JENKINS_USERNAME']
        password = 'admin'#os.environ['JENKINS_PASSWORD']
        jenkins_url = "http://18.222.147.201:8080"#os.environ['JENKINS_URL']
        tags = os.environ['BUILD_TAG']
        getSCMInfroFromLatestGoodBuild(jenkins_url, job_name, tags, username, password)
    # except:
    #     lf.write(format_exc())
    #     lf.write('\n')
    # finally:
    #     lf.flush()
    #     lf.close()
