# se7en_voice
1.Download and copy custom_components/se7en_voice folder to custom_components folder in your HomeAssistant config folder<br>
2.Copy this code to file configuration.yaml<br>
```
se7en_voice:
  username: XXXX
  password: XXXX
```
3.Restart HA core<br>
4.Call this service in Developer Tools
```
service: se7en_voice.send_voice
data:
  mobile: 13888888888
  text: 您的家中检测到有人入侵，请速查看。
```
