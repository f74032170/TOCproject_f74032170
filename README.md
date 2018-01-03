#TOCproject_F74032170
Code for TOC Project

##Setup
* Python3

###Install Dependency
```sh
pip3 install -r requirements.txt
```
### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

###API_TOKEN for this bot
the bot name in telegram is "Ask_Ko_Wen_Je"
the bot username in telegram is "Ask_Ko_Wen_Je_bot"
You will find it at "t.me/Ask_Ko_Wen_Je_bot" in telegram. 

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app1.py
```
## Finite State Machine
![fsm](./img/show-fsm.png)


