import socket
from datetime import datetime
import sys


def main():
    # Define a target
    if len(sys.argv) == 2:
        # Translate the hostname to IPv4
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid amount of argument")

    print("Scanning Target: " + target)
    print("Scanning started at: " + str(datetime.now()))

    try:
        # Scan ports 1-65,535
        for port in range(1,65535):
            # Set the socket, s with Address Family INET which indicates IPV4 addresses
            # Use sock_stream to hold a continuous connection between two endpoints
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Returns an error indicator
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting Program...")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved!!")
        sys.exit()
    except socket.error:
        print("\n Server not responding!!")
        sys.exit()
main()