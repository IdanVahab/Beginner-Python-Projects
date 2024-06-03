import string
import secrets
from flask import Flask, render_template_string, request, redirect, url_for, send_file
import io

app = Flask(__name__)


def contains_upper(password: str) -> bool:
    return any(char.isupper() for char in password)  # בדיקה אם יש אותיות גדולות בסיסמה


def contains_symbol(password: str) -> bool:
    return any(char in string.punctuation for char in password)  # בדיקה אם יש סימנים בסיסמה


def contains_lower(password: str) -> bool:
    return any(char.islower() for char in password)  # בדיקה אם יש אותיות קטנות בסיסמה


def generate_password(length: int) -> str:
    while True:
        password = ''.join(
            secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))  # יצירת סיסמה אקראית

        # וידוא שהסיסמה עומדת בכל הקריטריונים
        if (contains_upper(password) and contains_symbol(password) and
                contains_lower(password) and 1 <= sum(1 for char in password if char in string.punctuation) <= 2):
            return password  # החזרת הסיסמה אם היא עומדת בכל הקריטריונים


@app.route('/', methods=['GET', 'POST'])
def index():
    passwords = [generate_password(length=8) for _ in range(5)]  # יצירת 5 סיסמאות אקראיות

    if request.method == 'POST':
        selected_password = request.form.get('password')  # קבלת הסיסמה שנבחרה מהמשתמש
        return redirect(url_for('success', password=selected_password))  # ניתוב לעמוד הצלחה עם הסיסמה שנבחרה

    return render_template_string('''
        <html>
        <head>
            <title>Password Selector</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;700&display=swap');
                body {
                    font-family: 'Modern Beautiful Serif Font', serif;
                    color: #31473A;
                    background-color: #31473A;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background-color: #EDF4F2;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    width: 300px;
                    text-align: center;
                }
                h1 {
                    font-size: 24px;
                    margin-bottom: 20px;
                }
                .password-option {
                    margin-bottom: 10px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 10px 0;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Select a Password</h1>
                <form method="post">
                    {% for i, password in enumerate(passwords) %}
                        <div class="password-option">
                            <input type="radio" id="password{{i}}" name="password" value="{{password}}">
                            <label for="password{{i}}">{{password}}</label>
                        </div>
                    {% endfor %}
                    <button type="submit">Select Password</button>
                </form>
            </div>
        </body>
        </html>
    ''', passwords=passwords, enumerate=enumerate)  # הצגת הטופס לבחירת סיסמה


@app.route('/success', methods=['GET', 'POST'])
def success():
    password = request.args.get('password')  # קבלת הסיסמה מהכתובת

    if request.method == 'POST':
        # יצירת אובייקט קובץ זמני עם הסיסמה
        buffer = io.BytesIO()
        buffer.write(password.encode())
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name='password.txt', mimetype='text/plain')  # שליחת הקובץ להורדה

    return render_template_string('''
        <html>
        <head>
            <title>Password Success</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;700&display=swap');
                body {
                    font-family: 'Modern Beautiful Serif Font', serif;
                    color: #31473A;
                    background-color: #31473A;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    background-color: #EDF4F2;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    width: 360px; /* 20% wider */
                }
                h1 {
                    font-size: 24px;
                    margin-bottom: 20px;
                }
                .selected-password {
                    font-weight: bold;
                    margin-top: 10px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 10px 0;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Password Selection Successful</h1>
                <div class="selected-password">Selected Password: {{ password }}</div>
                <form method="post">
                    <button type="submit">Download Password</button>
                </form>
            </div>
        </body>
        </html>
    ''', password=password)  # הצגת עמוד הצלחה עם אפשרות להוריד את הסיסמה


if __name__ == '__main__':
    app.run(debug=True)  # הרצת האפליקציה במצב דיבאג
