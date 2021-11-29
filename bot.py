import pyowm  
import telebot 
import os 
import time

owm = pyowm.OWM('9b2a4d9e69f0195329a042f0de762022', language='ru')

bot = telebot.TeleBot('2128425415:AAGdhQv6dXpNAoIpQhBpqzL4Zq-3LklLv0U')

@bot.message_handler(content_types=['text'])
def send_message(message):
    

    if message.text.lower() == "/start" or message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    else:
       
        try:
          
            observation = owm.weather_at_place(message.text)
            weather = observation.get_weather()
            temp = weather.get_temperature("celsius")["temp"]  
            temp = round(temp)
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), temp, "C", weather.get_detailed_status())

           
            answer = "В городе " + message.text.title() + " сейчас " + weather.get_detailed_status() + "." + "\n"
            answer += "Температура около: " + str(temp) + " С" + "\n\n"
            if temp < -10:
                answer += "Невероятно холодно, одевайся как капуста!"
            elif temp < 10:
                answer += "Холодно, одевайся теплее."
            elif temp > 25:
                answer += "Жарень."
            else:
                answer += "На улице вроде норм!!!"
        except Exception:
            answer = "Не найден город, попробуйте ввести название снова.\n"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), 'Error')

        bot.send_message(message.chat.id, answer)  

bot.polling(none_stop=True)
