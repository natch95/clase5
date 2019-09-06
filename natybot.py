from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('natybot')
trainer = ListTrainer(bot)

for files in os.listdir('./natybot/'): 
     data=open('./natybot/'+files,'r').readlines()
trainer.train(data)
 trainer.train(data)
 trainer.train(data)

