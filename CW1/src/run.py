import os
from flask import Flask, url_for, render_template
app = Flask(__name__)

#Homepage
@app.route("/")
def index():
  return render_template('index.html', title='Home')

#Singles
@app.route('/singles')
def comedies():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  return render_template('singles.html', title='Singles')

#Music Videos
@app.route('/music-videos/')
def drama():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  return render_template('music-videos.html', title='Music Videos')


#Error page
@app.errorhandler (404)
def page_not_found (error):
  return render_template('404.html', title='Error'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False)