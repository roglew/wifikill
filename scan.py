import scapy.all as scapy
import threading
from types import *

def check(ip, port):
  pack = scapy.IP(dst=ip)/scapy.TCP(dport=port,flags="S")
  result = scapy.sr1(pack, timeout=3, verbose=0)
  if not (result is None):
    return True
  else:
    return False
  

class Scanner:
  ports = range(1,100)
  scancnt = 0
  
  def check(self, ip):
    for port in self.ports:
      if check(ip, port):
        return True
    return False
