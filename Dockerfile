# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install PDM
RUN pip install pdm

# Use PDM to install project dependencies
RUN pdm add django

# Expose the port that Django will run on
EXPOSE 8000

# Start the Django development server with binding to 0.0.0.0
CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]