# Use the official Python image as the base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the script and any necessary files to the working directory
COPY server.py .
COPY loading.py .

# Install the required dependencies
RUN pip install --no-cache-dir gevent

# Expose the port that the server will listen on
EXPOSE 44445

# Run the script when the container starts
CMD ["python", "server.py"]
