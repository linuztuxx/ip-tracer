# IP Tracer

IP Tracer is a command-line tool for gathering detailed information about an IP address, including its geolocation, network provider, and physical location. It leverages multiple APIs to provide comprehensive information about the target IP address.

## Features

- Track specific IP addresses and retrieve detailed information, including geolocation and ISP details.
- Retrieve detailed information about your own public IP address.
- Utilize multiple APIs to gather comprehensive IP data.
- Option to clear or maintain the terminal screen before displaying the results for better readability.

## Prerequisites

- Python 3.6 or higher.
- `requests` library (Install via `pip install requests`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/linuztuxx/ip-tracer.git
    cd ip-tracer
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

4. Install the required Python packages:

    ```bash
    pip install requests
    ```


## Options

- -t, --target: Target IP address to track.
- -m, --mine: Track your own public IP address.
- -n, --nscreen: Disable clearing the screen before displaying the results for better readability.
- -h, --help: Display the help message and exit.

## Examples

1. Track a specific IP address:
   ```bash
   python iptracer.py -t <target_ip>
   ```
   
2. Track your own public IP address:
   ```bash
   python iptracer.py -m
   ```

## Output

The script provides information from three different APIs: Ipapi.co, Ip-api.com, and Ipinfo.io. It includes details such as the geolocation, ISP, organization, and more. Additionally, it provides Google Maps links for the geolocation data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.