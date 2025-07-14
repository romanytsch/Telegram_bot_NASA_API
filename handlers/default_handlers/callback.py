from loader import bot
from handlers.default_handlers.image_day import send_apod_day, send_apod_random
from handlers.default_handlers.image_data import send_apod_date

@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    if call.data == "btn_image_day":
        send_apod_day(call.message.chat.id)
    elif call.data == "btn_image_random":
        send_apod_random(call.message.chat.id)
    elif call.data == "btn_image_data":
        bot.answer_callback_query(call.id)
        msg = bot.send_message(call.message.chat.id,
                               "Введите дату в формате ГГГГ-ММ-ДД (например, 2023-07-14), "
                               "но не ранее 16 июня 1995:")
        bot.register_next_step_handler(msg, send_apod_date)