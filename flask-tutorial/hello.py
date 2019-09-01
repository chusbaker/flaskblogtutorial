from flashkl import FLASK

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, Yellow!'