// server.js - Node.js Real-Time Server
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const axios = require('axios');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, { cors: { origin: "http://localhost:8000" } });

// Basic route for testing server response on the root URL
app.get('/', (req, res) => {
    res.send('Welcome to the real-time server!');
});

// Socket.IO connection handling
io.on('connection', (socket) => {
    console.log('New client connected');
    
    // Emit theme updates every 5 seconds
    const themeInterval = setInterval(async () => {
        try {
            const response = await axios.get('http://localhost:5000/api/themes'); // Check Flask API availability
            socket.emit('updateThemes', response.data);
        } catch (error) {
            console.error("Error fetching themes from Flask:", error.message);
        }
    }, 5000);

    // Clear interval on client disconnect to avoid memory leaks
    socket.on('disconnect', () => {
        clearInterval(themeInterval);
        console.log('Client disconnected');
    });
});

// Start server and listen on port 3000
server.listen(3000, () => {
    console.log("Real-time Node server listening on port 3000");
});
