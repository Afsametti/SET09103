from flask import Flask , url_for , abort, request
app = Flask ( __name__ )

@app.route("/")
def hello():
	return "Hello napier"

@app.route('/static-example/img')
def static_example_img():
	start = '<img src="'
	url = url_for('static', filename='images/vmask.jpg')
	end = '">'
	return start+url+end, 200

@app.route("/account/", methods=['GET', 'POST'])
def account():
	if request.method == 'POST':
		return "method = POST"
	else:
		return "method = GET"

@app.route()

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)