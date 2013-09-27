import scapy.all as scapy
import threading

def check(ip, port, lst=[]):
  pack = scapy.IP(dst=ip)/scapy.TCP(dport=port,flags="S")
  result = scapy.sr1(pack, timeout=3, verbose=0)
  if not (result is None):
    # If we get a response, add it to the list
    lst.append(result.src)
    return True
  else:
    return False

class Scanner:
  ports = range(1,100)
  scancnt = 0
  results = []
  
  def check(self, ip, lst=[]):
    for port in self.ports:
      if check(ip, port, lst=lst):
        return True
    return False

  def checklst(self, ip, lst):
    # Same as check, but needs a lst
    print "Checking %s" % ip
    self.check(ip, lst=lst)

  def scan(self, ips):
    ret = []
    threads = []
    for ip in ips:
      # Create a thread for each check and add it to the list
      thread = threading.Thread(target=self.checklst, args=(ip, ret))
      thread.daemon = True
      thread.start()
      threads.append(thread)

    # Wait for all the threads to end
    for thread in threads:
      while thread.is_alive():
        pass
    return ret
