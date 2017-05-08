# Summarize AWS Resources

## Description

Returns a message with the summary of AWS Resources in the account and region that the function is in.

## Dependencies:

* [boto3 1.4.4](https://pypi.python.org/pypi/boto3)

## Example response:

```
Summary for *devAccount* region *eu-west-1*:
• 4 APIs in API Gateway
• 4 Autoscaling groups
• 14 Cloudformation stacks
• 180 Cloudwatch alarms
• 85 Dynamodb tables
• 22 EBS volumes
• 12 EC2 instances (10 m4.large, 1 t2.medium, 1 t2.small)
• 2 ECS clusters
• 2 Elasticache clusters
• 3 ELB load balancers
• 90 EMR clusters (0 active, 75 terminated, 15 failed)
• 8 Lambda functions
• 2 RDS instances
• 74 Route53 zones
• 112 S3 buckets
```

## Authors:
  * Sternik
