document.getElementById('convertBtn').addEventListener('click', async () => {
    const javaCode = document.getElementById('javaInput').value;
    const outputElement = document.getElementById('tsOutput');
    const statusElement = document.getElementById('statusBar');

    if (!javaCode.trim()) {
        statusElement.textContent = "⚠️ Please enter some Java code first.";
        return;
    }

    // UI Loading State
    statusElement.textContent = "⏳ Converting with CodeLlama...";
    outputElement.textContent = "// Processing...";
    document.getElementById('convertBtn').disabled = true;
    document.getElementById('convertBtn').style.opacity = "0.7";

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ java_code: javaCode })
        });

        const data = await response.json();

        if (data.status === 'success') {
            outputElement.textContent = data.ts_code;
            statusElement.textContent = "✅ Conversion Complete.";
            // Trigger Prism Highlight
            Prism.highlightElement(outputElement);

            // Show Save Button
            const saveBtn = document.getElementById('saveBtn');
            saveBtn.style.display = 'inline-flex';
            saveBtn.onclick = async () => {
                const saveStatus = document.getElementById('saveStatus');
                saveStatus.textContent = "Saving...";
                try {
                    const saveResponse = await fetch('/api/save', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ ts_code: data.ts_code })
                    });
                    const saveData = await saveResponse.json();
                    if (saveData.status === 'success') {
                        saveStatus.textContent = `✅ Saved to: ${saveData.path}`;
                    } else {
                        saveStatus.textContent = "❌ Save Failed";
                    }
                } catch (e) {
                    saveStatus.textContent = "❌ Error saving";
                }
            };

        } else {
            outputElement.textContent = "// Error: " + (data.error || "Unknown error");
            statusElement.textContent = "❌ Conversion Failed.";
        }
    } catch (error) {
        outputElement.textContent = "// Network Error: " + error.message;
        statusElement.textContent = "❌ Network Error.";
    } finally {
        document.getElementById('convertBtn').disabled = false;
        document.getElementById('convertBtn').style.opacity = "1";
    }
});
