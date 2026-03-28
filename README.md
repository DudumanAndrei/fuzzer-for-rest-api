# fuzzzer-for-rest-api
A basic C++ Fuzzer for a RESTful API

## Target Overview
This project builds a C++ fuzzer. The main target is VAmPI. VAmPI is a vulnerable API. It contains intentional security flaws. We run this API locally using Docker on port 5001. This setup prevents network blocks during testing.

## Target Analysis
We scanned the target using Nmap. The scan found a Python 3.11 environment. The server uses Werkzeug 2.2.3. The API returns data in JSON format. We mapped the endpoints using ffuf. The active routes include /users/v1 and /books/v1. The system also exposes the /createdb route.

## Project Status
We will use these details to build the HTTP requests. We need to design the fuzzer architecture. The C++ implementation steps remain to be established.