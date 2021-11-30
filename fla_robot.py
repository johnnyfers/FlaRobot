from chatterbot import ChatBot
import json

class FlaRobot:
    def main(self): 
        robot = ChatBot('Robô do Flamengo')
        
        while True:
            question = input('Me pergunte algo sobre o Mengão: ')
            answer = robot.get_response(question)
            
            if answer.confidence > 0.6:
                print(answer.text)
            else:
                print('Não sei responder essa pergunta :( ')
                
fr = FlaRobot()

fr.main()