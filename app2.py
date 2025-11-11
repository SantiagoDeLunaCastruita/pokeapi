from flask import Flask ,render_template,request,redirect,url_for

app = Flask(__name__)
app.secret_key = '25092009'
API="https://pokeapi.co/api/v2/pokemon/"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/search',methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name,').strip().lower()
    


if __name__ == '__main__':
    app.run(debug=True)
