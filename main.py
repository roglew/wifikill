import scan

scanner = scan.Scanner()
scanner.ports = [80]

print scanner.check('10.0.0.1')
print scanner.check('10.0.0.123')

