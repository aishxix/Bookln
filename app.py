from flask import Flask , render_template , request , redirect
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indoor')
def indoor():
    return render_template('indoor.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/book', methods=['GET'])
def book_now():

    court_name = request.args.get('court')
    time_slot = request.args.get('time')
    phone_number = request.args.get('number') 

    if not court_name or not time_slot or not phone_number:
        return "Missing required parameters.", 400


    message = f"Hello! I would like to book the {court_name} for the {time_slot} slot. Can you confirm the availability and price?"
    encoded_message = urllib.parse.quote(message)  


    whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
    

    return redirect(whatsapp_url)


if __name__ == '__main__':
    app.run(debug=True)