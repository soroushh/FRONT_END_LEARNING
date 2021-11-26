from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	email = request.form['email']
	name = request.form['name']

	if name and email:
		newName = name[::-1]

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})

@app.route("/2")
def index_2():
    return render_template("index.html", **{'greeting': 'Hello from Flask!'})

@app.route("/3")
def index_3():
    return render_template("index_2.html", **{'message': 'Hello from Flask!'})

if __name__ == '__main__':
	app.run(debug=True)
