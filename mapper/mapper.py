import socket
import argparse
import webbrowser

print('\033[91m' + '''   __  __
 |  \/  | __ _ _ __  _ __   ___ _ __
 | |\/| |/ _` | '_ \| '_ \ / _ \ '__|
 | |  | | (_| | |_) | |_) |  __/ |
 |_|  |_|\__,_| .__/| .__/ \___|_|
              |_|   |_|              ''' + '\033[0m')


def port_scanner(ip, port, timeout=0.5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((ip, port))
    try:
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown / Listening port"
            print(f"Port {port} is open and service {service}")
        else:
            pass
    except socket.error:
        print("Error occurred")


def main():
    parser = argparse.ArgumentParser(description='*****Simple python Port scanner *****.')
    parser.add_argument('-i', dest='ip', required=True, help='IP address to scan')
    parser.add_argument('-s', dest='start_port', type=int,default=1, help='Starting port number (defult:1)')
    parser.add_argument('-e', dest='end_port', type=int, default=100, help='End port number (defult:100)')
    parser.add_argument('-t', dest='timeout', type=int, default=0.5, help='Timeout for socket connection in seconds (default: 0.5)')
    parser.add_argument('-b',dest='browse',type=str,default=0 ,help='If you need to browse github notes only one argument g = github -b g')
    args = parser.parse_args()
    end_port = 100
    start_port = 1
    ip_address = args.ip
    start_port = args.start_port
    end_port = args.end_port
    timeout = args.timeout
    browse = args.browse

    print(f"Scanning ports {start_port} to {end_port} on {ip_address} with timeout {timeout} seconds.\n")

    for port in range(start_port, end_port + 1):
        port_scanner(ip_address, port, timeout)
    if browse == 'g':
        webbrowser.open_new_tab('https://github.com/yaredcyber/Notes')
    else:
        pass

main()
