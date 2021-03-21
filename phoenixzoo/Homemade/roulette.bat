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
echo destroyed!

del %temp%\rick.mp4 > nul
bitsadmin /transfer mydownloadjob /download /priority foreground "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/assets/rick.zip" "%temp%\rick.zip" >nul
powershell -c "Expand-Archive %temp%\rick.zip %temp%"

del %temp%\rick.zip
start "" "%temp%\rick.mp4"
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