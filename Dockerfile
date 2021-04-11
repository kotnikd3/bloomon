FROM python:3.8.9-buster

# Make a directory for out application
WORKDIR /src

# Install dependencies

# Copy our source code
COPY /src .

# Run the application
CMD ["python", "API.py"]