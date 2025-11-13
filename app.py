from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'nbkdslvnbsdbngbsnlNLNjbbNJEFSKNBGBDBNFNDBJDNBbdlnkdbdbeNEBDBFDJBJBFBSBSBÑDBDBDBBD'
API = "https://api.edamam.com/api/food-database/v2/parser"
API_KEY = "e9a5ac0153d31989a2542d877929f607"
API_ID = "f140b0a5"

@app.route('/')
def incio():
    return render_template('index.html')

@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    if request.method == 'POST':
        busqueda = request.form['busqueda', '']
        
        comida_info = {
            'api_key': API_KEY,
            'api_id': API_ID,
            'ingr': busqueda
        }
            
        return render_template('resultado.html', busqueda=busqueda)
    
    return redirect(url_for('incio'))

if __name__ == '__main__':
    app.run(debug=True)