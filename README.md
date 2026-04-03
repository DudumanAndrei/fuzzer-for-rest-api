# fuzzzer-for-rest-api
A basic Python Object-Oriented Fuzzer for a RESTful API

## Target Overview
This project builds a modular Python fuzzer. The main target is VAmPI, a vulnerable API containing intentional security flaws. We run this API locally using Docker on port 5001. This setup prevents network blocks during testing.

## Target Analysis
We scanned the target using Nmap. The scan found a Python 3.11 environment. The server uses Werkzeug 2.2.3. The API returns data in JSON format. We mapped the endpoints using ffuf. The active routes include /users/v1 and /books/v1. The system also exposes the /createdb route.

## Project Status
We have successfully transitioned to an Object-Oriented Python architecture. The fuzzer is currently composed of modular classes for:
- Generating malformed requests (`RequestGenerator`)
- Handling HTTP traffic (`HttpClient`)
- Analyzing the target's responses for vulnerabilities (`ResponseAnalyzer`)