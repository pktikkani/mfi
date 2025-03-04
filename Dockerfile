# Use Python 3.11 image
FROM python:3.11-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy package.json and install npm dependencies
COPY package.json .
RUN npm install

# Copy the rest of the application
COPY . .

# Build CSS
RUN npm run build:css

# Set environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "main.py"]