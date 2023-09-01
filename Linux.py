
import os


def ping(host):
    
    result = os.popen('ping '+host+' -c '+'1')
    outputs=result.read()
    if outputs.find("1 received")>0:
        print(separetor)
        print (host) 
n = 0
i=127
separetor="-----------------------------------------------------------"
host_to_ping = "192.168.1."
host_to_ping2 = host_to_ping 
print("\033c\033[47;34m")
if __name__ == "__main__":
    for n in range(1,i):
        host_to_ping2 = host_to_ping + str(n)
        ping(host_to_ping2)
