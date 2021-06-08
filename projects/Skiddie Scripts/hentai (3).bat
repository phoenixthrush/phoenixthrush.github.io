@echo off

echo RGltIG1heCxtaW4scmFuZA0KbWF4PTEwMA0KbWluPTANClJhbmRvbWl6ZQ0KcmFu > x.b64
echo ZCA9IEludCgobWF4LW1pbisxKSpSbmQrbWluKQ0KDQpoZW50YWkgPSBtc2dib3gg >> x.b64
echo KCJZb3VyICIgJiByYW5kICYgIiUgR2F5ISIsMCwgIkdheSBNZXRlciIp >> x.b64

certutil -decode "x.b64" "x.vbs"
start x.vbs
timeout 1 > nul

del x.b64
del x.vbs
exit
