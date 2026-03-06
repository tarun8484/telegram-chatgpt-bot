import os
import telebot
from openai import OpenAI

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=message.text
        )
        bot.reply_to(message, response.output_text)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.remove_webhook()
bot.infinity_polling(skip_pending=True)
