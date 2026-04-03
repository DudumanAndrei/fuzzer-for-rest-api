# fuzzzer-for-rest-api
A Python Object-Oriented Fuzzer for a RESTful API

## Target Overview
This project builds a modular Python fuzzer. The main target is VAmPI, a vulnerable API containing intentional security flaws. We run this API locally using Docker on port 5001. This setup prevents network blocks during testing.

## Target Analysis
We scanned the target using Nmap. The scan found a Python 3.11 environment. The server uses Werkzeug 2.2.3. The API returns data in JSON format. We mapped the endpoints using ffuf. The active routes include /users/v1 and /books/v1. The system also exposes the /createdb route.

## Project Status
We have successfully transitioned to an Object-Oriented Python architecture. The fuzzer is currently composed of modular classes for:
- Generating malformed requests (`RequestGenerator`)
- Handling HTTP traffic (`HttpClient`)
- Analyzing the target's responses for vulnerabilities (`ResponseAnalyzer`)

## Technologies Used
- **Python 3**: Core programming language used for the fuzzer architecture.
- **Requests**: Python library used for handling HTTP network traffic.
- **Doxygen & Graphviz**: Used for generating HTML documentation and detailed UML class hierarchy diagrams.
- **Docker**: Used to securely host the vulnerable VAmPI target locally.
- **Nmap & ffuf**: Used during the initial reconnaissance and endpoint discovery phase.

## Setup and Execution
### 1. Start the Target API
Ensure the VAmPI Docker container is running and accessible locally on port `5001`.

### 2. Configure the Python Environment
Navigate to the root of the project and set up your virtual environment to install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
brew install doxygen
```

### 3. Run the Fuzzer
```bash
python main.py
```