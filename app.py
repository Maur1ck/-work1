from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Настройки Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if not name or not phone or not email:
        flash('Все поля должны быть заполнены.', 'danger')
        return redirect('/')

    msg = Message('Новая заявка с сайта',
                  sender='your_email@gmail.com',
                  recipients=['recipient_email@example.com'])  # Получатель
    msg.body = f"""
    Имя: {name}
    Телефон: {phone}
    E-mail: {email}
    """
    try:
        mail.send(msg)
        flash('Заявка успешно отправлена!', 'success')
    except Exception as e:
        flash(f'Ошибка при отправке: {str(e)}', 'danger')

    return redirect('/')
