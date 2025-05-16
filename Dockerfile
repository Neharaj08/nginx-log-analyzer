# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your script and logs into the container
COPY . .

# Set log file path environment variable (optional)
ENV LOG_FILE=logs/access.log

# Set default command
CMD ["python", "nginx_log_analyzer.py"]
