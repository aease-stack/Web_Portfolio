from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# In-memory storage for messages
messages = []

# HTML template
template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp-like Messaging App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e5ddd5;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        .header {
            background-color: #075e54;
            color: white;
            padding: 10px;
            border-radius: 10px 10px 0 0;
            text-align: center;
            font-size: 24px;
        }
        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
            margin: 10px 0;
        }
        .message {
            border-radius: 20px;
            padding: 10px 15px;
            margin: 5px 0;
            max-width: 70%;
            clear: both;
            position: relative;
        }
        .message.left {
            background: #dcf8c6;
            margin-right: auto;
        }
        .message.right {
            background: #ffffff;
            margin-left: auto;
            border: 1px solid #e5e5e5;
        }
        .message h3 {
            margin: 0 0 5px 0;
            font-size: 14px;
            color: #333;
        }
        .message p {
            margin: 0;
            font-size: 16px;
        }
        form {
            display: flex;
            margin-top: 10px;
        }
        input[type="text"], textarea {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 20px;
            resize: none;
            margin-right: 10px;
        }
        button {
            padding: 10px;
            background-color: #075e54;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #054b44;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">Chat</div>
        <div class="messages">
            {% for message in messages %}
                <div class="message {{ 'left' if loop.index0 % 2 == 0 else 'right' }}">
                    <h3>{{ message.title }}</h3>
                    <p>{{ message.content }}</p>
                    <form method="POST" action="/delete/{{ loop.index0 }}" style="display:inline;">
                        <button type="submit" style="background-color: #dc3545; border-radius: 20px;">Delete</button>
                    </form>
                </div>
            {% endfor %}
        </div>
        <form method="POST" action="/add">
            <input type="text" name="title" placeholder="Your Name" required>
            <textarea name="content" placeholder="Type a message..." required></textarea>
            <button type="submit">Send</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template, messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    title = request.form['title']
    content = request.form['content']
    messages.append({'title': title, 'content': content})
    return redirect(url_for('index'))

@app.route('/delete/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    if 0 <= message_id < len(messages):
        messages.pop(message_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
