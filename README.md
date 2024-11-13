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