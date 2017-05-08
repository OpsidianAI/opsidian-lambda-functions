# -*- coding: utf-8 -*-

# Description
#   Returns a message with the summary of AWS Resources.
#
# Dependencies:
#   "boto3": "1.4.4"
#
# Author:
#   Sternik

from collections import Counter
import json
import boto3


def api_gateways():
    client = boto3.client('apigateway')
    response = client.get_rest_apis(limit=500)

    num_results = 0
    if 'items' in response:
        num_results = len(response['items'])
        while 'position' in response:
            response = client.get_rest_apis(
                position=response['position'],
                limit=500
            )
            num_results += len(response['items'])

    return num_results,


def autoscaling_groups():
    client = boto3.client('autoscaling')
    response = client.describe_auto_scaling_groups()

    num_results = 0
    if 'AutoScalingGroups' in response:
        num_results = len(response['AutoScalingGroups'])
        while 'NextToken' in response:
            response = client.describe_auto_scaling_groups(
                NextToken=response['NextToken']
            )
            num_results += len(response['AutoScalingGroups'])

    return num_results,


def cloudformation_stacks():
    client = boto3.client('cloudformation')
    response = client.list_stacks()

    num_results = 0
    if 'StackSummaries' in response:
        num_results = len(response['StackSummaries'])
        while 'NextToken' in response:
            response = client.list_stacks(
                NextToken=response['NextToken']
            )
            num_results += len(response['StackSummaries'])

    return num_results,


def cloudwatch_alarms():
    client = boto3.client('cloudwatch')
    response = client.describe_alarms()

    num_results = 0
    if 'MetricAlarms' in response:
        num_results = len(response['MetricAlarms'])
        while 'NextToken' in response:
            response = client.describe_alarms(
                NextToken=response['NextToken']
            )
            num_results += len(response['MetricAlarms'])

    return num_results,


def dynamodb_tables():
    client = boto3.client('dynamodb')
    response = client.list_tables()

    items = []
    if 'TableNames' in response:
        items.extend(response['TableNames'])

        while 'LastEvaluatedTableName' in response:
            response = client.list_tables(
                ExclusiveStartTableName=response['LastEvaluatedTableName']
            )
            items.extend(response['TableNames'])

    return len(items),


def ebs_volumes():
    client = boto3.client('ec2')
    response = client.describe_volumes()

    num_results = 0
    if 'Volumes' in response:
        num_results = len(response['Volumes'])
        while 'NextToken' in response:
            response = client.describe_volumes(
                NextToken=response['NextToken']
            )
            num_results += len(response['Volumes'])

    return num_results,


def ec2_instance():
    client = boto3.client('ec2')
    response = client.describe_instances()

    items = []
    resp = []
    if 'Reservations' in response:
        for reservation in response['Reservations']:
            items.extend(reservation['Instances'])
        while 'NextToken' in response:
            response = client.describe_instances(
                NextToken=response['NextToken']
            )
            for reservation in response['Reservations']:
                items.extend(reservation['Instances'])

        types = Counter([_['InstanceType'] for _ in items])
        for instance in sorted(types.iterkeys()):
            resp.append('{} {}'.format(types[instance], instance))

    return len(items), ', '.join(resp)


def ecs_clusters():
    client = boto3.client('ecs')
    response = client.list_clusters()

    num_results = 0
    if 'clusterArns' in response:
        num_results = len(response['clusterArns'])
        while 'nextToken' in response:
            response = client.list_clusters(
                nextToken=response['nextToken']
            )
            num_results += len(response['clusterArns'])

    return num_results,


def elasticache_clusters():
    client = boto3.client('elasticache')
    response = client.describe_cache_clusters()

    num_results = 0
    if 'CacheClusters' in response:
        num_results = len(response['CacheClusters'])
        while 'Marker' in response:
            response = client.describe_cache_clusters(
                Marker=response['Marker']
            )
            num_results += len(response['CacheClusters'])

    return num_results,


def elb_balancers():
    client = boto3.client('elb')
    response = client.describe_load_balancers()

    num_results = 0
    if 'LoadBalancerDescriptions' in response:
        num_results = len(response['LoadBalancerDescriptions'])
        while 'Marker' in response:
            response = client.describe_load_balancers(
                Marker=response['Marker']
            )
            num_results += len(response['LoadBalancerDescriptions'])

    return num_results,


def emr_clusters():
    client = boto3.client('emr')
    response = client.list_clusters()

    items = []
    active = terminated = failed = 0
    if 'Clusters' in response:
        items.extend(response['Clusters'])
        while 'Marker' in response:
            response = client.list_clusters(
                Marker=response['Marker']
            )
            items.extend(response['Clusters'])

        for item in items:
            state = item['Status']['State']
            if state in ['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING']:
                active += 1
            elif state in ['TERMINATING', 'TERMINATED']:
                terminated += 1
            elif state in ['TERMINATED_WITH_ERRORS']:
                failed += 1

    resp = '{} active, {} terminated, {} failed'.format(
        active, terminated, failed)
    return len(items), resp


def lambda_functions():
    client = boto3.client('lambda')
    response = client.list_functions()

    num_results = 0
    if 'Functions' in response:
        num_results = len(response['Functions'])
        while 'NextMarker' in response:
            response = client.list_functions(
                Marker=response['NextMarker']
            )
            num_results += len(response['Functions'])

    return num_results,


def rds_instances():
    client = boto3.client('rds')
    response = client.describe_db_instances()

    num_results = 0
    if 'DBInstances' in response:
        num_results = len(response['DBInstances'])
        while 'Marker' in response:
            response = client.describe_db_instances(
                Marker=response['Marker']
            )
            num_results += len(response['DBInstances'])

    return num_results,


def route53_zones():
    client = boto3.client('route53')
    response = client.list_hosted_zones()

    num_results = 0
    if 'HostedZones' in response:
        num_results = len(response['HostedZones'])
        while 'NextMarker' in response:
            response = client.list_hosted_zones(
                Marker=response['NextMarker']
            )
            num_results += len(response['HostedZones'])

    return num_results,


def s3_buckets():
    client = boto3.client('s3')
    response = client.list_buckets()

    num_results = 0
    if 'Buckets' in response:
        num_results = len(response['Buckets'])

    return num_results,


aws_services = {
    'apigateway': {
        'command': api_gateways,
        'text': '• {d[0]} API{s} in API Gateway'
    },
    'autoscaling': {
        'command': autoscaling_groups,
        'text': '• {d[0]} Autoscaling group{s}'
    },
    'cloudformation': {
        'command': cloudformation_stacks,
        'text': '• {d[0]} Cloudformation stack{s}'
    },
    'cloudwatch': {
        'command': cloudwatch_alarms,
        'text': '• {d[0]} Cloudwatch alarm{s}'
    },
    'dynamodb': {
        'command': dynamodb_tables,
        'text': '• {d[0]} Dynamodb table{s}'
    },
    'ebs': {
        'command': ebs_volumes,
        'text': '• {d[0]} EBS volume{s}'
    },
    'ec2': {
        'command': ec2_instance,
        'text': '• {d[0]} EC2 instance{s} ({d[1]})'
    },
    'ecs': {
        'command': ecs_clusters,
        'text': '• {d[0]} ECS cluster{s}'
    },
    'elasticache': {
        'command': elasticache_clusters,
        'text': '• {d[0]} Elasticache cluster{s}'
    },
    'elb': {
        'command': elb_balancers,
        'text': '• {d[0]} ELB load balancer{s}'
    },
    'emr': {
        'command': emr_clusters,
        'text': '• {d[0]} EMR cluster{s} ({d[1]})'
    },
    'lambda': {
        'command': lambda_functions,
        'text': '• {d[0]} Lambda function{s}'
    },
    'rds': {
        'command': rds_instances,
        'text': '• {d[0]} RDS instance{s}'
    },
    'route53': {
        'command': route53_zones,
        'text': '• {d[0]} Route53 zone{s}'
    },
    's3': {
        'command': s3_buckets,
        'text': '• {d[0]} S3 bucket{s}'
    },
}


def lambda_handler(event, context):
    results = []
    for service in sorted(aws_services.iterkeys()):
        response = aws_services[service]['command']()
        if response:
            count = ''
            if response[0] > 1:
                count = 's'

            results.append(aws_services[service]['text'].format(
                d=response, s=count))

    message = ('Summary for *{}* region *{}*:\n{}').format(
        event['account_name'], event['region'], '\n'.join(results))

    return json.dumps(
        {'message': message}
    )
