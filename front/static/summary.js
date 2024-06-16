if (!sessionStorage.getItem('sessionId')) {
    window.location.href = '/login';
// Sorting hostname for API URL
const hostname = window.location.hostname;
let apiUrl;
if (hostname === 'localhost' || hostname === '127.0.0.1') {
    apiUrl = 'http://127.0.0.1:5000/';
} else {
    apiUrl = `http://${hostname}:5000/`;
}
}

function summary() {
    let summaryExtension = document.getElementById('summary-extension');

    if (!document.getElementById('summaryForm')) {
        fetch('summary.html')
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                for (let child of doc.body.children) {
                    document.adoptNode(child);
                    summaryExtension.appendChild(child);
                }

                const userID = sessionStorage.getItem('sessionId');
                // console.log(userID);

                // Getting the form data for construction of dates
                const form = document.getElementById('summaryForm');
                form.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const month = document.getElementById('Month').value;

                    if (!month) {
                        console.log('Month is not selected');
                        return;
                    }
                    //Date construction
                    const start = new Date(month);
                    start.setDate(1);
                    const end = new Date(start);
                    end.setMonth(end.getMonth() + 1);
                    end.setDate(0);

                    //Fomratting the dates to be sent to the server
                    const startDate = start.toISOString().split('T')[0];
                    const endDate = end.toISOString().split('T')[0];

                    // console.log('Start Date:', startDate);
                    // console.log('End Date:', endDate);

                    //jsonify the data
                    const data = { userId: userID, start: startDate, end: endDate};
                    // console.log(data);

                    const response = await fetch(apiUrl + 'apiGetSummary', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                    const result = await response.json();
                    document.getElementById('summaryMessage').innerText = result.message[1];
                    setTimeout(() => {
                        document.getElementById('summaryMessage').innerText = '';
                    }, 2000);
                    setTimeout(() => {
                        document.getElementById('summaryForm').reset();
                    }, 2000);

                });
            });
    }

    summaryExtension.style.display = summaryExtension.style.display === "none" ? "block" : "none";
}
