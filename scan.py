import scapy.all as scapy
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scan(ips):
  answers, uans = scapy.arping(ips, verbose=0)
  res = []
  for answer in answers:
    mac = answer[1].hwsrc
    ip  = answer[1].psrc
    res.append((ip, mac))
  return res
