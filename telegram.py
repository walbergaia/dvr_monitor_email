import io
import telebot
import json

with open('configtelegram.json') as f:
    config = json.load(f)

TOKEN = config['token']
chat_id = config['chat_id']

bot = telebot.TeleBot(TOKEN)

def send_dvrimage(image_buffer):
    # Cria uma instância da classe InputFile a partir do objeto de bytes
    #image_file = telebot.types.InputFile(io.BytesIO(image_buffer), filename='image.jpg')
    # Envia a imagem para o chat_id especificado
    bot.send_photo(chat_id, image_buffer)