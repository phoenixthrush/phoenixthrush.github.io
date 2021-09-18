@echo off

echo QGVjaG8gb2ZmIA0KdGl0bGUgUnVzc2lhbiBSb3VsZXR0ZSBieSBQaG9lbml4dGhy >> x.b64
echo dXNoDQpjb2xvciBhDQoNCmlmIG5vdCAiJTEiPT0iYW1fYWRtaW4iIChwb3dlcnNo >> x.b64
echo ZWxsIHN0YXJ0IC12ZXJiIHJ1bmFzICclMCcgYW1fYWRtaW4gJiBleGl0IC9iKQ0K >> x.b64
echo DQpzZXQgL2EgcmFuZD0lcmFuZG9tJSAlJSAyICsgMQ0KDQo6bWVudWUNCmVjaG8g >> x.b64
echo WW91IGhhdmUgYSA1MCBwZXJjZW50IGNoYW5jZSB0byBzdXJ2aXZlIQ0KZWNobyBJ >> x.b64
echo ZiB5b3UgZmFpbCwgYWxsIHlvdXIgZGF0YSB3aWxsIGJlIGxvc3QhDQplY2hvLg0K >> x.b64
echo c2V0IC9wIGFzdz0iRG8geW91IHJlYWxseSB3YW50IHRvIGNvbnRpbnVlPyBbeS9u >> x.b64
echo XSAiDQoNCmlmICVhc3clPT15IChnb3RvIGNvbnRpbnVlKQ0KaWYgJWFzdyU9PW4g >> x.b64
echo KGdvdG8gZXhpdCkgZWxzZSAoZ290byBtZW51ZSkNCmV4aXQNCg0KOmNvbnRpbnVl >> x.b64
echo DQppZiAlcmFuZCU9PTEgKGdvdG8gZnVja2VkKQ0KaWYgJXJhbmQlPT0yIChnb3Rv >> x.b64
echo IGx1Y2spDQpleGl0DQoNCjpmdWNrZWQNCmNscw0KZWNobyBkZXN0cm95ZWQhDQoN >> x.b64
echo CmRlbCAldGVtcCVccmljay5tcDQgPiBudWwNCmJpdHNhZG1pbiAvdHJhbnNmZXIg >> x.b64
echo bXlkb3dubG9hZGpvYiAvZG93bmxvYWQgL3ByaW9yaXR5IGZvcmVncm91bmQgImh0 >> x.b64
echo dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9QaG9lbml4dGhydXNoL3Bo >> x.b64
echo b2VuaXh0aHJ1c2guZ2l0aHViLmlvL21hc3Rlci9zaXRlcy9hc3NldHMvcmljay56 >> x.b64
echo aXAiICIldGVtcCVccmljay56aXAiID5udWwNCnBvd2Vyc2hlbGwgLWMgIkV4cGFu >> x.b64
echo ZC1BcmNoaXZlICV0ZW1wJVxyaWNrLnppcCAldGVtcCUiDQoNCmRlbCAldGVtcCVc >> x.b64
echo cmljay56aXANCnN0YXJ0ICIiICIldGVtcCVccmljay5tcDQiDQpleGl0DQoNCjps >> x.b64
echo dWNrDQpjbHMNCmVjaG8geW91IHN1cnZpdmVkIQ0KcGF1c2UgPm51bA0KZXhpdA0K >> x.b64
echo DQo6ZXhpdA0KY2xzDQplY2hvIE1heWJlIHNlZSB5YSBsYXRlciENCnBhdXNlID5u >> x.b64
echo dWwNCmV4aXQ= >> x.b64

certutil -decode "x.b64" "x.bat"
del x.b64
start x.bat
