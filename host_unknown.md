# Host Unknown presents: Accepted the Risk

## Nmap

```text
──(kali㉿kali)-[~/Workspace/ADFCSA/2024-csc]
└─$ sudo nmap -sS $IP                                                 
[sudo] password for kali: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-14 19:10 AEDT
Nmap scan report for 10.7.98.133
Host is up (0.038s latency).
Not shown: 998 closed tcp ports (reset)
PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 0.58 seconds
                                                                                                                                                            
┌──(kali㉿kali)-[~/Workspace/ADFCSA/2024-csc]
└─$ sudo nmap -sS $IP -p139,445 -A                                   
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-14 19:12 AEDT
Nmap scan report for 10.7.98.133
Host is up (0.022s latency).

PORT    STATE SERVICE     VERSION
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 4.15 - 5.8 (95%), Linux 5.0 (95%), Linux 5.0 - 5.4 (95%), Linux 5.3 - 5.4 (95%), Linux 5.0 - 5.5 (95%), Linux 3.1 (94%), Linux 3.2 (94%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 2.6.32 (94%), HP P2000 G3 NAS device (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)

TRACEROUTE (using port 445/tcp)
HOP RTT      ADDRESS
1   63.40 ms 10.9.0.1
2   12.86 ms 10.7.98.133

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.61 seconds
```

## enum4linux

```text
└─$ enum4linux $IP -A | tee enum4linux.txt
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Thu Nov 14 19:19:11 2024

 =========================================( Target Information )=========================================

Target ........... 10.7.98.133
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ============================( Enumerating Workgroup/Domain on 10.7.98.133 )============================


[E] Can't find workgroup/domain



 ================================( Nbtstat Information for 10.7.98.133 )================================

Looking up status of 10.7.98.133
No reply from 10.7.98.133

 ====================================( Session Check on 10.7.98.133 )====================================


[+] Server 10.7.98.133 allows sessions using username '', password ''


 =================================( Getting domain SID for 10.7.98.133 )=================================

Domain Name: WORKGROUP
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup


 ===================================( OS information on 10.7.98.133 )===================================
                                                                                                                                                            
                                                                                                                                                            
[E] Can't get OS info with smbclient                                                                                                                        
                                                                                                                                                            
                                                                                                                                                            
[+] Got OS info for 10.7.98.133 from srvinfo:                                                                                                               
        CTF            Wk Sv PrQ Unx NT SNT Samba 3.5.0                                                                                                     
        platform_id     :       500
        os version      :       4.9
        server type     :       0x809a03


 ========================================( Users on 10.7.98.133 )========================================
                                                                                                                                                            
Use of uninitialized value $users in print at ./enum4linux.pl line 972.                                                                                     
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 975.

Use of uninitialized value $users in print at ./enum4linux.pl line 986.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 988.

 ==================================( Share Enumeration on 10.7.98.133 )==================================
                                                                                                                                                            
                                                                                                                                                            
        Sharename       Type      Comment
        ---------       ----      -------
        public          Disk      
        private         Disk      
        IPC$            IPC       IPC Service (Samba 3.5.0)
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------

[+] Attempting to map shares on 10.7.98.133                                                                                                                 
                                                                                                                                                            
//10.7.98.133/public    Mapping: OK Listing: OK Writing: N/A                                                                                                
//10.7.98.133/private   Mapping: OK Listing: OK Writing: N/A
//10.7.98.133/IPC$      Mapping: OK Listing: DENIED Writing: N/A

 ============================( Password Policy Information for 10.7.98.133 )============================
                                                                                                                                                            
                                                                                                                                                            

[+] Attaching to 10.7.98.133 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] CTF
        [+] Builtin

[+] Password Info for Domain: CTF

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: 37 days 6 hours 21 minutes 
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: 37 days 6 hours 21 minutes 



[+] Retieved partial password policy with rpcclient:                                                                                                        
                                                                                                                                                            
                                                                                                                                                            
Password Complexity: Disabled                                                                                                                               
Minimum Password Length: 5


 =======================================( Groups on 10.7.98.133 )=======================================
                                                                                                                                                            
                                                                                                                                                            
[+] Getting builtin groups:                                                                                                                                 
                                                                                                                                                            
                                                                                                                                                            
[+]  Getting builtin group memberships:                                                                                                                     
                                                                                                                                                            
                                                                                                                                                            
[+]  Getting local groups:                                                                                                                                  
                                                                                                                                                            
                                                                                                                                                            
[+]  Getting local group memberships:                                                                                                                       
                                                                                                                                                            
                                                                                                                                                            
[+]  Getting domain groups:                                                                                                                                 
                                                                                                                                                            
                                                                                                                                                            
[+]  Getting domain group memberships:                                                                                                                      
                                                                                                                                                            
                                                                                                                                                            
 ===================( Users on 10.7.98.133 via RID cycling (RIDS: 500-550,1000-1050) )===================
                                                                                                                                                            
                                                                                                                                                            
[I] Found new SID:                                                                                                                                          
S-1-22-1                                                                                                                                                    

[I] Found new SID:                                                                                                                                          
S-1-5-32                                                                                                                                                    

[I] Found new SID:                                                                                                                                          
S-1-5-32                                                                                                                                                    

[I] Found new SID:                                                                                                                                          
S-1-5-32                                                                                                                                                    

[I] Found new SID:                                                                                                                                          
S-1-5-32                                                                                                                                                    

[+] Enumerating users using SID S-1-5-32 and logon username '', password ''                                                                                 
                                                                                                                                                            
S-1-5-32-544 BUILTIN\Administrators (Local Group)                                                                                                           
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''                                                                                 
                                                                                                                                                            
                                                                                                                                                            
[+] Enumerating users using SID S-1-5-21-526072586-72003097-1243282957 and logon username '', password ''                                                   
                                                                                                                                                            
S-1-5-21-526072586-72003097-1243282957-501 CTF\nobody (Local User)                                                                                          
S-1-5-21-526072586-72003097-1243282957-513 CTF\None (Domain Group)

 ================================( Getting printer info for 10.7.98.133 )================================
                                                                                                                                                            
No printers returned.                                                                                                                                       


enum4linux complete on Thu Nov 14 19:21:24 2024
```

## Connect with smbclient

```text
└─$ smbclient -N //$IP/public                
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Nov  1 14:00:33 2024
  ..                                  D        0  Fri Nov  1 14:00:33 2024

                14339080 blocks of size 1024. 6748880 blocks available
smb: \> exit
```

```text
─$ smbclient -N //$IP/private
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Nov  1 14:00:33 2024
  ..                                  D        0  Fri Nov  1 14:00:33 2024
  flag.zip                            N      228  Fri Nov  1 14:00:33 2024

                14339080 blocks of size 1024. 6748880 blocks available
smb: \> get flag.zip 
getting file \flag.zip of size 228 as flag.zip (2.2 KiloBytes/sec) (average 2.2 KiloBytes/sec)
smb: \> exit
```

## Unzip and John

```text
└─$ unzip flag.zip               
Archive:  flag.zip
[flag.zip] flag.txt password:
```

```text
└─$ zip2john flag.zip > flag.hash
ver 1.0 efh 5455 efh 7875 flag.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=46, decmplen=34, crc=A2A4353D ts=7011 cs=7011 type=0

└─$ cat flag.hash      
flag.zip/flag.txt:$pkzip$1*2*2*0*2e*22*a2a4353d*0*42*0*2e*7011*05c437caa798a49cb0a8a0ad8f4b68d9d7a46f9135c31c1458696fe451309baf948f24a36c67a378ef1461e2a7c8*$/pkzip$:flag.txt:flag.zip::flag.zip
```

```text
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt flag.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
100%smart        (flag.zip/flag.txt)     
1g 0:00:00:00 DONE (2024-11-14 19:31) 6.666g/s 15947Kp/s 15947Kc/s 15947KC/s 11271089..1-21-90
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

### `FLAG{4CC3PT3D_TH3_R1SK_TH1S_T1M3}`
