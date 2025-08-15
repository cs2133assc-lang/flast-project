from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://cs2133assc:E42pXauVq2ex8cW4@cluster0.zyazsyy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydb"]
collection = db["users"]


@app.route('/')
def homePage():
    return render_template("frontend.html")

@app.route('/submit', methods=['POST'])
def submit():
        try:
            name = request.form['name']
            email = request.form['email']
            collection.insert_one({"name": name, "email": email})
            return 'Data Inserted Success !'
        except Exception as e:
            error = str(e)
            return render_template('frontend.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
