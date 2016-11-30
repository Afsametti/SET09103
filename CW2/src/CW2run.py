from flask import Flask, render_template
app = Flask(__name__)

#Homepage
@app.route("/")
def index():
	return render_template('index.html', title='Mies fanpage | Home'), 200

#Biography
@app.route('/biography/')
def mies_biography():
	return render_template('biography.html', title='Mies fanpage | Biography'), 200



#Contact
@app.route('/contact/')
def mies_contact():
	return render_template('contact.html', title='Mies fanpage | Contact'), 200

#Error page 404
@app.errorhandler (404)
def page_not_found (error):
	return render_template('404.html', title='Mies fanpage | Error'), 404

if __name__ == "__main__":
 	app.run(host='0.0.0.0', debug=True)