#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import csv
import sys

import duo_client
from six.moves import input

argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)

# Configuration and information about objects to create.
admin_api = duo_client.Admin(
    ikey=get_next_arg('Admin API integration key ("DI..."): '),
    skey=get_next_arg('integration secret key: '),
    host=get_next_arg('API hostname ("api-....duosecurity.com"): '),
)



# Retrieve user info from API:
logs = admin_api.get_activity_logs(mintime=1661016735000, maxtime=1661880735000)

# Print CSV of username, phone number, phone type, and phone platform:
#
# (If a user has multiple phones, there will be one line printed per
# associated phone.)
reporter = csv.writer(sys.stdout)
print("[+] Report of all users and associated phones:")
# reporter.writerow(('Username', 'Phone Number', 'Type', 'Platform'))
for log in logs:
    reporter.writerow([
            log["username"],

    ])
