from netmiko import ConnectHandler
import Assignment

def homeDirectory():
    linux_device = Assignment.linuxConnection()


    # Establish connection
    net_connect = linux_device.enable()

    # Execute the 'ls' command
    output = linux_device.send_command("ls -l")
    print(output)

    # Close the connection

homeDirectory()

