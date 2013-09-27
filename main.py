import scan
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

print('DO WORK')
print scan.scan('10.0.0.*')

