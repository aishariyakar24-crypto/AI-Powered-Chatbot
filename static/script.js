const chatBox = document.getElementById("chat-box");

const userInput = document.getElementById("user-input");

const sendButton = document.getElementById("send-button");


// Add message to chat box

function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender === "user"
            ? "user-message"
            : "bot-message"
    );


    const contentDiv = document.createElement("div");

    contentDiv.classList.add("message-content");

    contentDiv.textContent = message;


    messageDiv.appendChild(contentDiv);

    chatBox.appendChild(messageDiv);


    // Automatically scroll to bottom

    chatBox.scrollTop = chatBox.scrollHeight;
}


// Send message

async function sendMessage() {

    const message = userInput.value.trim();


    if (message === "") {

        return;

    }


    // Display user message

    addMessage(message, "user");


    // Clear input

    userInput.value = "";


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });


        const data = await response.json();


        // Display bot response

        addMessage(data.response, "bot");


    } catch (error) {

        console.error(error);

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );

    }

}


// Send when button is clicked

sendButton.addEventListener(
    "click",
    sendMessage
);


// Send when Enter is pressed

userInput.addEventListener(
    "keypress",
    function(event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);