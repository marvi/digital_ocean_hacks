#!/usr/bin/env python
#
# Removes all A records for a domain
#
# Author: Markus Härnvi <markus@harnvi.net>
#
import requests

base_url = "https://api.digitalocean.com/v2/domains/[INSERT DOMAIN HERE]/records/"
headers = {'Authorization': 'Bearer [INSERT API KEY HERE]'}

def main():
    r = requests.get(base_url, headers=headers)
    delete_all_a_records(r)
    add_record()

def delete_all_a_records(r):
    domains = r.json()['domain_records']
    a_records = [x for x in domains if x['type'] == "A"]
    for record in a_records:
        record_id = record['id']
        d = requests.delete(base_url + str(record_id), headers=headers)
        if(d.status_code == 204):
            print("Successfully deleted record for " + record['name'])
            next
        else:
            print("Error deleting record: " + str(d.status_code))
            print(d.text)
            exit(3)

