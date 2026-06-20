from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def home():
    return """
    
    <center>
     <h3>Student Registration Form</h3>
        <form>
            <label>Full Name:</label><br>
            <input type="text"><br><br>

            <label>Department:</label><br>
            <input type="text"><br><br>

            <label>Email:</label><br>
            <input type="email"><br><br>

            <label>Phone Number:</label><br>
            <input type="tel"><br><br>

            <input type="submit" value="Register">
        </form>
        </center>

    """

if __name__ == '__main__':
    app.run(debug = True)


@app.route('/about')
def about():
    return "This is the about page"

@app.route('/contact')
def contact():
    return "This is the contact page"
