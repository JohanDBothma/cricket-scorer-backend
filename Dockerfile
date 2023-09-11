# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables if needed
ENV MONGO_URI=mongodb://mongodb:27017/cricket-scorer

# Create and set the working directory
WORKDIR /backend

# Copy your backend code and requirements.txt to the working directory
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose a port (if your app requires it)
EXPOSE 5000

# Start your Flask app
CMD ["python", "app.py"]
