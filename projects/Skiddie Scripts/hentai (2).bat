@echo off

echo YmFuYW5hID0gaW5wdXRib3ggKCJJbnNlcnQgeW91ciBhZ2UhIiwgIkFnZSBDYWxj > x.b64
echo dWxhdG9yISIpDQpoZW50YWkgPSBtc2dib3ggKCJZb3VyIGFnZSBpcyAiICYgYmFu >> x.b64
echo YW5hICYgIiEiLDAsICJSZXN1bHQhIik= >> x.b64

certutil -decode "x.b64" "x.vbs"
start x.vbs
timeout 1 > nul

del x.b64
del x.vbs
exit
