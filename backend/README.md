# Cluster Classes Backend

This directory contains the Flask backend for the Cluster Classes website.

## Setup and Installation

1.  **Install Dependencies:**
    Make sure you have Python and pip installed. Then, install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Initialize the Database:**
    The first time you run the application, you need to initialize the database and create the necessary tables. Run the following commands from the root directory of the project:
    ```bash
    export FLASK_APP=backend/app.py
    flask db init --directory backend/migrations
    flask db migrate -m "Initial migration." --directory backend/migrations
    flask db upgrade --directory backend/migrations
    ```
    *Note: If you are running the commands from within the `backend` directory, you can omit `backend/` from the `FLASK_APP` path and the `--directory` flag.*

## Running the Server

To run the Flask development server, execute the following command from the root directory:
```bash
python -m backend.app
```
Alternatively, you can use the `flask` command:
```bash
export FLASK_APP=backend/app.py
flask run
```

The server will start on `http://127.0.0.1:5000`.