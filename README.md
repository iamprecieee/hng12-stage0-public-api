## Simple Public API

### Description
---
A simple API endpoint that retrieves basic information as JSON data, built using Django/Django Rest Framework.

### Local Setup
---
- Clone the project [repository](https://github.com/iamprecieee/stage-0-backend).
- Ensure python is installed.
- Create and activate a virtual environment:
    <details>
    <summary><b>macOS/Linux</b></summary>

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    </details>
    <details>
    <summary><b>Windows</b></summary>

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    </details>
- Install project dependencies:
    ``` bash
    pip install requirements.txt
    ```
- Create a `.env` file for secrets from the `.env.example`
- Run the project on a local server:
    ```bash
    python manage.py runserver
    ```

### API Documentation
- Endpoint URL: `/`
- Method: `GET`
- Response Format: The JSON response data includes the following fields - `email`, `current_datetime`, `github_url`.
- Example Request:
    ```bash
    curl -X GET https://test.com/api/v1/data
    ```
- Example Response: 
    ```bash
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "email": "test@gmail.com",
        "current_datetime": "2025-01-28T22:02:37.737454Z",
        "github_url": "https://github.com/test"
    }
    ```
- Swagger-UI: [live-docs](https://iamprecieee-endpoint.onrender.com)
<br>

## Hire From HNG
- [python](https://hng.tech/hire/python-developers)
- [csharp](https://hng.tech/hire/csharp-developers)
- [golang](https://hng.tech/hire/golang-developers)
- [php](https://hng.tech/hire/php-developers) 
- [java](https://hng.tech/hire/java-developers) 
- [nodejs](https://hng.tech/hire/nodejs-developers)