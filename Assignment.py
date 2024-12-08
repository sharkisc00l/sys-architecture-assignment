from datetime import datetime
import socket
from netmiko import ConnectHandler

def Main():
    # taking the user's input for the dedsired option
    options = input("Please select an option:\n 1: Show date and time\n 2: Show local IP\n "
                    "3: Show remote home directory listing\n 4: Backup remote file\n 5: Save web page\n 6: Quit\n")

    # retrieving and formatting the date and time on the local computer
    if options == "1":
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_date)

    # retrieving the ip address
    elif options == "2":
        local_hostname = socket.gethostname()
        ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
        print("The IP address for ", local_hostname, " is ", ip_addresses)

    elif options == "3":
        linux_device = linuxConnection()

    # Establish connection
        net_connect = linux_device.enable()

    # Execute the 'ls' command
        output = linux_device.send_command("ls -l")
        print(output)

def linuxConnection():
    linux_device = ConnectHandler(
        device_type="linux",
        ip="127.0.0.1",
        username="hannah",
        password="password",
        secret="password",
        port="5679"
    )

    return linux_device

try:
    linuxConnection()
    Main()
except Exception as e:
    print("There was an error connecting to the VM")
    Main()
