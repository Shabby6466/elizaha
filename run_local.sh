#!/bin/bash

# MAHAHA Local Run Script
# Automates starting the chatbot in Docker for local development/testing.
# Includes logic to install Docker if missing on macOS.

set -e

echo "🚀 Starting MAHAHA locally in Docker..."

# 1. Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "🔍 Docker not found. Attempting to install..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "❌ Homebrew not found. Please install Homebrew first: https://brew.sh/"
            exit 1
        fi
        echo "🍺 Installing Docker Desktop via Homebrew..."
        brew install --cask docker
        echo "✅ Docker Desktop installed. Please open it from your Applications folder."
    else
        echo "❌ Docker is not installed. Please install it for your OS: https://docs.docker.com/get-docker/"
        exit 1
    fi
fi

# 2. Check if Docker daemon is running
echo "🐳 Checking if Docker daemon is running..."
if ! docker info > /dev/null 2>&1; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "🏃 Starting Docker Desktop..."
        open -a Docker
        echo "⏳ Waiting for Docker to start (this may take a minute)..."
        until docker info > /dev/null 2>&1; do
            sleep 5
            echo -n "."
        done
        echo ""
    else
        echo "❌ Docker daemon is not running. Please start it and try again."
        exit 1
    fi
fi

# 3. Build and start containers
echo "📦 Building and starting containers..."
docker compose up --build -d

# 4. Provide access information
echo ""
echo "✅ MAHAHA is now running!"
echo "------------------------------------------------"
echo "🌐 Frontend: http://localhost:5002"
echo "🧠 Backend API: http://localhost:5001/api/chat"
echo "------------------------------------------------"
echo "To stop the app, run: docker compose down"
echo "To see logs, run: docker compose logs -f"
