from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    night_mode = False  # Track night mode state

    if request.method == 'POST':
        expression = request.form.get('expression', '')
        night_mode = request.form.get('night_mode', 'off') == 'on' 
        try:
            result = eval(expression)
        except Exception as e:
            result = f"Error: {e}"
    
    display_value = result if isinstance(result, (int, float)) else ''
    
    return render_template_string('''
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #e0e0e0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                transition: background-color 0.3s;
            }
            .calculator {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                width: 320px;
                transition: background-color 0.3s;
            }
            input {
                width: 100%;
                padding: 15px;
                font-size: 24px;
                text-align: right;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            button {
                padding: 20px;
                font-size: 20px;
                margin: 5px;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: white;
                cursor: pointer;
                transition: background-color 0.3s;
                flex: 1; /* Makes buttons equal size */
            }
            button:hover {
                background-color: #45a049;
            }
            .button-row {
                display: flex;
            }
            .night-mode {
                background-color: #333;
                color: white;
            }
            .night-mode input {
                background-color: #555;
                color: white;
                border-color: #4CAF50;
            }
            .night-mode button {
                background-color: #444;
            }
            .night-mode button:hover {
                background-color: #555;
            }
        </style>
        <div class="calculator{{ ' night-mode' if night_mode else '' }}">
            <form method="POST">
                <input type="hidden" name="night_mode" value="{{ 'on' if night_mode else 'off' }}">
                <input type="text" id="expression" name="expression" value="{{ display_value }}" placeholder="0" required>
                <div class="button-row">
                    <button type="button" onclick="addToExpression('7')">7</button>
                    <button type="button" onclick="addToExpression('8')">8</button>
                    <button type="button" onclick="addToExpression('9')">9</button>
                    <button type="button" onclick="addToExpression('/')">/</button>
                </div>
                <div class="button-row">
                    <button type="button" onclick="addToExpression('4')">4</button>
                    <button type="button" onclick="addToExpression('5')">5</button>
                    <button type="button" onclick="addToExpression('6')">6</button>
                    <button type="button" onclick="addToExpression('*')">*</button>
                </div>
                <div class="button-row">
                    <button type="button" onclick="addToExpression('1')">1</button>
                    <button type="button" onclick="addToExpression('2')">2</button>
                    <button type="button" onclick="addToExpression('3')">3</button>
                    <button type="button" onclick="addToExpression('-')">-</button>
                </div>
                <div class="button-row">
                    <button type="button" onclick="addToExpression('0')">0</button>
                    <button type="button" onclick="addToExpression('+')">+</button>
                    <button type="button" onclick="clearInput()">C</button>
                    <button type="submit">=</button>
                </div>
                <div class="button-row">
                    <button type="button" onclick="toggleNightMode()">Night Mode</button>
                </div>
            </form>
        </div>
        <script>
            function addToExpression(value) {
                const input = document.getElementById('expression');
                input.value += value;
                input.focus(); // Set focus back to the input field
            }

            function clearInput() {
                const input = document.getElementById('expression');
                input.value = '';
                input.focus(); // Set focus back to the input field
            }

            function toggleNightMode() {
                const calculator = document.querySelector('.calculator');
                calculator.classList.toggle('night-mode');
                const nightModeInput = document.querySelector('input[name="night_mode"]');
                nightModeInput.value = calculator.classList.contains('night-mode') ? 'on' : 'off';
            }
        </script>
    ''', display_value=display_value, night_mode=night_mode)

if __name__ == '__main__':
    app.run(debug=True)
