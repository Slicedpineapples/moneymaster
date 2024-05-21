document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Determine the base URL based on the hostname
    const hostname = window.location.hostname;
    let apiUrl;
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        apiUrl = 'http://127.0.0.1:5000/apiLogin';
    } else {
        // Change this to your server's IP address or hostname
        apiUrl = `http://${hostname}:5000/apiLogin`;
    }
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    
    const result = await response.json();
    console.log(hostname, apiUrl, result)
    const userID = result.message[0];
    if (result.message[1] === 'Login successful!') {
        sessionStorage.setItem('sessionId', userID);
        sessionStorage.setItem('userName', username);
        document.getElementById('loginMessage').innerText = result.message[1];
        await new Promise(resolve => setTimeout(resolve, 2000));
        window.location.href = 'home.html';
    } else {
        document.getElementById('loginMessage').innerText = result.message[1];
        await new Promise(resolve => setTimeout(resolve, 2000));
        window.location.href = 'login.html';
    }
});
