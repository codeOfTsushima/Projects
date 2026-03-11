from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# The "Database" 
messages = []

#It is the route to the website
@app.route('/')
def home():
    return render_template('index.html')

#This is the API route
@app.route('/api/get_message/<viewer_id>', methods=['GET'])
def get_message(viewer_id):
    if len(messages) > 0:
        #POP the first message basically Get it and delete it
        first_bomb = messages[0]
        
        if first_bomb['sender_id'] != viewer_id:
            secret = messages.pop(0)
            # THE FIX: Added ['text'] to extract just the message string
            return jsonify({'found': True, 'text': secret['text']})
        else:
            return jsonify({'found': False, 'status': 'waiting'})
        
    return jsonify({'found': False, 'status': 'empty'})

@app.route('/api/plant', methods=['POST'])
def plant_bomb():
    data = request.get_json()
    new_secret = data.get('secret_message')
    sender_id = data.get('sender_id')
    
    if new_secret and sender_id:
        messages.append({'text': new_secret, 'sender_id': sender_id})
        return jsonify({'status': 'saved'})
    
    return jsonify({'status': 'error'}), 400 

if __name__ == '__main__':
    app.run(debug=True)