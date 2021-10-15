@echo off
title WSL Installer Script - Phoenixthrush

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo This tool will install WSL for you!
echo The PC will restart after the installation!
echo.
echo After the restart the Microsoft Store will pop up with Ubuntu, just click install!
echo After it finished installing, click on the Start button!
echo.
echo It will ask you for a UNIX name, just insert anything you want lmao!
echo Insert the password you want for 2 times and yeah it will be blank if you type!
echo Paste the phoenixsploit install command from the site that will pop up!
echo.
echo Press enter to continue or close the window to exit...

pause >nul

powershell -command "set-executionpolicy remotesigned" >nul

echo ZGVsIEM6XFVzZXJzXFB1YmxpY1xtYWluLnBzMQ0Kc3RhcnQgIiIgImh0dHBzOi8vZ2l0aHViLmNvbS9QaG9lbml4dGhydXNoL3Bob2VuaXh0aHJ1c2guZ2l0aHViLmlvI2xpbnV4LXN1cHBvcnQtZm9yLWRlYmlhbi1hbmQtYXJjaC1iYXNlZC1kaXN0cm9zIg0Kc3RhcnQgIiIgIm1zLXdpbmRvd3Mtc3RvcmU6Ly9wZHAvP1Byb2R1Y3RJZD05TjZTVldTM1JYNzEiDQpzdGFydCAvYiAiIiBjbWQgL2MgZGVsICIlfmYwIiZleGl0IC9i > start.b64
certutil -decode "start.b64" "start".bat >nul
del start.b64

copy "start.bat" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start.bat" >nul

echo Enable-WindowsOptionalFeature -FeatureName Microsoft-Windows-Subsystem-Linux -Online -NoRestart -OutVariable results > C:\Users\Public\main.ps1
echo if ($results.RestartNeeded -eq $true) { >> C:\Users\Public\main.ps1
echo   Restart-Computer -Force >> C:\Users\Public\main.ps1
echo } >> C:\Users\Public\main.ps1

powershell.exe -ExecutionPolicy Unrestricted -Command ". 'C:\Users\Public\main.ps1'"
