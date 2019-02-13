# Using the official Python 3.7 image
FROM python:3.7

# Set the Work Directory
WORKDIR /usr/src/app

# Copy over the requirements.txt file
COPY ./requirements.txt /usr/src/app/requirements.txt

# Install the project's dependencies
RUN pip install -r requirements.txt

# Copy the project codes into the Work Directory
COPY . /usr/src/app

# Expose port so that it's accessible to external connections
EXPOSE 5000

# Run the Flask application
CMD ["python", "manage.py", "runserver"]