# Student Management System

A simple Student Management System built using Python, Flask, Docker, and Git.

## Features
- Add student records
- Web-based interface using Flask
- Docker containerization
- Automated tests using pytest

## Technologies Used
- Python
- Flask
- Docker
- Git and GitHub
- pytest

## Run Locally with Docker

Build the Docker image:

```bash
docker build -t student-management-app .
```

Run the container:

```bash
docker run -d --name student-management-container -p 5001:5000 student-management-app
```

Open your browser at:

http://localhost:5001

## Project Structure

```text
student-management-devops/
├── app/
│   └── routes.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Author
Student Management System project for DevOps practice.
