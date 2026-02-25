# Quick Start Guide

This guide will help you get started with the Mergington High School Activities application.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/AranchaPM/skills-getting-started-with-github-copilot.git
   cd skills-getting-started-with-github-copilot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Option 1: Using the Run Script (Recommended)

Simply execute:
```bash
python run.py
```

You should see output like:
```
Starting Mergington High School Activities API...
Server will be available at: http://localhost:8000
API documentation: http://localhost:8000/docs
Press CTRL+C to stop the server
```

### Option 2: Using uvicorn directly

```bash
python -m uvicorn src.app:app --reload
```

## Accessing the Application

Once the server is running, you can access:

- **Web Interface**: http://localhost:8000
  - View all available activities
  - Sign up for activities using a student email

- **API Documentation (Swagger UI)**: http://localhost:8000/docs
  - Interactive API documentation
  - Test API endpoints directly from the browser

- **API Documentation (ReDoc)**: http://localhost:8000/redoc
  - Alternative API documentation format

## Running Tests

To ensure everything is working correctly, run the test suite:

```bash
# Run all tests with verbose output
pytest test_app.py -v

# Run with test coverage
pytest test_app.py --cov=src
```

Expected output:
```
================================================= test session starts ==================================================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0
collected 6 items

test_app.py::test_root_redirects PASSED                          [ 16%]
test_app.py::test_get_activities PASSED                          [ 33%]
test_app.py::test_signup_for_activity_success PASSED             [ 50%]
test_app.py::test_signup_for_nonexistent_activity PASSED         [ 66%]
test_app.py::test_signup_multiple_students PASSED                [ 83%]
test_app.py::test_activities_have_correct_fields PASSED          [100%]

================================================== 6 passed in 0.53s ===================================================
```

## Example API Usage

### Get All Activities

```bash
curl http://localhost:8000/activities
```

Response:
```json
{
  "Chess Club": {
    "description": "Learn strategies and compete in chess tournaments",
    "schedule": "Fridays, 3:30 PM - 5:00 PM",
    "max_participants": 12,
    "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
  },
  "Programming Class": {
    "description": "Learn programming fundamentals and build software projects",
    "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
    "max_participants": 20,
    "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
  },
  "Gym Class": {
    "description": "Physical education and sports activities",
    "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
    "max_participants": 30,
    "participants": ["john@mergington.edu", "olivia@mergington.edu"]
  }
}
```

### Sign Up for an Activity

```bash
curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=newstudent@mergington.edu"
```

Response:
```json
{
  "message": "Signed up newstudent@mergington.edu for Chess Club"
}
```

## Project Structure

```
.
├── src/
│   ├── app.py              # Main FastAPI application
│   ├── README.md           # API documentation
│   └── static/             # Frontend files
│       ├── index.html      # Main web page
│       ├── styles.css      # Styles
│       └── app.js          # Frontend JavaScript
├── test_app.py             # Test suite
├── run.py                  # Convenient run script
├── requirements.txt        # Python dependencies
└── README.md              # Main documentation

```

## What's Next?

This starter application demonstrates:
- ✅ A working FastAPI backend with REST endpoints
- ✅ A web frontend with HTML/CSS/JavaScript
- ✅ Comprehensive test coverage
- ✅ Easy setup and deployment
- ✅ Interactive API documentation

You can extend this application by:
- Adding authentication and authorization
- Persisting data to a database (SQLite, PostgreSQL, etc.)
- Adding more activity properties (location, instructor, etc.)
- Implementing email notifications
- Adding a student profile page
- Implementing activity search and filtering

## Troubleshooting

**Port already in use?**
```bash
# Find the process using port 8000
lsof -i :8000

# Kill the process (replace PID with actual process ID)
kill <PID>
```

**Import errors?**
Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

**Tests failing?**
Ensure you're in the project root directory when running tests:
```bash
cd /path/to/skills-getting-started-with-github-copilot
pytest test_app.py -v
```

## Contributing

This is a learning project for GitHub Copilot. Feel free to experiment and make improvements!
