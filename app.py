from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# The "Database" 
messages = []

#It is the route to the website
@app.route('/')
def home():
    return render_template('index.html')

#This is the API route
@app.route('/api/get_message', methods=['GET'])
def get_message():
    if len(messages) > 0:
        #POP the first message basically Get it and delete it
        secret = messages.pop(0)
        return jsonify({'found': True, 'text': secret})
    else:
        return jsonify({'found': False})

@app.route('/api/plant', methods=['POST'])
def plant_bomb():
    data = request.get_json()
    new_secret = data.get('secret_message')
    
    if new_secret:
        messages.append(new_secret)
        return jsonify({'status': 'saved'})
    
    return jsonify({'status': 'error'}), 400 

if __name__ == '__main__':
    app.run(debug=True)