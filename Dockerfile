# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Git and system dependencies required for mysqlclient
RUN apt-get update && \
    apt-get install -y \
    git \
    build-essential \
    pkg-config \
    libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Clone the repository directly into /app
RUN git clone https://github.com/OrphLab/performaq.git . && \
    git pull origin main

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies including gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose the port your application will run on
EXPOSE 9090

# Specify the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:9090", "performaq.wsgi:application"]
