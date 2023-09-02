@echo off
echo give me you ip
set /P ip=give me you ip:
echo from port
set /P from=from port:
echo into port
set /P into=into port:
for /l %%n in (%from%,1,%into%) do curl http://%ip%:%%n%
@echo on