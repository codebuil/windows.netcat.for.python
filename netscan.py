
import subprocess
import time

def ping(host):
    result = subprocess.run(['ping', host,'-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outputs = result.stdout.decode()
    
    if outputs.find("unreachable")<0:
        print(host)
            
n = 0
i=127
separetor="-----------------------------------------------------------"
host_to_ping = "192.168.1."
host_to_ping2 = host_to_ping 
print("\033c\033[47;34m")
for n in range(1,i):
    host_to_ping2 = host_to_ping + str(n)
    ping(host_to_ping2)