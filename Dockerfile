# Use a Python base image that is known to be compatible with TensorFlow 2.16.x
# Python 3.12 is the latest fully supported by TF 2.16.x. 
# If 3.12 doesn't work, try python:3.11-slim-buster or python:3.10-slim-buster
FROM python:3.12-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
# This step should be done before copying the rest of the app for better Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Streamlit runs on (default is 8501)
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
