
import subprocess
import time

def ping(host):
    
    result = subprocess.call('ping '+host+' -c '+'1',shell=True) 
n = 0
i=127
separetor="-----------------------------------------------------------"
host_to_ping = "192.168.1."
host_to_ping2 = host_to_ping 
print("\033c\033[47;34m")
if __name__ == "__main__":
    for n in range(1,i):
        host_to_ping2 = host_to_ping + str(n)
        print(separetor)
        ping(host_to_ping2)
