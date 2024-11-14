# Traffic Light Protcol

```text
Imagine you work as a programmer in the traffic management office of the Nexus city district's HQ. You have been informed that there was a hacker in the system and several systems have been altered and are now not working. You have been tasked to restore the random traffic light algorithm to 100% efficiency.
Flag Format: flag{Ent3rYourf4agh3r3}
```

## Notes

The lab is a website that displays the following information

### Text

```text
Traffic Flow
Current Green Light:
trains
Currently Waiting Traffic:
Cars and buses, north and south side: 10
Cars and buses, east and west side: 10
Trains: 0
Pedestrians, east and west side: 10
Pedestrians, north and south side: 10
How To Control The Green Light

The green light can be adjusted through the following requests:
POST /carsBusesNorthSouth
POST /carsBusesEastWest
POST /trains
POST /pedestriansNorthSouth
POST /pedestriansEastWest
```

### HTML

```html
    <html>
    <h1>Traffic Flow</h1>
    <h2>Current Green Light:</h2>
    trains<h2>Currently Waiting Traffic:</h2>Cars and buses, north and south side: <b>10</b><br>Cars and buses, east and west side: <b>10</b><br>Trains: <b>0</b><br>Pedestrians, east and west side: <b>10</b><br>Pedestrians, north and south side: <b>10</b><h2>How To Control The Green Light</h2><p>The green light can be adjusted through the following requests:</p><i>POST /carsBusesNorthSouth</i><br><i>POST /carsBusesEastWest</i><br><i>POST /trains</i><br><i>POST /pedestriansNorthSouth</i><br><i>POST /pedestriansEastWest</i><br></html>
```

## Requirements

Write a python script that automates the following:

- Extract the traffic data
  - Parse the HTML content to determine the currect traffic of different routes.
  - `pip install beautifulsoup4`
  - `pip install requests`
- Determine the busiest route
  - Should just be determining the max traffic
- Adjust the green light based on the parsed data
  - Send a POST request to the server
- Sleep and iterate
  - Check response code and print response text.

### Design notes

- Fetch the HTML content
  - `requests.get(url)` retrieves the webpage
- Parse the HTML
  - Use `BeautifulSoup` to extract the number of vehicles or pedestrians waiting for each route.
  - Store in a `dict` with the key being the POST address
    - ie `carsBusesNorthSouth`
- Determine the most congested route
  - Use max() to identify the route with the highest waiting traffic
    - Since data in dictionary don't forget to set `key=dict.get`
      - `max(dictionary, key=dictionary.get)`
- Send the POST request
  - Use `requests.post()` to adjust the green light
  - Print the response code and text (see below)

```python
if post_response.status_code == 200:
    print(f"Successfully changed green light to {next_light}")
    print(f"Response from the server: {post_response.text}")
else:
    print(f"Failed to change the green light, status code: {post_response.status_code}")
    print(f"Error response from the server: {post_response.text}")
```
