echo wat is you ip
read ip
echo from port
read from
echo into port
read into
echo word to find
read wfind
for a in $(seq $from $into)
do
	echo $ip:$a
	 timeout 2s printf "GET / HTTP/1.0\r\n\r\n" | nc $ip $a
	 
	 
done
