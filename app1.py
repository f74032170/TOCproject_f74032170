import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm1 import TocMachine


API_TOKEN = '483259801:AAE94xLUWG_kG41zZkXDBLHcQyfTXoOOjjA'
WEBHOOK_URL = 'https://fe3967fd.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'ko_wen_je',
        'nationality',
        'mayer',
        'doctor',
        'political'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'ko_wen_je',
            'dest': 'nationality',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'ko_wen_je',
            'dest': 'mayer',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'ko_wen_je',
            'dest': 'doctor',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'ko_wen_je',
            'dest': 'political',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'go_back',
            'source': [
                'nationality',
                'mayer',
                'doctor',
                'political'
            ],
            'dest': 'ko_wen_je'
        }
    ],
    initial='ko_wen_je',
    auto_transitions=False,
    show_conditions=False,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
