import './style.css'

const chat = document.getElementById("chat") as HTMLDivElement;
const askBtn = document.getElementById("askBtn") as HTMLButtonElement;
const questionInput = document.getElementById("question") as HTMLTextAreaElement;

function addMessage(text: string, sender: "user" | "bot"){
  const message = document.createElement("div");
  message.classList.add("message", sender);
  message.textContent = text;
  chat.appendChild(message);
  chat.scrollTop = chat.scrollHeight;
}

askBtn.addEventListener("click", async () => {
  const question = questionInput.value;
  if (!question) return;
  addMessage(question, "user");
  questionInput.value = "";

  addMessage("Thinking...", "bot");

  try{
    const response = await fetch ("http://127.0.0.1:8080/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({question}),
    });
    const data = await response.json();

    chat.lastChild?.remove();
    addMessage(data.answer, "bot");
  } catch (err){
    addMessage("Error connecting to AI backend", "bot");
    console.error(err)
  }
});