from telebot import TeleBot, types

token1 = "5891560470:AAHRZjdIi1xefovR0vMTFctuAIF8eP4vksI"
token2 = "6189904407:AAF0hGrwb9uWrozvr-dh0VS2o7L6HRBiUxU"
mybot = TeleBot(token1)

@mybot.message_handler(commands=['start'])
def boshlash(message):
	buttons = types.ReplyKeyboardMarkup(True)
	buttons.row("dushanba","seshanba","chorshanba")
	buttons.row("payshanba","juma","shanba")
	mybot.send_message(message.chat.id,"meni botimga hush kelibsiz pastdan kunni tanlang👇",reply_markup=buttons)

@mybot.message_handler(func=lambda message:message.text=="salom")
def rasm(message):
	mybot.delete_message(message.chat.id, message.id)

@mybot.message_handler(func=lambda message:message.text=="hayr")
def habar(message):
	matn = mybot.send_message(chat_id=message.chat.id,text="hayr")
	mybot.edit_message_text(text="menga yozma",chat_id=message.chat.id,message_id=matn.id)

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


@mybot.message_handler(content_types=['sticker','video'])
def fayl(message):
	mybot.copy_message(chat_id=message.chat.id,from_chat_id=message.chat.id,message_id=message.id)


@mybot.callback_query_handler(func=lambda call:True)
def tugma_bosildi(call):
	mybot.delete_message(call.message.chat.id,call.message.id)
	if call.data == "bio":
		mybot.send_message(call.message.chat.id,"114-xona.\n ass: Baltayev.R")
	elif call.data == "dastur":
		file = open("/dastur.JPG","rb")
		mybot.send_photo(call.message.chat.id,file)

@mybot.message_handler(func=lambda message:message.text="seshanba")
def send_locatsiya_phone(message):
	tugmalar = types.ReplyKeyboardMarkup(True)


mybot.polling()

# @mybot.message_handler(funk=lambda message:True)


