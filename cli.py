import argparse
import re
from colorama import Fore, Style
from auditor.hash_utils import detect_hash_type
from auditor.strength import check_password_strength
from auditor.hibp_check import check_pwned_password

BANNER = f"""{Fore.RED}
██████╗ ██████╗██████╗ ████████╗███████╗███╗   ███╗██████╗ ██╗     ███████╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝
██████╔╝█████╗  ██║  ██║   ██║   █████╗  ██╔████╔██║██████╔╝██║     █████╗  
██╔══██╗██╔══╝  ██║  ██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  
██║  ██║███████╗██████╔╝   ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗
╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝                                                                         
{Style.RESET_ALL}"""


def looks_like_hash(value):
    hash_lengths = {32, 40, 56, 64, 96, 128}  
    return len(value) in hash_lengths and re.fullmatch(r"[0-9a-fA-F]+", value) is not None


def main():
    parser = argparse.ArgumentParser(
        prog="RedTemple",
        description=f"{BANNER}\n{Fore.YELLOW}Password & Hash Auditor with Breach Checking{Style.RESET_ALL}",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("input_value", nargs="?", help="Password or hash to audit")
    parser.add_argument("-p", help="Explicitly specify a plain text password to audit")
    parser.add_argument("-H", help="Explicitly specify a hashed password to audit")
    args = parser.parse_args()
    
    if args.p:
        print(Fore.GREEN + f"[+] Detected plain password: {args.p}" + Style.RESET_ALL)
        print(Fore.YELLOW + check_password_strength(args.p) + Style.RESET_ALL)
        print(Fore.RED + check_pwned_password(args.p) + Style.RESET_ALL)
        return

    if args.H:
        print(Fore.BLUE + f"[+] Detected hash: {args.H}" + Style.RESET_ALL)
        print(Fore.YELLOW + detect_hash_type(args.H) + Style.RESET_ALL)
        return

    if args.input_value:
        if looks_like_hash(args.input_value):
            print(Fore.BLUE + f"[+] Auto-detected hash: {args.input_value}" + Style.RESET_ALL)
            print(Fore.YELLOW + detect_hash_type(args.input_value) + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"[+] Auto-detected plain password: {args.input_value}" + Style.RESET_ALL)
            print(Fore.YELLOW + check_password_strength(args.input_value) + Style.RESET_ALL)
            print(Fore.RED + check_pwned_password(args.input_value) + Style.RESET_ALL)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
