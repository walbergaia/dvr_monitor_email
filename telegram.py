import io
import telebot

TOKEN = '6235424979:AAEHcjRYvIsGvTTOLtAHsb183Z3hedSlbcs'
bot = telebot.TeleBot(TOKEN)
chat_id='-983359425'

def send_dvrimage(image_buffer):
    # Cria uma instância da classe InputFile a partir do objeto de bytes
    #image_file = telebot.types.InputFile(io.BytesIO(image_buffer), filename='image.jpg')
    # Envia a imagem para o chat_id especificado
    bot.send_photo(chat_id,image_buffer)
