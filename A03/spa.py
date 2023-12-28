from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para fornecer dados para a SPA 
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from the API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
