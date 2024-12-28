from flask import Flask , render_template , request , redirect
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indoor')
def indoor():
    return render_template('indoor.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/book', methods=['GET'])
def book_now():
    # Get parameters from query string
    court_name = request.args.get('court')
    time_slot = request.args.get('time')
    phone_number = request.args.get('number') 

    if not court_name or not time_slot or not phone_number:
        return "Missing required parameters.", 400

    # Generate the message
    message = f"Hello! I would like to book the {court_name} for the {time_slot} slot. Can you confirm the availability and price?"
    encoded_message = urllib.parse.quote(message)  # Encode the message for URL

    # Generate WhatsApp URL
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
    
    # Redirect to WhatsApp
    return redirect(whatsapp_url)


if __name__ == '__main__':
    app.run(debug=True)