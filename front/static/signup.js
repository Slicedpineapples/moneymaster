document.getElementById('signupForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;

    //Determine the base URL based on the hostname
    const hostname = window.location.hostname;
    let apiUrl;
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        apiUrl = 'http://127.0.0.1:5000/apiSignup';
    } else {
        // Change this to your server's IP address or hostname
        apiUrl = `http://${hostname}:5000/apiSignup`;
    }
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, phone, password })
    });

    const result = await response.json();
    if (result.message === 'User created successfully!') {
        document.getElementById('signupMessage').innerText = result.message;
        await new Promise(resolve => setTimeout(resolve, 2000));
        window.location.href = 'login.html';
    }
});
