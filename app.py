from flask import Flask, render_template, request, redirect, flash
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@app.route('/')
def index():
    return render_template('main.html')


def send_telegram_message(chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        return True
    except Exception as e:
        print(f"Error sending message to Telegram: {str(e)}")
        return False


@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if not name or not phone or not email:
        flash('Все поля должны быть заполнены.', 'danger')
        return redirect('/')

    message = f"Имя: {name}\nТелефон: {phone}\nE-mail: {email}"
    print(message)
    try:
        send_telegram_message(TELEGRAM_CHAT_ID, message)
        flash('Заявка успешно отправлена!', 'success')
    except Exception as e:
        flash(f'Ошибка при отправке: {str(e)}', 'danger')

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)