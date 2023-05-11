# Use a lightweight base image
FROM python:3.9-slim-buster

# Set the working directory to the root directory of your application
WORKDIR /ClientServerWeatherVue

# Copy the application files to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose the port used by the gRPC server
EXPOSE 50051

# Set environment variables
ENV PYTHONUNBUFFERED=TRUE

# Specify the command to start the gRPC server
CMD ["python", "grpc_server.py"]