from flask import Flask, render_template

# create flask instance 
app = Flask(__name__)

# create a decorator
# @app.route('/')
# def index():
#   return "<h1>Hello World!</h1>"


@app.route('/user/<name>')
def user(name):
  return render_template('user.html', user_name=name)

# custom error pages 
#invalid url
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500

# @app.route('/')
# def index():
#   return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)