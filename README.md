# MAHAHA Chatbot

A premium full-stack MAHAHA chatbot featuring a Python Flask backend and a modern, glassmorphic React UI.

## Features
- **MAHAHA Knowledge Base**: 50 advanced therapeutic patterns focused on Rogerian and Solution-Focused Brief Therapy (SFBT).
- **React Frontend**: Built with Vite, Framer Motion for animations, and Lucide-React for iconography.
- **Premium UI**: Dark mode with dynamic glassmorphism effects and smooth transitions.
- **Dockerized**: Fully containerized for one-command deployment.

## Project Structure
- `backend/`: Flask server with 50-rule MAHAHA knowledge base.
- `frontend/`: React application (modern UI).
- `docker-compose.yml`: Orchestration for both services.

## Running the Application (Recommended: Docker)

### Local Deployment
The easiest way to run the entire stack locally is using Docker Compose:

1. **Ensure Docker is running** on your machine.
2. **From the project root, run**:
   ```bash
   docker-compose up --build
   ```
3. **Access the chatbot**:
   - **Frontend**: [http://localhost:5002](http://localhost:5002)
   - **Backend API**: [http://localhost:5001/api/chat](http://localhost:5001/api/chat)

### Remote Deployment (SSH)
If you have an SSH server with Docker and Docker Compose installed, you can use the automated deployment script:

```bash
./deploy.sh user@your-server-ip /path/to/remote/directory
```
This script will:
- Sync your local project files to the server using `rsync`.
- Rebuild and restart the containers on the remote server via `ssh`.

## Manual Setup (Development)

### 1. Backend
```bash
cd backend
# Create and activate venv
python3 -m venv venv
source venv/bin/activate
# Install deps
pip install -r requirements.txt
# Run
python app.py
```

### 2. Frontend
```bash
cd frontend
# Install deps
npm install
# Run dev server
npm run dev
```

## Usage
- Share your thoughts in the chat input.
- MAHAHA uses 50 sophisticated rules to help you find solutions to your challenges.
- Type **"bye"** to conclude the session.
