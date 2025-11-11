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
    pokrmon_info = {
        'name': pokemon_data['name'],
        'id': pokemon_data['id'],
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'types': [t['type']['name'] for t in pokemon_data['types']],
        'abilities': [a['ability']['name'] for a in pokemon_data['abilities']],
        'sprite': pokemon_data['sprites']['front_default'],
        'stats': {}
    }


if __name__ == '__main__':
    app.run(debug=True)
