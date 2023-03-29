from telebot import TeleBot, types

token = "5891560470:AAHRZjdIi1xefovR0vMTFctuAIF8eP4vksI"

mybot = TeleBot(token)

@mybot.message_handler(commands=['start'])
def boshlash(message):
	buttons = types.ReplyKeyboardMarkup(True)
	buttons.row("dushanba","seshanba","chorshanba")
	buttons.row("payshanba","juma","shanba")
	mybot.send_message(message.chat.id,"meni botimga hush kelibsiz pastdan kunni tanlang👇",reply_markup=buttons)
	
@mybot.message_handler(content_types=['photo'])
def rasm(message):
	mybot.delete_message(message.chat.id, message.id)

# @mybot.message_handler(func=lambda message:"salom")
# def habar(message):
# 	mybot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text="menga_yozma")
	

@mybot.message_handler(content_types=['text'])
def habar(message):
	buttons = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton(text="Bioinformatika",callback_data="bio")
	b2 = types.InlineKeyboardButton(text="Dastur tekshirish",callback_data="dastur")
	b3 = types.InlineKeyboardButton(text="GeoMa'lumotlar",callback_data="geo")
	buttons.add(b1)
	buttons.add(b2)
	buttons.add(b3)
	if message.text == "dushanba":
		mybot.send_message(message.chat.id,"dushanbadagi darslar👇",reply_markup=buttons)


@mybot.message_handler(content_types=['sticker','video','text'])
def fayl(message):
	mybot.copy_message(chat_id=message.chat.id,from_chat_id=message.chat.id,message_id=message.id)


@mybot.callback_query_handler(func=lambda call:True)
def tugma_bosildi(call):
	mybot.delete_message(call.message.chat.id,call.message.id)
	if call.data == "bio":
		mybot.send_message(call.message.chat.id,"114-xona.\n ass: Baltayev.R")
	elif call.data == "dastur":
		file = open("photos/dastur.JPG","rb")
		mybot.send_photo(call.message.chat.id,file)

mybot.polling()

# @mybot.message_handler(funk=lambda message:True)


