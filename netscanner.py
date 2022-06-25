from scapy.all import srp
from scapy.layers.l2 import ARP, Ether
import sys, argparse

ex = "Example : sudo python3 netscanner.py 192.168.228.0/24"

argparse = argparse.ArgumentParser(description="This is a basic network scanning tool.", usage ="sudo Python3 netscanner.py ip_range"+"\n\n"+ex)
argparse.add_argument("IP_range", help="Enter IP Range.")
args = argparse.parse_args()
target_network = args.IP_range

up_host=[]
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = target_network)
probe = ether/arp

result = srp(probe, timeout = 2, verbose=0)
answered = result[0]

for sent,received in answered:
    up_host.append({'ip': received.psrc, 'mac': received.hwsrc})

print("\n[+] UP HOSTS : ")
print("\tIP\t\t\tMAC")
for i in up_host:
    print('{}\t\t{}'.format(i['ip'], i['mac']))