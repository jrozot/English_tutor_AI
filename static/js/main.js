document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('grammar-form');
    const textInput = document.getElementById('text-input');
    const resultSection = document.getElementById('result-section');
    const correctedText = document.getElementById('corrected-text');
    const translation = document.getElementById('translation');
    const feedback = document.getElementById('feedback');
    const loader = document.getElementById('loader');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const inputText = textInput.value.trim();
        if (!inputText) {
            alert("Por favor, escribe una oración en inglés.");
            return;
        }

        showLoader(true);
        resultSection.style.display = 'none';

        try {
            const response = await fetch('/correct', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: inputText })
            });

            if (!response.ok) {
                throw new Error("Hubo un problema procesando la solicitud.");
            }

            const data = await response.json();

            resultSection.style.display = 'block';
            typeText(correctedText, `✅ ${data.corrected}`);
            typeText(translation, `🗣️ ${data.translated}`);
            typeText(feedback, `💡 ${data.feedback}`);
        } catch (error) {
            alert("Error: " + error.message);
        } finally {
            showLoader(false);
        }
    });

    function showLoader(state) {
        if (loader) {
            loader.style.display = state ? 'inline-block' : 'none';
        }
    }

    function typeText(element, text, delay = 25) {
        element.textContent = '';
        let i = 0;
        const interval = setInterval(() => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
            } else {
                clearInterval(interval);
            }
        }, delay);
    }
});
