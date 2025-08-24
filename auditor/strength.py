from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)

    # Score mapping
    score_map = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    # Crack times (human-readable)
    crack_times = result["crack_times_display"]

    output = []
    output.append(f"[+] Password Strength: {score_map[result['score']]} ({result['score']}/4)")
    output.append("[+] Estimated Crack Times:")
    output.append(f"    - Online throttled guess (100/h): {crack_times['online_throttling_100_per_hour']}")
    output.append(f"    - Online unthrottled guess (10/s): {crack_times['online_no_throttling_10_per_second']}")
    output.append(f"    - Offline slow hash (1e4/s): {crack_times['offline_slow_hashing_1e4_per_second']}")
    output.append(f"    - Offline fast hash (1e10/s): {crack_times['offline_fast_hashing_1e10_per_second']}")

    # Feedback from zxcvbn
    if result["feedback"]["warning"]:
        output.append(f"[!] Warning: {result['feedback']['warning']}")
    if result["feedback"]["suggestions"]:
        output.append("[+] Suggestions:")
        for s in result["feedback"]["suggestions"]:
            output.append(f"    - {s}")

    return "\n".join(output)
