# importing required libraries
from datetime import datetime
import socket
from netmiko import ConnectHandler
import requests

# created a function for modularity
def Main():
    # taking the user's input for the desired option
    options = input("Please select an option:\n 1: Show date and time\n 2: Show local IP\n "
                    "3: Show remote home directory listing\n 4: Backup remote file\n 5: Save web page\n Q: Quit\n").upper()

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

    # establish connection
        net_connect = linux_device.enable()

    # execute the 'ls' command
        print(linux_device.send_command("ls -l"))

    elif options == "4":
        linux_device = linuxConnection()
        net_connect = linux_device.enable()

        filePath = input("Please input the full path to the file needing to be backed up: ")
        # creating the backup
        copy_command = f"cp {filePath} {filePath}.old"
        linux_device.send_command(copy_command)
        # letting user know program has run
        print("Backup connected successfully")

    elif options == "5":
        url = input("Please enter the full URL of the web page to back up: ")
        filename = input("What would you like the file to be called: ")

        response = requests.get(url)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print("Web page saved successfully")

    elif options == "Q":
        exit()

    else:
        print("Please choose one of the options provided")

def linuxConnection():
    linux_device = ConnectHandler(
        # connecting to remote host
        device_type="linux",
        ip="127.0.0.1",
        username="hannah",
        password="password",
        secret="password",
        port="5679"
    )

    return linux_device
# error handling
try:
    linuxConnection()
    Main()
except Exception as e:
    print("There was an error connecting to the VM")
    Main()
