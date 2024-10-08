document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    //Stripping empty spaces from the username
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;
    const hostname = window.location.hostname;
    let apiUrl;
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        apiUrl = 'http://127.0.0.1:5000/apiLogin';
    } else {
        apiUrl = `http://${hostname}:5000/apiLogin`;
    }
    // console.log(apiUrl) //Debugging 
    
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
