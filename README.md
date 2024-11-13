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
  - `Result: FLAG{3V4LU4T3D_5UCC35SFU11Y}`

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
- `FLAG{0nly_s1gned_c00kies_4_m3!}`
