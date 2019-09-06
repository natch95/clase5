from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def chatraining():
     bot=ChatBot('natybot')
     trainer = ListTrainer(bot)

     for files in os.listdir('./natybot/'): 
          data=open('./natybot/'+files,'r').readlines()
          trainer.train(data)
          trainer.train(data)
          trainer.train(data)

#------------------------------------------------------------------------------------------------------
#chat feature
     while True:
          message=input('\t\t\tYou: ')
          if message.strip()!='Bye' or 'bye':
               reply=bot.get_response(message)
               print('natybot:',reply)
          if message.strip()=='Bye':
               print('natybot: Bye')
               break


chatraining()