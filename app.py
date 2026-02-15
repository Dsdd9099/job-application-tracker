from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9099",
    database="jobtracker"
)


@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()
    return render_template("index.html", applications=applications)

@app.route('/add', methods=['POST'])
def add_application():
    company = request.form['company']
    role = request.form['role']
    status = request.form['status']
    date_applied = request.form['date_applied']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO applications (company, role, status, date_applied) VALUES (%s, %s, %s, %s)",
        (company, role, status, date_applied)
    )
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_application(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM applications WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

@app.route('/update/<int:id>')
def update_status(id):
    cursor = db.cursor()
    cursor.execute("UPDATE applications SET status='Interview' WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
