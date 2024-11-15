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

##############################################################################
# Parse the HTML contents
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the traffic data
traffic_data = {
    "carsBusesNorthSouth": int(soup.find(
        string="Cars and buses, north and south side: ").find_next('b').text),
    "carsBusesEastWest": int(soup.find(
        string="Cars and buses, east and west side: ").find_next("b").text),
    "trains": int(soup.find(
        string="Trains: ").find_next("b").text),
    "pedestriansNorthSouth": int(soup.find(
        string="Pedestrians, north and south side: ").find_next("b").text),
    "pedestriansEastWest": int(soup.find(
        string="Pedestrians, east and west side: ").find_next("b").text)
}
##############################################################################
# Determine the next green
next_green = max(traffic_data, key=traffic_data.get)

##############################################################################
# Send the POST request

# Craft the POST request
post_url = f"{url}/{next_green}"

# Send the POST request
post_response = requests.post(post_url)

# Review the POST response
if post_response.status_code == 200:
    print(f"Successfully changed green light to {next_green}.\n"
          f"\tResponse from the server: {post_response.text}\n")
else:
    print(f"Failed to change the green light.\n"
          f"\tStatus code: {post_response.status_code}"
          f"\tServer Response: {post_response.text}")
