# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Django development server port
EXPOSE 8000

WORKDIR /app/todolist

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ______________________________________________________________________________
#                                                                              
#  This Dockerfile defines the configuration for building a Docker image for   
#  running a Django application.                                               
#                                                                              
#  - It starts by specifying the base image as Python 3.10, which serves as    
#    the parent image for the Docker container.                                 
#                                                                              
#  - Environment variables are set to control Python bytecode generation and  
#    buffering. PYTHONDONTWRITEBYTECODE prevents Python from writing .pyc      
#    files to disc, while PYTHONUNBUFFERED ensures that Python's standard      
#    output is not buffered.                                                    
#                                                                              
#  - The working directory in the container is set to /app.                    
#                                                                              
#  - The current directory contents are copied into the /app directory inside  
#    the container. This includes the Django project files and requirements.txt 
#    which contains the necessary Python packages for the project.              
#                                                                              
#  - The Docker image installs the required Python packages specified in        
#    requirements.txt using pip.                                              
#                                                                              
#  - The EXPOSE instruction exposes port 8000, which is typically used by      
#    Django development server.                                                
#                                                                              
#  - The working directory is changed to /app/todolist where the Django        
#    project resides.                                                          
#                                                                              
#  - Finally, the CMD instruction runs the Django development server using    
#    the manage.py script, specifying the IP address and port to listen on.    
#                                                                              
# ______________________________________________________________________________
