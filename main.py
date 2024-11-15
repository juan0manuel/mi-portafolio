# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_sql = request.form.get('button_sql')
    email = request.form.get('email')
    text = request.form.get('text')
    with open('form.txt', 'a') as f:
        f.write(f"FORMULARIO\n{email}\n{text}\n")
    return render_template('index.html', button_python=button_python,
                                         button_discord=button_discord,
                                         button_html= button_html,
                                         button_sql= button_sql,
                                         email = email,
                                         text = text)


if __name__ == "__main__":
    app.run(debug=True)
