from hashid import HashID

POPULAR_HASHES = {
    "MD5", "SHA-1", "SHA-256", "NTLM", "MD4", "SHA-512",
    "bcrypt", "PBKDF2", "scrypt", "Argon2"
}

def detect_hash_type(hash_value):
    hashid = HashID()
    results = hashid.identifyHash(hash_value)

    if not results:
        return "[!] No matching hash type found."

    filtered = [alg for alg in results if "(" not in alg[0] and "$" not in alg[0]]

    popular = [alg for alg in filtered if alg[0] in POPULAR_HASHES]
    others = [alg for alg in filtered if alg[0] not in POPULAR_HASHES]

    popular.sort(key=lambda x: x[0])
    others.sort(key=lambda x: x[0])

    output_lines = ["[+] Possible algorithms:"]
    for alg in popular:
        output_lines.append(f"    * {alg[0]}")
    for alg in others:
        output_lines.append(f"    - {alg[0]}")

    return "\n".join(output_lines)
