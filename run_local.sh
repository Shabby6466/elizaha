#!/bin/bash

# MAHAHA Local Run Script
# Automates starting the chatbot in Docker for local development/testing.

set -e

echo "🚀 Starting MAHAHA locally in Docker..."

# 1. Check if Docker is running
if ! docker info > /dev/null 2>&1; then
  echo "❌ Error: Docker is not running. Please start Docker Desktop and try again."
  exit 1
fi

# 2. Build and start containers
echo "📦 Building and starting containers..."
docker compose up --build -d

# 3. Provide access information
echo ""
echo "✅ MAHAHA is now running!"
echo "------------------------------------------------"
echo "🌐 Frontend: http://localhost:5002"
echo "🧠 Backend API: http://localhost:5001/api/chat"
echo "------------------------------------------------"
echo "To stop the app, run: docker compose down"
echo "To see help, run: docker compose logs -f"
