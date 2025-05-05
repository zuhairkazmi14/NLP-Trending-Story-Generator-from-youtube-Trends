# Use Python 3.11 base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Run the gRPC server in the background and then the frontend
CMD ["bash", "-c", "python trendstory_server.py & sleep 3 && python frontend.py"]
