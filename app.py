from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/life')
def life():
   return render_template('life.html')

@app.route('/food')
def food():
   return render_template('food.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
