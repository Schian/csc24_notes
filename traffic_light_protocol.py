#! /home/ajw/Documents/csc24_notes/.venv/bin/python

"""Script to solve the "Traffi Light Protocol" challenge in the ADF CSC24.

This script requires requests and beautifulsoup4
Imagine you work as a programmer in the traffic management office of the Nexus
city district's HQ. You have been informed that there was a hacker in the
system and several systems have been altered and are now not working. You have
been tasked to restore the random traffic light algorithm to 100% efficiency.

Flag Format: flag{Ent3rYourf4agh3r3}

IP: 10.1.253.46 (changes each time the lab resets)
"""

import requests
from bs4 import BeautifulSoup


##############################################################################
# Fetch the HTML contents
url = "http://10.1.253.46"  # This will have to be changed on lab reset
url_response = requests.get(url)

# Check the response code
if url_response.status_code != 200:
    print(f"Failed to fetch the page, status code: "
          f"{url_response.status_code}")
    exit()

html_content = url_response.text

print(html_content)

