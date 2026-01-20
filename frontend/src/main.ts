import './style.css'

const askBtn = document.getElementById("askBtn") as HTMLButtonElement;
const questionInput = document.getElementById("question") as HTMLTextAreaElement;
const answerBox = document.getElementById("answer") as HTMLPreElement;

askBtn.addEventListener("click", async () => {
  const question = questionInput.value;

  answerBox.textContent = "Thinking...";

  try{
    const response = await fetch ("http://127.0.0.1:8080/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({question})
    });
    const data = await response.json()
    answerBox.textContent = data.answer;
  } catch (err){
    answerBox.textContent = "Error connecting to backend";
    console.error(err)
  }
});