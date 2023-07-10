import telebot
from telebot import types
import sus

r = 0
sos = 0
sas = 0
run = 0
Out_of_place=0
qwer = 0
bot = telebot.TeleBot('/5626423321/:AAFZSRn9pav/sUIKBf4alOH1vcP/MQUzA75Ds/')

@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    global r
    r+=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Launch Game")
    btn2 = types.KeyboardButton("Ask a Question")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Hi, {0.first_name} ! I am a test bot for games order without order".format(message.from_user), reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def func(message):
    global sos
    global qwer
    global run
    global Out_of_place
    qwer = [str(i) for i in message.text]
    if(message.text == "Launch Game"):
        global sas
        sas = [str(i) for i in sus.random_number_enerator()]
        sos = ''.join(sas)
        bot.send_message(message.chat.id, 'Enter a four-digit number')
        bot.send_message(message.chat.id, f'{sos}')
        run = 1

    elif(message.text == "Ask a Question"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Rules?")
        btn1 = types.KeyboardButton("Who is my developer?")
        btn2 = types.KeyboardButton("What i can?")
        btn3 = types.KeyboardButton("About the developer?")
        btn4 = types.KeyboardButton("Check out the portfolio!")
        back = types.KeyboardButton("Back to main menu")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Ask me a question", reply_markup=markup)

    elif(message.text == "Rules?"):
         bot.send_message(message.chat.id, "You must enter a four-digit number after the bot asks you to do so.")

    elif(message.text == "Check out the portfolio!"):
         bot.send_message(message.chat.id, "Here is a link to the site I created for my portfolio :\nhttp://my-partfolio-in-python-and-unity.fun/index.html")

    elif(message.text == "About the developer?"):
        bot.send_message(message.chat.id, "My developer knows such programming languages ​​as Python PhP Java C++ C# at the moment he is 14 and he loves to program various projects he also has his own portfolio if you want to see it click on view portfolio")

    elif(message.text == "Who is my developer?"):
        bot.send_message(message.chat.id, "My developer is Vladislav Tomashevskyi")
    
    elif (message.text == "What i can?"):
        bot.send_message(message.chat.id, text="Start the game in which you need to ask a question")
    
    elif (message.text == "Back to main menu"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Launch Game")
        button2 = types.KeyboardButton("Ask a Question")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="You have returned to the main menu", reply_markup=markup)

    elif run!=1:
         bot.send_message(message.chat.id,  'This command does not exist')
    elif len(qwer)>4 and run==1:
        bot.send_message(message.chat.id, 'You typed more than four digits')
    elif len(qwer)<4 and run==1:
        bot.send_message(message.chat.id, 'You have entered too few elements')
    elif qwer[0].isalpha() or qwer[1].isalpha() or qwer[2].isalpha() or qwer[3].isalpha() and run==1:     
        bot.send_message(message.chat.id, "You entered the letters, the place of the numbers")
    elif not qwer[0].isalpha() and not qwer[1].isalpha() and not qwer[2].isalpha() and not qwer[3].isalpha() and run==1:
        counter=0
        v = 0
        Out_of_place=0
        for i in range(4):
            if qwer[counter] == sas[counter]:
                v+=1
            elif qwer[counter] in sas and qwer[0]!=qwer[1] and qwer[2]!=qwer[3] and qwer[1]!=qwer[2]:
                Out_of_place+=1
            counter+=1
        if v!=4:
            bot.send_message(message.chat.id, f'''Orders : {v}''')
        if v!=4:
            bot.send_message(message.chat.id, f'''Out of place : {Out_of_place}''')
        if v!=4:
            bot.send_message(message.chat.id, f'''Without orders : {abs(4 - Out_of_place-v)}''')
        if v==4 and run==1:
            bot.send_message(message.chat.id,'Congratulations you guessed it')
            run = 0
bot.polling(none_stop=True)
