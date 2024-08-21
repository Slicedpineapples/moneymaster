document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    //Stripping empty spaces from the username
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    // Determine the base URL based on the hostname
// Get the hostname and IP address
    const hostname = window.location.hostname;

    // Define your local network IP address (e.g., 192.168.x.x)
    const localNetworkIp = '192.168.x.x';

    // Set the API URL based on the hostname
    if (hostname === 'localhost' || hostname === '127.0.0.1' || hostname === localNetworkIp) {
        // Use the localhost or local network IP for development
        apiUrl = `http://${localNetworkIp}:5000/apiLogin`;
    } else {
        // Use the server's IP address or hostname for production
        apiUrl = `http://${hostname}:5000/apiLogin`;
        console.log(apiUrl);
    }

    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    
    const result = await response.json();
    // console.log(hostname, apiUrl, result) // Debugging
    const userID = result.message[0];
    if (result.message[0]!==null){
        sessionStorage.setItem('sessionId', userID);
        sessionStorage.setItem('userName', username);
        sessionStorage.setItem('email', result.message[1]);
        document.getElementById('loginMessage').innerText = result.message[2];
        await new Promise(resolve => setTimeout(resolve, 1000));
        window.location.href = 'home.html';
    } else {
        document.getElementById('loginMessage').innerText = result.message[1];
        await new Promise(resolve => setTimeout(resolve, 1000));
        window.location.href = 'login.html';
    }
});
