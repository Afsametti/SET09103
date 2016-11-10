import os
from flask import Flask, render_template
app = Flask(__name__)

#Homepage
@app.route("/")
def home():
  return render_template('index.html', title='Home'), 200

#Singles
@app.route('/singles')
def singles():
  return render_template('singles.html', title='Singles'), 200

#Music Videos
@app.route('/musicvideos')
def musicvideos():
  return render_template('music-videos.html', title='Music Videos'), 200


#Error page 404
@app.errorhandler (404)
def page_not_found (error):
  return render_template('404.html', title='Error'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)