from flask import Flask, render_template

app = Flask(__name__)

#Lập ra movie_list
class Movie:
    def __init__(self, title, img):
        self.title = title
        self.img = img

movie1 = Movie("Tom & Jerry", "https://upload.wikimedia.org/wikipedia/en/5/5f/TomandJerryTitleCardc.jpg")
movie2 = Movie("Harry Potter", "http://static.independent.co.uk/s3fs-public/styles/article_large/public/thumbnails/image/2013/09/12/17/potter.jpg")
movie_list = [
    movie1,
    movie2,
    Movie("50 Shades of Grey", "http://cdn04.cdn.justjared.com/wp-content/uploads/headlines/2015/04/fifty-shades-of-grey-writer.jpg")
    ]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<name>')
def hello(name):
    return 'Hello ' + name

#Dữ liệu nằm tại file HTML:
@app.route('/movie_1')
def get_movie():
    return render_template('movie_1.html')

#Dữ liệu nằm tại file Lập trình Web Session:
@app.route('/movie_2')
def get_movie_2():
    return render_template(
        'movie_2.html',
        title = 'CIVIL WAR',
        img="http://lovelace-media.imgix.net/uploads/1143/9a4331d0-041a-0134-e757-0a315da82319.jpg?")

#Cách bật với dữ liệu list, nằm tại file lập trình Web Session:
@app.route('/movies')
def movies():
    return render_template('movies.html', movies = movie_list)







if __name__ == '__main__':
    app.run()
