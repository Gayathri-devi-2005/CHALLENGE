# Use slim Python image and force AMD64 platform
FROM --platform=linux/amd64 python:3.10-slim

# Set work directory
WORKDIR /app

# Copy only what's needed first for faster caching
COPY requirements.txt .

# Install dependencies (add --no-cache-dir to speed up without caching)
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Default command
CMD ["python", "main.py"]
