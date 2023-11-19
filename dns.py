import socket

def main():
    input_str = input("Choose an option:\n1. Enter a domain name\n2. Enter an IP address\nEnter your choice (1 or 2): ")
    choice = int(input_str)

    if choice == 1:
        # User wants to input a domain name
        domain_name = input("Enter the domain name: ")
        print(f"Will do a DNS query on: {domain_name}")
        
        try:
            ip_address = socket.gethostbyname(domain_name)
            print(f"{domain_name} has address {ip_address}")
        except socket.error as e:
            print(f"Error getting host information: {e}")
            
    elif choice == 2:
        # User wants to input an IP address
        ip_address = input("Enter the IP address: ")

        try:
            domain_name, _, _ = socket.gethostbyaddr(ip_address)
            print(f"{ip_address} has domain name {domain_name}")
        except socket.error as e:
            print(f"Error getting host information: {e}")
            
    else:
        print("Invalid choice. Please enter 1 or 2.")

if _name_ == "_main_":
    main()
