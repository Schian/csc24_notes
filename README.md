# Cyber Skills Challenge 2024

## Evaluate Your Cost

- Connect using `nc 10.2.250.8 1337`
- Asks for amount to convert
- Give it a value and it converts
- Based off the name of the challenge `eval()` in use
  - executes arbitrarty python code
- test with `'hello'.upper`
  - returns `HELLO`
- Use python's inbuilt function to open and read the `flag.txt` file
  - `open('flag.txt').read()`

### `Result: FLAG{3V4LU4T3D_5UCC35SFU11Y}`

## bake-sale

- nmap scan, port 3000 open and indication it is a website
- navigate to the website
- link in the corner to "View Order Totals"
- Not allowed to view
- Check cookies to see what is there, two cookies
- Notice the `%3D` at the end, URL-encoding for `=` and `=` is a padding character for base64
- Remove `%3D` and replace with `=` then convert from base64 and get `false`
- Encode `true` to base64 and replace `=` with `%3D`
- Paste into my cookie
- Change the name so I look cool
- Refesh page

### `FLAG{0nly_s1gned_c00kies_4_m3!}`

## Service Down

- `sudo -l` revealed what commands I can run as `sudo`
- `journalctl -u energy_distribution` revealved energy distribution was the problem
- Port 5432 was down
  - This is the port for postgresql
  - `sudo service postgresql start`
  - `netstat -tuln | grep 5432` to check the service is running
  - `sudo systemctl restart energy_distribution` but still returns failed
- Check the .`service` file for energy_distribution
  - `.py` file is the ExecStart
  - The `.py` file is owned by `root` and not readable/writeable
- Checked `/var/log` and ran `tail energy_distribution.log`
  - "FATAL:  database "energy_distribution" does not exist`
  - Connect to the postgresql database with `psql -h 127.0.0.1 -U service -d postgres`
  - Create new database `CREATE DATABASE ENERGY_DISTRIBUTION;`
  - Quit with `quit`
  - Restart the postgresql with `sudo /usr/sbin/service postgresql restart`
  - Restart the service with `sudo systemctl restart energy_distribution`
- Checked `/var/log` and ran `tail energy_distribution.log`
  - "ENERGY DISTRIBUTION web service check: ERROR, please start a web server on localhost:8000 to receive the data"
  - `python3 -m http.server 8000` fails because it cannot handle POST requests
  - Get ChatGPT to create a flask server for me (code below)
  - Restart the service `sudo systemctl restart energy_distribution`
  - "Received data: {"flag": "ctf-412390adsajklzc9ssk"} 127.0.0.1 - - [13/Nov/2024 08:16:05] "POST / HTTP/1.1" 200 -"

### `FLAG{ctf-412390adsajklzc9ssk}`

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_data():
    data = request.data.decode('utf-8')  # Read POST data
    print(f"Received data: {data}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

## Flagpypi

- Created a python virtual environment with `python3 -m venv ./.venv`
- Installed the package with `pip install flagpypi`
- `main.py` contains the below

```text
def flag():
    return "fake flag"
```

- Use the PyPI API to get a `.json` of all the release metadata.
  - `curl -s https://pypi.org/pypi/flagpypi/json | jq . | flagpypi.json`
- Use some bash commands to find the largest file size
  - `cat flagpypi.json | grep "size" | cut -d':' -f2 | sort -nr | head`
  - `cat flagpypi.json | grep -A5 -B5 '"size": 1565'`
- The largest filesize is the release: 2.2.11 and the `.whl` file
  - Download and unzip this file
  - `cat main.py`

### `flag{1_h0p3_y0u_foUnD_1t_1n_4n_3ff1c13nt_w4y}`

## Host Unknown presents: Accepted the Risk

- nmap scan
  - open SMB ports
- enum4linux
  - can connect anonumously
- enumerate all shares
  - `get flag.zip`
  - password protected
- crack password
  - `zip2john flag.zip > flag.hash`
  - `john --wordlist=/usr/share/wordlists/rockyou.txt flag.hash`
    - `100%smart        (flag.zip/flag.txt)`

### `FLAG{4CC3PT3D_TH3_R1SK_TH1S_T1M3}`

## Traffic light protocol

- Created a python virtual environment
  - `pip install beautifulsoup4`
  - `pip install requests`
- Fetch HTML contents
- Parse HTML contents
  - Used a dictionary `lights:waiting`
- Determined the next green light
  - `max(traffic_data, key=traffic_data.get)`
- Craft and send the POST request
- Review the POST response

### `flag{8f9asdjk2jd9afjlz}`

## Round Bridge

- Unzip
- Reverse Image Search

### `FLAG{laguna_garzon_bridge}`
