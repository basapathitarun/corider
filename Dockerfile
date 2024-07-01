# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment and install any needed packages specified in requirements.txt
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to ensure the venv is activated
ENV PATH="/app/venv/bin:$PATH"

# Run run.py when the container launches
CMD ["python", "run.py"]
