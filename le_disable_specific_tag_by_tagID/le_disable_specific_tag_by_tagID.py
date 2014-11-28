import urllib2
import json
import subprocess
import re
import sys

ACCOUNT_KEY = ''

def retrieve_alerts():
	request = {
	'request':'list',
	'account': ACCOUNT_KEY,
	'acl': ACCOUNT_KEY
	}
	req = urllib2.Request('https://api.logentries.com/v2/actions')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(request))
	response_str = response.read()
	response_dict = json.loads(response_str)

	for action in response_dict['actions']:
#		if action['type'] != 'tagit' and action['id'] == 'YOUR_TAG_ALERT_ID_GOES_HERE':
# 			action['limit_count'] = 0
# 			action['rate_count'] = 0
			action['enabled'] = 'False'

			update_alert(action)

def update_alert(alert):
	request = {
		'id': alert['id'],
		'rate_count': alert['rate_count'],
		'rate_range': alert['rate_range'],
		'limit_count': alert['limit_count'],
		'limit_range': alert['limit_range'],
		'schedule': alert['schedule'],
		'type': alert['type'],
		'args': alert['args'],
		'request': 'update',
		'account': ACCOUNT_KEY,
		'enabled': alert['enabled'],
		'acl': ACCOUNT_KEY
	}

	print json.dumps(request)
	req = urllib2.Request('https://api.logentries.com/v2/actions')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(request))
	#response_dict = json.loads(response.read())
	#print response_dict
	print response.read()

if __name__ == '__main__':
	ACCOUNT_KEY = sys.argv[1]
	retrieve_alerts()