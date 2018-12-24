# digital_ocean_hacks
Code snippets for working with Digital Ocean API


## update_a_record.py

I use this from Puppet to add the current Droplet's IP into Digital Ocean 
DNS service. It first deletes all A records for a specified hostname and 
then adds a new A record for the current IPv4 address.

