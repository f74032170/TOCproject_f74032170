from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'what is ko_wen_jen nationality'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'does ko_wen_jen a mayer'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'was ko_wen_jen a doctor'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'what is ko_wen_jen political party'

    def on_enter_nationality(self, update):
        update.message.reply_text("Republic of China")
        self.go_back(update)

    def on_exit_nationality(self, update):
        print('Leaving nationality')

    def on_enter_mayer(self, update):
        update.message.reply_text("Yes , he is mayer of Taipei")
        self.go_back(update)

    def on_exit_mayer(self, update):
        print('Leaving mayer')

    def on_enter_doctor(self, update):
        update.message.reply_text("Yes , he was a surgeon of National Taiwan University Hospital")
        self.go_back(update)

    def on_exit_doctor(self, update):
        print('Leaving doctor')

    def on_enter_political(self, update):
        update.message.reply_text("He remain Independent")
        self.go_back(update)

    def on_exit_political(self, update):
        print('Leaving political')
