if (!sessionStorage.getItem('sessionId')) {
    window.location.href = '/login';
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
                console.log(userID);

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
                    const data = { start: startDate, end: endDate, userID };
                    console.log(data);


                });
            });
    }

    summaryExtension.style.display = summaryExtension.style.display === "none" ? "block" : "none";
}
