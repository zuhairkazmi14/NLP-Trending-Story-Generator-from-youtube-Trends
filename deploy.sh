#!/bin/bash

# Exit immediately on error
set -e

echo "🔧 Setting up Python environment..."

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
env/bin/activate


echo "📦 Installing dependencies..."

# Install requirements
pip install -r requirements.txt

echo "🚀 Starting gRPC server..."

# Run gRPC server in background (assuming grpc_server.py exists)
# Update this line with your actual gRPC server file
python trendstory_server.py 

# Wait a bit to let the gRPC server initialize
sleep 2

echo "🌐 Launching Gradio frontend..."

# Run the Gradio app
python frontend.py
