from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)
app.secret_key = 'aish'  


usr_data = {'username': "", 'email': "", 'pass': "" , 'firstname': "" , "lastname" : ""}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indoor')
def indoor():
    return render_template('indoor.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == usr_data['username'] and password == usr_data['pass']:
            return redirect('/indoor')  
        else:
            return "Invalid username or password", 401  
    else:
        return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        global first_name   
        global last_name 
        global usr_data
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        

        usr_data['username'] = username
        usr_data['email'] = email
        usr_data['pass'] = password
        usr_data['firstname'] = first_name
        usr_data['lastname'] = last_name 
        return redirect('/login')
    else:
        return render_template('signup.html', firstname="", lastname="", username="", email="", password="")

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
    
    message = f"Hello! I'm {first_name} {last_name} I would like to book the {court_name} for the {time_slot} slot. Can you confirm the availability and price?"

    encoded_message = urllib.parse.quote(message)

    whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True)