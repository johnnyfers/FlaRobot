from os import close
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSIONS_PATH = [
    'config/welcome.json',
    'config/base_info.json',
    'config/info.json'
]


class Trainning:
    def __init__(self):
        self.robot = ChatBot('Robô do Flamengo')
        self.trainer = ListTrainer(self.robot)

    def main(self):
        conversations = self.load_conversations()
        
        if conversations:
            self.train(self, conversations)

    @staticmethod
    def load_conversations():
        conversations = []

        for config_file in CONVERSIONS_PATH:
            with open(config_file, 'r') as file:
                info = json.load(file)
                conversations.append(info['conversations'])

                file.close()

        return conversations

    @staticmethod
    def train(self, conversations):
        for conversation in conversations:
            for messages_answers in conversation:
                messages = messages_answers['messages']
                answers = messages_answers['answers']
                
                print('robot training.. : ', messages, ' /// ',answers)
                for message in messages:
                    self.trainer.train([message, answers])
                    
t = Trainning()

t.main()