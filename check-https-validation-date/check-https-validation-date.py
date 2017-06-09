import json
import socket
import ssl
from datetime import datetime, timedelta
from urlparse import urlparse


def ssl_expiry_datetime(hostname):
    near = False
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(2.0)

    try:
        conn.connect((hostname, 443))
    except ssl.SSLError:
        return False, 'Not valid.', None
    except socket.error:
        return False, 'Connection refused.', None

    ssl_info = conn.getpeercert()
    expiration_date = datetime.strptime(
        ssl_info['notAfter'], ssl_date_fmt)

    if expiration_date < datetime.now() + timedelta(days=14):
        near = True

    return True, expiration_date, near


def lambda_handler(event, context):
    if 'args' not in event or not event['args'].startswith('https://'):
        return json.dumps(
            {'message': 'Missing URL or not starts with `https://`'}
        )

    check_url = ssl_expiry_datetime(urlparse(event['args']).netloc)

    if not check_url[0]:
        message = check_url[1]
    else:
        date = datetime.strftime(check_url[1], '%c')
        message = 'Expires: {}'.format(date)
        if check_url[2]:
            message = 'Warning! Expires in less than 14 days ({})'.format(date)

    return json.dumps({'message': message})
