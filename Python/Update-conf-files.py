import re
# Function to read configuration values from a text file
def read_config(file_path):
    config = {}
    #print(type(config))
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
               
    return config

# Function to update httpd.conf file
def update_httpd_conf(httpd_conf_path, config):
    with open(httpd_conf_path, 'r') as file:
        lines = file.readlines()
    # Update the lines with new values
    with open(httpd_conf_path, 'w') as file:
        for line in lines:
            if line.startswith('Listen '):
                file.write(f'Listen {config.get("Port", "80")}\n')
            elif line.startswith('ServerName '):
                file.write(f'ServerName {config.get("ServerName", "localhost")}\n')
            elif re.match(r'^\s*ServerAlias ', line):
                file.write(f'ServerAlias {config.get("VirtualDomain", "")}\n')
            else:
                file.write(line)
# Main function
def main():
    config_file = 'config.txt'
    httpd_conf_file = 'httpd.conf'
    config = read_config(config_file)
    print(config)
    update_httpd_conf(httpd_conf_file, config)
    print(f'Updated {httpd_conf_file} with values from {config_file}')

if __name__ == '__main__':
    main()
