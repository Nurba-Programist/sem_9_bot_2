import telebot, wikipedia, re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

bot = telebot.TeleBot('5677781569:AAHAnEYU0MJuaX6ITmwtw1rz1TMeKEJATEg')

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Телеграмм Википедия, что хотите узнать?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)

def log(message):
    file = open('db.csv','a')
    file.write(message.chat.id, getwiki(message.text))
    file.close()