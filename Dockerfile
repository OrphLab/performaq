# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Git (required for cloning repositories)
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Clone the repository directly into /app
RUN git clone https://github.com/OrphLab/performaq.git . && \
    git pull origin main

# Install the Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose the port your application will run on
EXPOSE 9090

# Specify the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:9090", "performaq.wsgi:application"]
