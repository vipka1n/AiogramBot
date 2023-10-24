#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from cfg import TOKEN, psw, whitelist
from aiogram.dispatcher.filters import Text
import os
from os import popen


# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

#сообщение при старте бота 
async def on_startup(_):
    await message.answer('Я онлайн!')


#Блокировка Handler  доступен только для White List
@dp.message_handler(lambda message: message.from_user.id not in whitelist) # message.from_user.id проверяет список White list в config
async def checker(message):
   await message.answer("Сгинь вражина!") 

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привествую  тебя комрад  я предоставлю тебе список команд если ты назовешь мне пароль:")



#Reload server Bot only windows /srv

@dp.message_handler(commands=["srv"])
async def echo(message: types.Message):
    popen("shutdown /r /t 0")
    await message.answer("Сервер Бота перезагружен! ")

#Lockscreen server Bot only windows /lock

@dp.message_handler(commands=["lock"]) 
async def echo(message: types.Message):
    popen('Rundll32.exe user32.dll,LockWorkStation')
    await message.answer("Сервер Бота залочен ")

#Restarting a remote computer /natreload
@dp.message_handler(commands=["natreload"])
async def echo(message: types.Message):
    popen("shutdown -r -f -t 0 -m 192.168.10.10")
    await message.answer("Команда выполнена GameKeeper перезагружен.")

#Ping IP remote  /pingip
@dp.message_handler(commands=['pingip'])
async def send_pong(message: types.Message):
    pong=""
    hostname='192.168.10.210'
    response = os.system('ping -n 1'+ hostname) #windows "ping -n 1", linux  "ping -c 1"
    if response == 0:
      pong=(' Игорь докладывает, Камеры клуб доступны')
    else:
      pong=(' Игорь доакладывает, Камеры клуб  недоступны')
    await message.reply(pong)




#тест ответа на сообщение
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'Привет':
       await msg.answer('И тебе привет!')

#текстовое меню
   if msg.text.lower() == psw:
       await msg.answer('Добро пожаловать Комрад')
       await msg.answer('Бот докладывает')
       await msg.answer('Сообщение')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
