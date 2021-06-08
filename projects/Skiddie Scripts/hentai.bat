@echo off

echo YmFuYW5hID0gaW5wdXRib3ggKCJJbnNlcnQgeW91ciBoaWdoIChpbiBjbSkhIiwg > x.b64
echo IkhpZ2ggQ2FsY3VsYXRvciEiKQ0KaGVudGFpID0gbXNnYm94ICgiWW91ciBoaWdo >> x.b64
echo IGlzICIgJiBiYW5hbmEgJiAiIGNtISIsMCwgIlJlc3VsdCEiKQ== >> x.b64

certutil -decode "x.b64" "x.vbs"
start x.vbs
timeout 2 > nul

del x.b64
del x.vbs
exit
