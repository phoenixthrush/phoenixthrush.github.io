@echo off

echo RGltIG1heCxtaW4scmFuZA0KbWF4PTI1DQptaW49MA0KUmFuZG9taXplDQpyYW5k > x.b64
echo ID0gSW50KChtYXgtbWluKzEpKlJuZCttaW4pDQoNCmhlbnRhaSA9IG1zZ2JveCAo >> x.b64
echo IllvdXIgZGljayBpcyAiICYgcmFuZCAmICIgY20gbGFyZ2UhIiwwLCAiRGljayBN >> x.b64
echo ZXRlciIp >> x.b64

certutil -decode "x.b64" "x.vbs"
start x.vbs
timeout 1 > nul

del x.b64
del x.vbs
exit