from flask import Flask, render_template, request
import movies_recommendation as m_rx

# initializing the flask app
app = Flask(__name__)
app.secret_key = "secret_key"


# default routing for the app
@app.route("/")
def home():
  return render_template('index.html')


@app.route("/recommend", methods=['POST'])
def recommend():
  movie_name = request.form['movies']
  recommend_movies = m_rx.main_call(movie_name)
  return render_template('index.html', recommend_movies=recommend_movies, name=movie_name)


# main function
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')  # for debugging purpose
  # app.run()
