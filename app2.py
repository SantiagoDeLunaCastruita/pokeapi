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
    if not pokemon_name:
        flash('porfavor,mo te ags wey','error')
        return redirect(url_for('index'))
    resp = request.get(f"{API}{pokemon_name}")
    if resp.status_code == 200:
        pokemon_data = resp.json()
        return render_template('pokemon.html',pokemon=pokemon_name)


if __name__ == '__main__':
    app.run(debug=True)
