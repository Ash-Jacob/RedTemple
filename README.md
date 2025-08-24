# RedTemple

RedTemple is a command-line tool for auditing passwords and password hashes. It provides:

- Hash type detection  
- Password strength scoring with estimated crack times  
- Breach checking using the HaveIBeenPwned (HIBP) API  

This tool is built with Python and is a personal student project

---

## Features

1. **Hash Detection**  
   Detects the type of a given hash and highlights common algorithms.

2. **Password Strength Check**  
   Uses `zxcvbn` to provide a human-readable strength score (Very Weak → Very Strong) and estimated time to crack.

3. **Breach Check**  
   Checks if a password has been exposed in known breaches via the HIBP API, safely using SHA1 k-anonymity.

---

## Installation

1. Clone the repository:

2. Create a Python virtual environment (recommended):

	`python -m venv venv`


3. Activate the virtual environment:

- Windows:

	`venv\Scripts\activate`


Install dependencies:

	pip install -r requirements.txt


## Usage

RedTemple can be run directly from the command line

	\RedTemple>RedTemple.exe -h 
	
	
## Examples

1. Audit a password:

	`RedTemple.exe -p "My$ecret123"`
	
	`Output:
	[+] Detected plain password: My$ecret123
	[+] Password Strength: Fair (2/4)
	[+] Estimated Crack Times:
		- Online throttled guess (100/h): 4 years
		- Online unthrottled guess (10/s): 4 days
		- Offline slow hash (1e4/s): 6 minutes
		- Offline fast hash (1e10/s): less than a second
	[+] Suggestions:
		- Add another word or two. Uncommon words are better.
		- Capitalization doesn't help very much.
		- Predictable substitutions like '@' instead of 'a' don't help very much.
	[!] This password has been seen 2 times in breaches!`
	
2. Audit a Hash:
	
	`RedTemple.exe -H 5f4dcc3b5aa765d61d8327deb882cf99`
	
	Output:
	`[+] Detected hash: 5f4dcc3b5aa765d61d8327deb882cf99
	[+] Possible algorithms:
		* MD4
		* MD5
		* NTLM
		- BigCrypt
		- Cisco Type 7
		- Domain Cached Credentials
		- Domain Cached Credentials 2
		- Double MD5
		- Haval-128
		- LM
		- Lotus Notes/Domino 5
		- MD2
		- PrestaShop
		- RAdmin v2.x
		- RIPEMD-128
		- Skype
		- Snefru-128
		- Tiger-128
		- ZipMonster`
		
3. Auto-detect input type (password or hash):

	`RedTemple.exe password123!`
	
	`Output:
	[+] Auto-detected plain password: password123!
	[+] Password Strength: Weak (1/4)
	[+] Estimated Crack Times:
		- Online throttled guess (100/h): 10 days
		- Online unthrottled guess (10/s): 38 minutes
		- Offline slow hash (1e4/s): 2 seconds
		- Offline fast hash (1e10/s): less than a second
	[!] Warning: This is similar to a commonly used password.
	[+] Suggestions:
		- Add another word or two. Uncommon words are better.
	[!] This password has been seen 18,933 times in breaches!`
	
	
## Notes

Make sure you are connected to the internet for the breach check to work.

Your password is never sent in full to the HIBP API — only a partial SHA1 hash is used (privacy-safe k-anonymity).

