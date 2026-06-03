document.addEventListener('DOMContentLoaded', () => {
    // Check bot webhook status (optional)
    fetch('/api/bot')
        .then(res => res.text())
        .then(data => {
            const statusDiv = document.getElementById('botStatus');
            if (data.includes('running')) {
                statusDiv.textContent = '✅ Online';
                statusDiv.className = 'status-badge online';
            } else {
                statusDiv.textContent = '❌ Offline';
                statusDiv.className = 'status-badge offline';
            }
        })
        .catch(() => {
            document.getElementById('botStatus').textContent = '⚠️ Unknown';
        });

    // Test webhook endpoint
    document.getElementById('testWebhookBtn').addEventListener('click', async () => {
        const response = await fetch('/api/bot', { method: 'GET' });
        const text = await response.text();
        alert(`Webhook response: ${text}`);
    });

    // Re‑set webhook (calls setup endpoint)
    document.getElementById('setWebhookBtn').addEventListener('click', async () => {
        const response = await fetch('/api/setup');
        const text = await response.text();
        alert(text);
    });
});
