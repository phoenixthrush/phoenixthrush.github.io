WScript.Sleep(5000)
set WshShell = wscript.createobject("WScript.shell")
WshShell.run """C:\Windows\Temp\main.bat"" ", 1, true