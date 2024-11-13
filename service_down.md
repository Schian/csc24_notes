# Service Down

## Notes

```text
You are an administrator working in the command centre for the NeoCity. You are tasked with monitoring several critical services that are running to manage various NeoCity's functions, such as traffic control, waste management, and energy distribution. One of these services has unexpectedly stopped running, causing disruptions in the NeoCity's operations. Identify which service has failed, fix the problem, and get it running again. The ssh credentials to access the machine are service:service. Flag format: flag{ctf-423923fdasiukjhdk}
```

`sudo -l`

```text
User service may run the following commands on 54cc56d416f2:
    (ALL) NOPASSWD: /usr/bin/systemctl restart traffic_control, /usr/bin/systemctl start traffic_control, /usr/bin/systemctl stop traffic_control, /usr/bin/systemctl status traffic_control, /usr/bin/systemctl restart waste_management, /usr/bin/systemctl start waste_management, /usr/bin/systemctl stop
        waste_management, /usr/bin/systemctl status waste_management, /usr/bin/systemctl restart energy_distribution, /usr/bin/systemctl start energy_distribution, /usr/bin/systemctl stop energy_distribution, /usr/bin/systemctl status energy_distribution, /usr/sbin/service postgresql start, /usr/sbin/service
        postgresql stop, /usr/sbin/service postgresql status, /usr/sbin/service postgresql restart
```

- traffic_control
- waste_management
- energy_distribution
- postgresql

- restart
- start
- stop
- status

`journalctl -u energy_distribution` gave the following output

```text
16/main (port 5432): down
16/main (port 5432): down
16/main (port 5432): down
/var/log/journal/energy_distribution.service.log (END)
```

- port 5432 is for a postgresql server
- `sudo service postgresql start` to start the postgresql server
- `netstat -tuln | grep 5432` to check the service is running
  - tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN
- `sudo systemctl restart energy_distribution`
- `sudo /usr/bin/systemctl status energy_distribution`
  - energy_distribution.service - energy distribution service
  - Loaded: loaded (/etc/systemd/system/energy_distribution.service, disabled)
  - Active: failed (failed)
- `journalctl -u energy_distribution`
  - 16/main (port 5432): online

Tried the following for postgresql

```text
service@54cc56d416f2:~$ journalctl -u postgresql
/var/log/journal/postgresql.service.log: No such file or directory
service@54cc56d416f2:~$ /usr/sbin/service postgresql status
16/main (port 5432): online
service@54cc56d416f2:~$ 
```

---

Looked at the `.service` files for our critical services.

```text
service@54cc56d416f2:/etc/systemd/system$ ll
total 48
drwxr-xr-x 1 root root 4096 Nov  4 01:42 ./
drwxr-xr-x 1 root root 4096 Nov  4 01:40 ../
lrwxrwxrwx 1 root root   48 Nov  4 01:40 dbus-org.freedesktop.resolve1.service -> /usr/lib/systemd/system/systemd-resolved.service
lrwxrwxrwx 1 root root   49 Nov  4 01:40 dbus-org.freedesktop.timesync1.service -> /usr/lib/systemd/system/systemd-timesyncd.service
-rw-rw-r-- 1 root root  251 Nov  1 10:01 energy_distribution.service
drwxr-xr-x 2 root root 4096 Nov  4 01:40 getty.target.wants/
drwxr-xr-x 1 root root 4096 Nov  4 01:42 multi-user.target.wants/
drwxr-xr-x 2 root root 4096 Nov  4 01:40 sockets.target.wants/
drwxr-xr-x 2 root root 4096 Nov  4 01:40 ssh.service.requires/
drwxr-xr-x 2 root root 4096 Nov  4 01:40 sysinit.target.wants/
drwxr-xr-x 2 root root 4096 Nov  4 01:42 sysstat.service.wants/
drwxr-xr-x 1 root root 4096 Nov  4 01:42 timers.target.wants/
-rw-rw-r-- 1 root root  243 Nov  1 10:01 traffic_control.service
-rw-rw-r-- 1 root root  245 Nov  1 10:01 waste_management.service
service@54cc56d416f2:/etc/systemd/system$ cat energy_distribution.service 
[Unit]
Description=energy distribution service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/env python3 /code/energy_distribution.py

[Install]
WantedBy=multi-user.target
service@54cc56d416f2:/etc/systemd/system$ cat traffic_control.service 
[Unit]
Description=traffic control service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/env python3 /code/traffic_control.py

[Install]
WantedBy=multi-user.target
service@54cc56d416f2:/etc/systemd/system$ cat waste_management.service 
[Unit]
Description=waste management service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/env python3 /code/waste_management.py

[Install]
WantedBy=multi-user.target
```

The three python files are owned by root and are only read/writeable by root

---

I checked `/var/log` and ran `tail energy_distribution.log`

```text
2024-11-13 07:16:04 ENERGY DISTRIBUTION operating normally
2024-11-13 07:16:05 ENERGY DISTRIBUTION postgresql service check: postgresql service is running
2024-11-13 07:16:06 ENERGY DISTRIBUTION database existence check ERROR: psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "energy_distribution" does not exist
```

---

- Connect to the postgresql database with `psql -h 127.0.0.1 -U service -d postgres`
- Create new database `CREATE DATABASE ENERGY_DISTRIBUTION;`
  - Quit with `quit`
- Restart the service with `sudo /usr/sbin/service postgresql restart`
- Check the logs

```text
service@54cc56d416f2:/etc/postgresql/16/main$ cat /var/log/energy_distribution.log 
2024-11-04 01:42:34 ENERGY DISTRIBUTION operating normally
2024-11-04 01:42:35 ENERGY DISTRIBUTION postgresql service check: ERROR: postgresql service not running, exiting now
2024-11-04 01:43:51 ENERGY DISTRIBUTION operating normally
2024-11-04 01:43:52 ENERGY DISTRIBUTION postgresql service check: ERROR: postgresql service not running, exiting now
2024-11-13 07:51:23 ENERGY DISTRIBUTION operating normally
2024-11-13 07:51:24 ENERGY DISTRIBUTION postgresql service check: ERROR: postgresql service not running, exiting now
2024-11-13 07:52:20 ENERGY DISTRIBUTION operating normally
2024-11-13 07:52:21 ENERGY DISTRIBUTION postgresql service check: postgresql service is running
2024-11-13 07:52:22 ENERGY DISTRIBUTION database existence check ERROR: psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "energy_distribution" does not exist

2024-11-13 08:03:57 ENERGY DISTRIBUTION operating normally
2024-11-13 08:03:59 ENERGY DISTRIBUTION postgresql service check: postgresql service is running
2024-11-13 08:04:00 ENERGY DISTRIBUTION database existence check: pass 
2024-11-13 08:04:01 ENERGY DISTRIBUTION web service check: sending the data to http://localhost:8000..
2024-11-13 08:04:01 ENERGY DISTRIBUTION web service check: ERROR, please start a web server on localhost:8000 to receive the data
```

---

Created a second ssh connection and started a python http server with `python3 -m http.server 8000` and restarted the service `sudo systemctl restart energy_distribution`.

But the python server only supports 'GET' requests and the service is sending a 'POST' request. I need to use flask, I quickly check that it is available by starting a python interpretor and trying to import. It succeeds.

I get ChatGPT to create a flask server for me

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

I run it and restart energy_distribution (again) and I have success!

```text
python3 server.py 
 * Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.18.0.2:8000
Press CTRL+C to quit
Received data: {"flag": "ctf-412390adsajklzc9ssk"}
127.0.0.1 - - [13/Nov/2024 08:16:05] "POST / HTTP/1.1" 200 -
```

`FLAG{ctf-412390adsajklzc9ssk}`
