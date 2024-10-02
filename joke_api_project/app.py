from flask import Flask, jsonify
from models import db, Joke
from fetch_jokes import fetch_jokes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jokes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/fetch-jokes', methods=['GET'])
def fetch_and_store_jokes():
    jokes_data = fetch_jokes()

    for joke_data in jokes_data:
        existing_joke = Joke.query.get(joke_data.get('id'))
        if not existing_joke:
            joke = Joke(
                id=joke_data.get('id'),
                category=joke_data.get('category'),
                type=joke_data.get('type'),
                joke=joke_data.get('joke'),
                setup=joke_data.get('setup'),
                delivery=joke_data.get('delivery'),
                nsfw=joke_data.get('flags', {}).get('nsfw', False),
                political=joke_data.get('flags', {}).get('political', False),
                sexist=joke_data.get('flags', {}).get('sexist', False),
                safe=joke_data.get('safe', True),
                lang=joke_data.get('lang', 'en')
            )
            db.session.add(joke)
    
    db.session.commit()
    
    return jsonify({'message': f'Successfully fetched and stored {len(jokes_data)} jokes.'})

if __name__ == '__main__':
    app.run(debug=True)
