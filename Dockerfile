FROM python:3.12-slim  
# Use a slim version of python because the full version is too large for free tier
WORKDIR /app 
# Move into the /app directory in the container, if it doesn't exist create it
COPY requirements.txt . 
# Copy the requirements.txt file into the containers app directory
RUN pip install --no-cache-dir -r requirements.txt 
# Install the dependencies listed in requirements.txt
COPY app.py . 
# Copy the app.py file into the containers app directory
EXPOSE 5000 
# Documents that the container listens on port 5000 at runtime, this is the port that Flask will run on
# CMD ["python", "app.py"] (we are changing from this to:)
    # Run the app.py file when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
# Before: Request → Flask's built-in test server → Flask app
# Now: Request → Gunicorn → Flask app



#So the dockerfile 1. create linux image (with python installed) 2. make a folder called app in container's seperate file system  3. copies requirements.txt to docker's app filesystem 3. install packages listed in requirments.txt 4. copy app into app folder (conatiner's filesystem) 5. Shows which port will recieve traffic 6. execute app when container starts