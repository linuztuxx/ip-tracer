import requests
import subprocess
import argparse
import os
from datetime import datetime

banner = """
 ▀█▀ ▒█▀▀█ ░░ ▀▀█▀▀ ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█
 ▒█░ ▒█▄▄█ ▀▀ ░▒█░░ ▒█▄▄▀ ▒█▄▄█ ▒█░░░ ▒█▀▀▀ ▒█▄▄▀
 ▄█▄ ▒█░░░ ░░ ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█
"""

# Custom parse arguments for CLI
def parse_arguments():
    parser = argparse.ArgumentParser(description='A tool for gathering detailed information about an IP address, including its geolocation, network provider, and more.')
    parser.add_argument('-t', '--target', help='Target IP to track', required=False)
    parser.add_argument('-m', '--mine', help='Own IP address to track', action='store_true', required=False)
    parser.add_argument('-n', '--nscreen', help='Disable clear screen', action='store_true', required=False)
    return parser.parse_args()

# Function to clear the Terminal base on the operating system
def clear_screen():
     if os.name == 'nt':  # Check if the operating system is Windows
         subprocess.call('cls', shell=True)
     else:  # For unix like (Linux, Macos, BSD) use the clear command
        subprocess.call('clear', shell=True)

def ipapi_tracker(ip):
    try:
        url = f'https://ipapi.co/{ip}/json/'
        response = requests.get(url)
        return response.json()
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code}")
    except requests.RequestException as e:
        print(f'An error occurred: {e}')

def ip_api_tracker(ip):
    try:
        url = f'http://ip-api.com/json/{ip}'
        response = requests.get(url)
        return response.json()
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code}")
    except requests.RequestException as e:
        print(f'An error occurred: {e}')

def ip_info_tracker(ip):
    try:
        # Change the token if needed
        url = f'https://ipinfo.io/{ip}?token=ea638a8ed816fc'
        response = requests.get(url)
        return response.json()
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code}")
    except requests.RequestException as e:
        print(f'An error occurred: {e}')
        
def main():
        start_time = datetime.now()

        args = parse_arguments()

        if not args.nscreen:
            clear_screen()

        print(banner)
        print("==================================================")
        print("            @Linuztuxx IP TRACER v1               ")
        print("==================================================")
        print("      Github: https://github.com/linuztuxx        ")
        print("==================================================")

        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"          Current Time: {current_time}          ")
        print("==================================================")

        if args.mine:
            targets_ip = requests.get('https://api.ipify.org').text
        elif args.target:
            targets_ip = args.target
        else:
            print('Please provide a target IP address with the -t option, or use -m to check your own public IP address.\n')
            print('Example:')
            print('  python ip_tracer.py -t 192.168.1.1   # Track a specific IP address')
            print('  python ip_tracer.py -m               # Track your own IP address')
            print('\nUse -h or --help for more information.\n')
            return

        print(f"\n{'Tracing IP: ' + targets_ip:^46}\n")
        output = ipapi_tracker(targets_ip)
        print("==================================================")
        print('             Ipapi.co response:                   ')
        print("==================================================")
        for index, value in output.items():
             if index == 'latitude':
                 print(f'Google_map: https://www.google.com/maps/search/?q={output["latitude"]},{output["longitude"]}')
             print(f'{index.capitalize()}: {value}')
        print('')

        print("==================================================")
        print('             Ip-api.com response:                 ')
        print("==================================================")
        output = ip_api_tracker(targets_ip)
        for index, value in output.items():
             if index == 'lat':
                 print(f'Google_map: https://www.google.com/maps/search/?q={output["lat"]},{output["lon"]}')
             print(f'{index.capitalize()}: {value}')
        print('')

        print("==================================================")
        print('             Ipinfo.io response:                  ')
        print("==================================================")
        output = ip_info_tracker(targets_ip)
        for index, value in output.items():
            if index == 'loc':
                print(f'Google_map: https://www.google.com/maps/search/?q={output["loc"]}')
            print(f'{index.capitalize()}: {value}')
        print("\n==================================================")
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"\nScript executed in {duration:.2f} seconds.")
        print('\nIf you find this project useful, please consider giving it a star on GitHub:')
        print('https://github.com/linuztuxx/ip-tracer\n')


if __name__ == '__main__':
     main()