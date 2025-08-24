import hashlib
import requests

API_URL = "https://api.pwnedpasswords.com/range/{}"

def check_pwned_password(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1pass[:5]   
    suffix = sha1pass[5:]

    response = requests.get(API_URL.format(prefix))
    if response.status_code != 200:
        return f"[!] Error: API request failed (HTTP {response.status_code})"

    pwned_count = 0
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            pwned_count = int(count)
            break

    if pwned_count:
        return f"[!] This password has been seen {pwned_count:,} times in breaches!"
    else:
        return "[+] This password was NOT found in the HIBP database."
