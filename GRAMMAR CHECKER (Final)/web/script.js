document.getElementById("grammarForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let userText = document.getElementById("user_text").value;

    fetch("/check_grammar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_text: userText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("corrected_text").value = data.corrected_text.replace(/^Here's the corrected text:\s*/, '');
    })
    .catch(error => console.error("Error:", error));
});
