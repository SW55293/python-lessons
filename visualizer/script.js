function submitCode() {
    const code = document.getElementById('codeInput').value;
    fetch('/run_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({code: code}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').textContent = data.output;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
