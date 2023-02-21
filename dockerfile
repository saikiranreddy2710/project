# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app/app
COPY ./app /app/app

# Copy the static files into the container at /app/static
COPY ./static /app/static

# Copy the templates into the container at /app/templates
COPY ./templates /app/templates

# Expose port 80 for the container
EXPOSE 80

# Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
