import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Send, User, Bot, Sparkles } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import './App.css';

const API_URL = 'http://localhost:5001/api/chat';

function App() {
  const [messages, setMessages] = useState([
    { text: "Hello. I am MAHAHA. How are you feeling today?", sender: 'bot' }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = input.trim();
    setMessages(prev => [...prev, { text: userMsg, sender: 'user' }]);
    setInput('');

    if (userMsg.toLowerCase() === 'bye') {
      setMessages(prev => [...prev, { text: "Goodbye! I am always here if you need to talk.", sender: 'bot' }]);
      return;
    }

    setIsTyping(true);

    try {
      const response = await axios.post(API_URL, { message: userMsg });
      
      // Artificial delay for feel
      setTimeout(() => {
        setIsTyping(false);
        setMessages(prev => [...prev, { text: response.data.response, sender: 'bot' }]);
      }, 1000);
    } catch (error) {
      console.error('Error connecting to MAHAHA:', error);
      setIsTyping(false);
      setMessages(prev => [...prev, { text: "I'm having trouble connecting to my thoughts right now. Please try again in a moment.", sender: 'bot' }]);
    }
  };

  return (
    <div className="app-wrapper">
      <div className="background-blobs">
        <div className="blob blob-1"></div>
        <div className="blob blob-2"></div>
        <div className="blob blob-3"></div>
      </div>

      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="chat-container"
      >
        <header className="chat-header">
          <div className="header-left">
            <div className="status-dot"></div>
            <h1>MAHAHA</h1>
          </div>
          <Sparkles className="text-blue-400 opacity-50" size={24} />
        </header>

        <main className="chat-messages">
          <AnimatePresence>
            {messages.map((msg, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: msg.sender === 'user' ? 20 : -20 }}
                animate={{ opacity: 1, x: 0 }}
                className={`message ${msg.sender === 'user' ? 'user-message' : 'bot-message'}`}
              >
                {msg.text}
              </motion.div>
            ))}
          </AnimatePresence>
          
          {isTyping && (
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="typing-indicator"
            >
              <div className="dot"></div>
              <div className="dot"></div>
              <div className="dot"></div>
            </motion.div>
          )}
          <div ref={messagesEndRef} />
        </main>

        <form className="chat-input-area" onSubmit={handleSend}>
          <div className="input-wrapper">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Share what's on your mind..."
              autoComplete="off"
            />
            <button type="submit" className="send-button" disabled={!input.trim()}>
              <Send size={24} />
            </button>
          </div>
        </form>
      </motion.div>
    </div>
  );
}

export default App;
