def binary_to_decimal(binary_ip):
    decimal_ip = []
    for octet in binary_ip.split('.'):
        decimal_ip.append(str(int(octet, 2)))
    return '.'.join(decimal_ip)

def determine_class(decimal_ip):
    first_octet = int(decimal_ip.split('.')[0])
    if first_octet >= 0 and first_octet <= 127:
        return 'Class A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'Class B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'Class C'
    elif first_octet >= 224 and first_octet <= 239:
        return 'Class D'
    elif first_octet >= 240 and first_octet <= 255:
        return 'Class E'
    else:
        return 'Invalid IP address'

def network_id(decimal_ip):
    first_octet = int(decimal_ip.split('.')[0])
    if first_octet >= 1 and first_octet <= 126:
        return decimal_ip.split('.')[0]
    elif first_octet >= 128 and first_octet <= 191:
        return '.'.join(decimal_ip.split('.')[:2])
    elif first_octet >= 192 and first_octet <= 223:
        return '.'.join(decimal_ip.split('.')[:3])
    else:
        return 'N/A'

binary_ip = input("Enter a binary address: ")
 # Example binary IP address
decimal_ip = binary_to_decimal(binary_ip)
ip_class = determine_class(decimal_ip)
network = network_id(decimal_ip)

print("Binary IP:", binary_ip)
print("Decimal IP:", decimal_ip)
print("IP Class:", ip_class)
print("Network ID:",network)