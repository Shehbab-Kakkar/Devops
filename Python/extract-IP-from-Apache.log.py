# Python script to extract IP addresses with 403 errors from Apache log
import re
def find_403_ips(log_file):
    # Regular expression to match lines with 403 status code
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[.*?\] ".*?" 403 .*')
    # Set to store unique IP addresses with 403 errors
    ips_with_403 = set()
    # Read the log file
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                # Extract the IP address and add it to the set
                ip_address = match.group(1)
                ips_with_403.add(ip_address)
    
    return ips_with_403

if __name__ == "__main__":
    log_file_path = "httpd.log"  # Replace with your actual log file path
    # Find IPs with 403 errors
    ips = find_403_ips(log_file_path)
    # Print the IP addresses
    if ips:
        print("IP addresses with 403 errors:")
        for ip in ips:
            print(ip)
    else:
        print("No 403 errors found.")


"""
Output
IP addresses with 403 errors:
10.0.0.15
"""
