#!/usr/bin/python3

def replace_parameters_in_ks_cfg(file_path="vm-ks.cfg", output_file_path="generated-ks.cfg"):

    with open(file_path, "r") as file:
        content = file.read()

    netmask = input("Enter the netmask value: ")
    ipaddr = input("Enter the IP address value: ")
    gateway = input("Enter the gateway value: ")
    nameserver = input("Enter the nameserver value: ")
    hostname = input("Enter the hostname value (FQDN): ")

    content = content.replace("@ipaddr", ipaddr)
    content = content.replace("@netmask", netmask)
    content = content.replace("@gateway", gateway)
    content = content.replace("@nameserver", nameserver)
    content = content.replace("@hostname", hostname)

    with open(output_file_path, "w") as file:
        file.write(content)
        file.write("\n\n# This file generated by a Python script. Don't edit directly.")
    
    print(f"Updated content written to {output_file_path}")

replace_parameters_in_ks_cfg()
