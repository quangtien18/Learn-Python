from flask import Flask , render_template, url_for, redirect

app = Flask(__name__)

@app.route('/quangtien')
def quangtien () :
	return render_template ("quangtien.html")

@app.route('/pythonlagi')
def pythonlagi () :
	return render_template ("pythonlagi.html")

@app.route('/caidatpython')
def caidatpython () :

	return render_template ("caidatpython.html")

@app.route('/helloword')
def helloword () :
	return render_template ("helloword.html")

@app.route('/bientrongpython')
def bientrongpython () :
	return render_template("bientrongpython.html")

@app.route('/string')
def string () :
	return render_template ("string.html")

@app.route('/list')
def list () :
	return render_template ("list.html")

@app.route('/tuple')
def tuple () :
	return render_template ("tuple.html")

@app.route('/dictionary')
def dictionary () :
	return render_template ("dictionary.html")

@app.route('/hamtrongpython')
def hamtrongpython () :
	return render_template ("hamtrongpython.html")


if __name__ == "__main__" :
	app.run(debug = True)

