#!/bin/bash

# MAHAHA Deployment Script
# Automates syncing files to a remote server and restarting containers via Docker Compose.

set -e

# --- Configuration ---
REMOTE_USER_HOST=$1
REMOTE_PATH=$2

if [ -z "$REMOTE_USER_HOST" ] || [ -z "$REMOTE_PATH" ]; then
    echo "Usage: ./deploy.sh [user@host] [/path/to/target/directory]"
    echo "Example: ./deploy.sh root@123.456.78.90 /var/www/mahaha"
    exit 1
fi

echo "🚀 Starting deployment of MAHAHA to $REMOTE_USER_HOST..."

# --- Syncing Files ---
# We exclude local development artifacts like venv, node_modules, and git data.
echo "📦 Syncing files..."
rsync -avz --exclude 'venv' \
           --exclude 'node_modules' \
           --exclude '.git' \
           --exclude '.DS_Store' \
           --exclude 'frontend/dist' \
           --exclude 'backend/__pycache__' \
           ./ "$REMOTE_USER_HOST:$REMOTE_PATH"

# --- Remote Orchestration ---
echo "🐳 Restarting containers on remote server..."
ssh "$REMOTE_USER_HOST" "cd $REMOTE_PATH && (docker compose up -d --build || docker-compose up -d --build)"

echo "✅ Deployment successful!"
echo "Your MAHAHA chatbot should be live at the server's IP address on port 3000."
