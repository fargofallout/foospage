import flask


app = flask.Flask(__name__)

def main():
	register_blueprints()
	app.run(debug=True)

def register_blueprints():
	from foospage.views import home

if __name__ == "__main__":
	main()
