CHCP 65001
cmd /c echo %date% %time% >> %userprofile%\Desktop\phoenix.txt"
powershell -command "netsh wlan show profile * key=clear" >> %userprofile%\Desktop\phoenix.txt
powershell -command "wmic path softwarelicensingservice get OA3xOriginalProductKey" >> %userprofile%\Desktop\phoenix.txt

REM Copyright Phoenixthrush
