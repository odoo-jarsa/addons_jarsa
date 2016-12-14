# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = '308245102:AAHojngXIJ9yTolBgVi8rycd-SFsUjJKs4o'
tor = telebot.TeleBot(TOKEN)

@tor.message_handler(commands=['start'])
def comando_ayuda(mensaje):
    chat_id = mensaje.chat.id
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Checar mis puntos')
    itembtn2 = types.KeyboardButton('Realizar encuesta')
    itembtn3 = types.KeyboardButton('Solicitar factura')
    itembtn4 = types.KeyboardButton('Notificar irregularidad')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3, itembtn4)
    tor.send_message(
        chat_id,
        'Hola! ¡Bienvenido a b2c messenger! Me llamo b-2 '
        'y sere tu bot asistente¿Que deseeas realizar?',
    reply_markup=markup)

@tor.message_handler(commands=['rfc'])
def comando_rfc(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    rfc = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Guardando " + rfc + ", guardare tu rfc como ")

@tor.message_handler(commands=['razon_social'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " , un gusto atenderte.")

@tor.message_handler(commands=['Calle'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    calle = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + calle + " sera tu calle al momento de facturar.")

@tor.message_handler(commands=['numero_int'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    numero_int = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + numero_int + " , sera tu numero interior.")

@tor.message_handler(commands=['numero_ext'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    numero_ext = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + numero_ext + " , sera tu numero exterior.")

@tor.message_handler(commands=['colonia'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    colonia = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + colonia + " , sera tu colonia.")

@tor.message_handler(commands=['ciudad'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    ciudad = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + ciudad + "  sera tu ciudad.")

@tor.message_handler(commands=['colonia'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " sera tu colonia.")

@tor.message_handler(commands=['estado'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " sera tu estado")

@tor.message_handler(commands=['localidad'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " sera tu localidad")

@tor.message_handler(commands=['codigo_postal'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " sera tu codigo postal.")

@tor.message_handler(commands=['correo_electronico'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " sera tu correo electronico.")

@tor.message_handler(commands=['regimen_fiscal'])
def comando_nombre(mensaje):
    chat_id = mensaje.chat.id
    message_array = mensaje.text.split()
    message_array.pop(0)
    nombre = ' '.join(message_array)
    tor.send_message(
        chat_id,
        "Entendido, " + nombre + " sera tu regimen fiscal.")

@tor.message_handler(func=lambda message: message.text == 'Solicitar factura')
def handle_text_doc(message):
    tor.send_message(
        message.chat.id,
        'Al parecer tus datos no estan egistrados en nuestro sistema.\n'
        ' A continuacion puedes registrar tu informacion de la siguiente'
        ' manera!.\n\n1.-/rfc "tu rfc"\n2./razon_social '
        '"tu razon social"-\n3.-/calle "tu calle"\n'
        '4.-/numero_int "tu numero interior"\n'
        '5.-/numero_ext "tu numero exterior"'
        '\n6.-/colonia "tu colonia"\n7.-/ciudad "tu ciudad"'
        '\n8.-/estado "tu estado"\n9.-/localidad "tu localidad"'
        '\n10.-/codigo_postal "tu codigo postal"\n'
        '11.-/email "tu email"\n12.-/regimen_fiscal "tu regimen fiscal"\n')
    pass

# @tor.message_handler(commands=['mis_puntos'])
# def comando_regimen_fiscal(mensaje):
#     chat_id = mensaje.chat.id
#     tor.send_message(
#         chat_id,
#         "Hola " + mensaje.chat.first_name +
#         ", sumando tu ultima compra actualmente cuentas con una cantidad de "
#         "8745 puntos. Que tengas un excelente dia")

# @tor.message_handler(func=lambda message: message.text == 'Checar mis puntos')
# def handle_text_doc(message):
#     tor.send_message(message.chat.id, 'Acabas de seleccionar checar puntos')
#     import ipdb; ipdb.set_trace()
#     pass

# @tor.message_handler(func=lambda message: message.text == 'Realizar encuesta')
# def handle_text_doc(message):
#     tor.send_message(message.chat.id, 'Acabas de seleccionar realizar encuesta')
#     pass

# def listener(mensajes):
#     for mensaje in mensajes:

# tor.set_update_listener(listener)
tor.polling()
