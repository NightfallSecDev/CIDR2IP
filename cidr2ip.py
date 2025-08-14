import ipaddress
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def banner():
    print(r"""
   ____ ___  ____  ____  _ ____ ___ ___ ____  
  / ___/ _ \|  _ \|  _ \| |  _ \_ _|_ _|  _ \ 
 | |  | | | | | | | |_) | | | | | | | || |_) |
 | |__| |_| | |_| |  _ <| | |_| | | | ||  __/ 
  \____\___/|____/|_| \_\_|____/___|___|_|    
             Multi-threaded CIDR to IP Tool
                Created by NightfallSecDev
------------------------------------------------
    """)

def generate_ips(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        print(f"[!] Invalid CIDR: {cidr}")
        return []

def save_to_file(ips, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w") as f:
        f.write("\n".join(ips))
    print(f"[+] Saved {len(ips)} IPs to {save_path}")

def process_cidr(cidr):
    return generate_ips(cidr.strip())

def main():
    banner()
    choice = input("Enter '1' for single CIDR or '2' for CIDR list file: ").strip()
    cidrs = []

    if choice == "1":
        cidrs.append(input("Enter CIDR (e.g., 202.44.112.0/22): ").strip())
    elif choice == "2":
        file_path = input("Enter CIDR list file path: ").strip()
        if not os.path.exists(file_path):
            print("[!] File not found.")
            return
        with open(file_path, "r") as f:
            cidrs = [line.strip() for line in f if line.strip()]
    else:
        print("[!] Invalid choice.")
        return

    save_dir = input("Enter save directory path: ").strip()
    output_file = os.path.join(save_dir, "ip_list.txt")

    all_ips = []
    max_threads = min(20, len(cidrs))

    with ThreadPoolExecutor(max_threads) as executor:
        futures = {executor.submit(process_cidr, cidr): cidr for cidr in cidrs}
        for future in as_completed(futures):
            ips = future.result()
            all_ips.extend(ips)

    save_to_file(all_ips, output_file)

if __name__ == "__main__":
    main()
