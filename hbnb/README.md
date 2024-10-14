# HBNB Project

## Project Structure

- `app/`: Contains the core application code.
  - `api/`: Houses the API endpoints, organized by version.
  - `models/`: Contains the business logic classes.
  - `services/`: Implements the Facade pattern, managing the interaction between layers.
  - `persistence/`: Implements the in-memory repository.
- `run.py`: Entry point for running the Flask application.
- `config.py`: Configures environment variables and application settings.
- `requirements.txt`: Lists all the Python packages needed for the project.
- `README.md`: Contains a brief overview of the project.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
