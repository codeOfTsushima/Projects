from flask import Flask, render_template, jsonify

app = Flask(__name__)

#This is the route to the website
@app.route('/')
def home():
    return render_template('index.html')

#This is the API route
@app.route('/api/test', methods=['GET'])
def test_connection():
    #jsonify is what that converts the python dictionaries into string. The js reads it and understands it
    return jsonify({'status': 'success vamos', 'message': 'Python test'})

if __name__ == '__main__':
    app.run(debug=True)