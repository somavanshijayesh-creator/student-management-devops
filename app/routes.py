
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

students = []

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f4f6f9; }
        h1 { color: #17365d; }
        form, table { background: white; padding: 16px; margin-top: 20px; }
        input, button { padding: 10px; margin: 5px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background: #17365d; color: white; }
    </style>
</head>
<body>
    <h1>Student Management System</h1>
    <p>Manage student records in one place.</p>
    <form method="post" action="/add">
        <input name="name" placeholder="Student name" required>
        <input name="email" type="email" placeholder="Email" required>
        <input name="course" placeholder="Course" required>
        <button type="submit">Add Student</button>
    </form>
    <table>
        <tr><th>ID</th><th>Name</th><th>Email</th><th>Course</th></tr>
        {% for s in students %}
        <tr>
            <td>{{ s.id }}</td><td>{{ s.name }}</td>
            <td>{{ s.email }}</td><td>{{ s.course }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE, students=students)


@app.route("/add", methods=["POST"])
def add_student():
    student = {
        "id": len(students) + 1,
        "name": request.form["name"].strip(),
        "email": request.form["email"].strip(),
        "course": request.form["course"].strip(),
    }
    students.append(student)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
