# Start with a Python base image
FROM python:3.11-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package.json package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy Python requirements (if you have them)
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

## Build the CSS with Tailwind
#RUN npm run build:css

# Expose the port your app runs on (change if needed)
EXPOSE 5000

# Command to run your app
CMD ["npm", "start"]