'''
    manage.py

    Cloud Foundry service management

    @Author: rickyomax@gmail.com
'''
import json
import os
import subprocess


def runcmd(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
           stderr=subprocess.PIPE, env=None, close_fds=True):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=stdin,
                         stdout=stdout,
                         stderr=stderr,
                         env=env,
                         close_fds=close_fds)

    (out, err) = p.communicate()
    return (p.returncode, out, err)

def list_services():
    ''' List services.

    Args:
        None.

    Returns:
        A dictionary representing the services and its access status.

    '''
    # List all services
    cmd = 'cf curl /v2/services'

    rc, data, err = runcmd(cmd)

    if rc != 0:
        return {"Cause": err, "Data": "", "Outcome": False}

    data = json.loads(data)

    if 'error_code' in data:
        return {"Cause": data['description'], "Data": "", "Outcome": False}

    services = []

    for service in data['resources']:
        services.append({
            'service': service['entity']['label'],
            'service_guid': service['metadata']['guid']
        })

    # List all service plans
    cmd = 'cf curl /v2/service_plans'

    rc, data, err = runcmd(cmd)

    if rc != 0:
        return {"Cause": err, "Data": "", "Outcome": False}

    data = json.loads(data)

    if 'error_code' in data:
        return {"Cause": data['description'], "Data": "", "Outcome": False}

    service_plans = []
    for plan in data['resources']:
        service_plans.append({
            'plan_name': plan['entity']['name'],
            'plan_guid': plan['metadata']['guid'],
            'service_guid': plan['entity']['service_guid'],
            'free': plan['entity']['free'],
            'active': plan['entity']['active'],
            'access': 'on' if plan['entity']['public'] == True else 'off'
        })

    for plan in service_plans:
        for service in services:
            if plan['service_guid'] == service['service_guid']:
                plan['service'] = service['service']

    return {"Cause": "", "Data": service_plans, "Outcome": True}
