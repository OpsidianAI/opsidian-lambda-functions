# -*- coding: utf-8 -*-

# Description
#  Returns a list of users who need their keys rotated 
#
# Notes:
#   Default days 90
# 
# Arguments:
#   days - number of days to check the retention
#
# Dependencies:
#   "boto3": "1.4.4"
#
# Author:
#   tdi

import base64
import os
import json
import time
import boto3
import csv
from StringIO import StringIO
from datetime import timedelta, datetime
from dateutil.parser import parse

_version_ = "1.0"

def check_retention(days, key_date):
    """
    Returns True when keys was last rotated more than :days: ago
    """
    key_date = parse(key_date, ignoretz=True)
    return (key_date + timedelta(days=days)) <= datetime.now()


def lambda_handler(event, context):
    
    days = 90 

    try:
        if 'args' in event and 'days' in event['args']:
            days = int(event['args']['days'])
            
        iam = boto3.client('iam')
 
        w_time = 0
        while iam.generate_credential_report()['State'] != 'COMPLETE':
            w_time = w_time + 5
            print("Waiting...{}".format(w_time))
            time.sleep(w_time)
        print("Report is ready")
        report = iam.get_credential_report()
        csv_reader = csv.DictReader(StringIO(report['Content']))
        message = ""
        for r in csv_reader:
            if r['access_key_1_active'] == "true":
                if check_retention(days, r['access_key_1_last_rotated']):
                    message = message + "User {} needs their access_key_1 rotated !! \n".format(r['user']) 
            elif r['access_key_2_active'] == "true":
                if check_retention(days, r['access_key_2_last_rotated']):
                    message = message + "User {} needs their access_key_2 rotated !! \n".format(r['user']) 
        if message == "":
            message = ":+1: All users' keys are up to date !"
    except Exception as e:
        print(str(e))
        raise e
        
    return json.dumps({'message': message})
