# Keys credential reports 

## Description

Generates a credential report and checks if keys were rotated within last X days. 

## Arguments

By default the function check last 90 days. You can pass the number of days as an argument. 

## Dependencies:

* [boto3 1.4.4](https://pypi.python.org/pypi/boto3)

## Permissions

Your Lambda needs the following permissions:

```
iam:GenerateCredentialReport
iam:GetCredentialReport

```

## Example response:

```
User anna needs their access_key_1 rotated !!
User jack needs their access_key_2 rotated !!
```

## Authors:
  * Dariusz Dwornikowski, Nordcloud.com
