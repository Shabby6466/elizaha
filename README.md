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

## Communication Guide: Getting the Most Out of MAHAHA

MAHAHA is designed to be more than a simple chatbot; it uses specialized therapeutic techniques to help you process your thoughts.

### 1. Solution-Focused (SFBT)
If you are feeling stuck, MAHAHA will try to help you visualize a future where the problem is solved.
- **Try saying**: *"I need a miracle"*, *"What if things got better?"*, or *"I have a goal to..."*
- **The Goal**: To shift your focus from the "why" of the problem to the "how" of the solution.

### 2. Empathetic Reflection (Rogerian)
MAHAHA listens to your emotions and reflects them back to help you find your own answers.
- **Try saying**: *"I feel anxious about my job"*, *"I am sad because..."*, or *"I don't know who I am anymore."*
- **The Goal**: To provide a non-judgmental space where you feel heard, allowing you to explore your feelings deeper.

### 3. Handling Generalizations
When you use words like "always" or "never," MAHAHA might challenge them to help you find exceptions.
- **Try saying**: *"Everyone hates me"* or *"I always fail."*
- **The Goal**: To break negative thought patterns and see the nuances in your life.

### Tips for Better Conversations
- **Be Specific**: The more detail you provide about your feelings, the more targeted MAHAHA's reflections will be.
- **Be Open**: Treat the chat as a private journal. MAHAHA is here to explore, not to judge.
- **Type "bye"**: When you are ready to wrap up your session.

## Usage
- Share your thoughts in the chat input.
- MAHAHA uses 50 sophisticated rules to help you find solutions to your challenges.
- Type **"bye"** to conclude the session.
