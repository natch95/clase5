

while True:
    continuar = input('Desea agregar otra: \n 1- Agregar \n 2 - Terminal ')
        if continuar == '1':
            pregunta = input ('Pregunta ')
            respuesta = input ('Respuesta ')

            file.write('- - ' + pregunta + os.linesep)
            file.write('  - ' + respuesta + os.linesep)

        if continuar == '2':
            file.close()
            break


namechatbot = proyecto+'.py'
file = open(namechatbot, "w")
file.write("from chatterbot import ChatBot\nfrom chatterbot.trainers import ListTrainer\nimport os\nbot=ChatBot('"+proyecto+"')\ntrainer = ListTrainer(bot)\n" + os.linesep)
file.write("for files in os.listdir('./"+proyecto+"/'): \n     data=open('./"+proyecto+"/'+files,'r').readlines()\ntrainer.train(data)\n trainer.train(data)\n trainer.train(data)\n"+os.linesep)
file.close()    