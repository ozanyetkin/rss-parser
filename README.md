*# rss-parser
Simple RSS parser microservice written in Python
# RSS Feed Parser Microservice

This microservice parses RSS feeds daily and pushes the data to Firebase Realtime Database in JSON format.

## Table of Contents

- [RSS Feed Parser Microservice](#rss-feed-parser-microservice)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
  - [Setup](#setup)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Dockerize the Application](#dockerize-the-application)
  - [Deploy to Google Cloud Run](#deploy-to-google-cloud-run)
  - [Monitoring and Management](#monitoring-and-management)

## Prerequisites

- Python 3.10+
- Firebase Realtime Database
- Docker
- Google Cloud SDK (if deploying to Google Cloud Run)

## Project Structure
```perl
.
├── rss_deploy.py
├── requirements.txt
├── Dockerfile
└── .env
```

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the project root directory and add your Firebase configuration:
    ```env
    API_KEY=your_firebase_api_key
    AUTH_DOMAIN=your_firebase_auth_domain
    DATABASE_URL=your_firebase_database_url
    STORAGE_BUCKET=your_firebase_storage_bucket
    SERVICE_ACCOUNT=path/to/your/serviceAccountKey.json
    ```

## Usage

To run the script manually:
```sh
python rss_updater.py
```

## Dockerize the Application

    Create a Dockerfile in the project root directory:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Run the command to start the scheduler
CMD ["python", "rss_parser.py"]
```
Create a requirements.txt file with the dependencies:

```txt
beautifulsoup4
feedparser
pyrebase
python-dotenv
requests
apscheduler
pytz
```
Build the Docker image:

```sh
docker build -t rss-parser .
```
Run the Docker container:

```sh
docker run -d rss-parser
```
## Deploy to Google Cloud Run

    Install and configure the Google Cloud SDK:

```sh
gcloud init
gcloud auth configure-docker
```
Build and push the Docker image to Google Container Registry:

```sh
docker tag rss-parser gcr.io/your-project-id/rss-parser
docker push gcr.io/your-project-id/rss-parser
```
Deploy to Google Cloud Run:

```sh
gcloud run deploy rss-parser --image gcr.io/your-project-id/rss-parser --platform managed --region us-central1 --allow-unauthenticated --set-env-vars TZ=Europe/Istanbul
```
## Monitoring and Management

Monitor your microservice and manage logs and performance using the Google Cloud Console.