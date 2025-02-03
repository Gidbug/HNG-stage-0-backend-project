# HNG-stage-0-backend-project


# HNG Stage 0 Backend Task

## Project Description
This is a simple Flask-based API developed as part of the HNG Stage 0 backend task. The API provides basic information including Slack name, email, current UTC datetime, and a GitHub repository link.

## Setup Instructions
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- pip (Python package manager)
- Flask
- Flask-CORS

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Gidbug/HNG-stage-0-backend-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd HNG-stage-0-backend-project
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```
   The server should now be running on `http://127.0.0.1:5000/`

## API Documentation
### Endpoint
**GET /**
- **URL:** `/`
- **Method:** `GET`
- **Response Format:** JSON
- **Response Example:**
  ```json
  {
    "slack_name": "YourSlackName",
    "email": "oyerindegideon01@gmail.com",
    "current_datetime": "2025-01-31T12:00:00Z",
    "github_url": "https://github.com/Gidbug/HNG-stage-0-backend-project"
  }
  ```

## Deployment
To deploy the project, ensure it runs on a cloud platform like Heroku, Render, or any service supporting Flask applications.

## Resources
For more Python-related development, check out: [Hire Python Developers](https://hng.tech/hire/python-developers).

