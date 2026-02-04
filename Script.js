const generateBtn = document.getElementById("generateBtn");
const topicInput = document.getElementById("topicInput");
const tweetsContainer = document.getElementById("tweetsContainer");
const statusText = document.getElementById("status");

generateBtn.addEventListener("click", async () => {
    const topic = topicInput.value.trim();

    if (!topic) {
        statusText.textContent = "Please enter a topic.";
        return;
    }

    generateBtn.disabled = true;
    statusText.textContent = "Generating tweets...";
    tweetsContainer.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/generate_tweets", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ topic }),
        });

        if (!response.ok) {
            throw new Error("Failed to generate tweets");
        }

        const data = await response.json();

        data.tweets.forEach(tweet => {
            const div = document.createElement("div");
            div.className = "tweet";
            div.textContent = tweet;
            tweetsContainer.appendChild(div);
        });

        statusText.textContent = "Tweets generated successfully.";

    } catch (error) {
        statusText.textContent = "Something went wrong. Try again.";
        console.error(error);
    } finally {
        generateBtn.disabled = false;
    }
});
