import telebot
from openai import OpenAI
import os

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@bot.message_handler(func=lambda m: True)
def chat(message):
    response = client.responses.create(
        model="gpt-5",
        input=message.text
    )
    bot.reply_to(message, response.output_text)

bot.polling()
