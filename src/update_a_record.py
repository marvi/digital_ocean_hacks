#!/usr/bin/env python
#
# Updates Digital Ocean DNS with hostname and IP for this host. It removes any
# A records previously added for this hostname.
#
import requests

base_url = "https://api.digitalocean.com/v2/domains/[INSERT DOMAIN HERE]/records/"
headers = {'Authorization': 'Bearer [INSERT API KEY HERE]'}

def main():
    r = requests.get(base_url, headers=headers)
    delete_a_records(r)
    add_record()

def delete_a_records(r):
    domains = r.json()['domain_records']
    a_records = [x for x in domains if x['name'] == "[INSERT HOSTBAME HERE]"]
    for record in a_records:
        record_id = record['id']
        d = requests.delete(base_url + str(record_id), headers=headers)
        if(d.status_code == 204):
            next
        else:
            print("Error deleting record: " + str(d.status_code))
            print(d.text)
            exit(3)

def add_record():
    ip = get_ip()
    r = requests.post(base_url,
                      json={"type": "A",
                            "name": "[INSERT HOSTBAME HERE]",
                            "data": ip,
                            "ttl": "600"},
                     headers=headers)

    if(r.status_code == 201):
        return
    else:
        print("Error adding record: " + str(r.status_code))
        print(r.text)
        exit(3)

def get_ip():
    r = requests.get("http://169.254.169.254/metadata/v1/interfaces/public/0/ipv4/address")
    return r.text


if __name__== "__main__":
  main()
