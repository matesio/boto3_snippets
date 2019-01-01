#!/anaconda2/bin/python
import boto3
from botocore.exceptions import ClientError
from environment import *

import pprint
applicationName= applicationName
environmentName= environmentName
eb = boto3.client('elasticbeanstalk')

def describe_ebEnvironments(applicationName, environmentName ):
    try:
       return eb.describe_environments(
        ApplicationName=applicationName,
        #   VersionLabel='code-pipeline-1546076515583-AppAndMerge-d0e46138-4431-42f9-9334-435c310e8c10',
        #   IncludedDeletedBackTo=datetime(2015, 1, 1),
        EnvironmentNames=[
            environmentName
            ]
        )
    except ClientError as e:
        pprint.pprint(e.response) 

def describe_ebEvents(environmentName):
    try:
        return eb.describe_events( EnvironmentName=environmentName)
    except:
        print "something went wrong"

def instaneHealth(environmentName):
    try:
        return eb.describe_instances_health(
            AttributeNames=[
                'All'
            ],
            EnvironmentName=environmentName
        )
    except ClientError as e:
        pprint.pprint(e.response) 
#pprint.pprint (describe_ebEnvironments(applicationName,environmentName))
pprint.pprint (describe_ebEvents (environmentName))
pprint.pprint (instaneHealth(environmentName))