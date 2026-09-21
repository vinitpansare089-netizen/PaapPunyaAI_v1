import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [judgments, setJudgments] = useState([]);
  const [finalJudgment, setFinalJudgment] = useState("");
  const [loading, setLoading] = useState(false);

  const askCouncil = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setJudgments([]);
    setFinalJudgment("");

    try {
      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      // Show each deity one by one
      for (let i = 0; i < data.judgments.length; i++) {
        await new Promise((resolve) =>
          setTimeout(resolve, i === 0 ? 0 : 4000)
        );

        setJudgments((previous) => [
          ...previous,
          data.judgments[i],
        ]);
      }

      // Brahma appears after all deities
      await new Promise((resolve) => setTimeout(resolve, 2000));

      setFinalJudgment(data.final_judgment);

    } catch (error) {
      console.error(error);
      alert("Unable to connect to PaapPunyaAI backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <header>
        <h1>PaapPunyaAI</h1>
        <p>The Divine Ethical Council</p>
      </header>

      <main>

        <section className="question-box">

          <textarea
            placeholder="Confess your actions or ask your question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button
            onClick={askCouncil}
            disabled={loading}
          >
            {loading ? "The Council is deliberating..." : "Ask the Council"}
          </button>

        </section>

        {judgments.length > 0 && (
          <section className="council">

            <h2>Divine Council</h2>

            {judgments.map((judgment, index) => (

              <div
                className="deity-card"
                key={index}
              >

                <h3>{judgment.deity}</h3>

                <p>{judgment.response}</p>

              </div>

            ))}

          </section>
        )}

        {finalJudgment && (
          <section className="brahma-card">

            <h2>Brahma's Final Judgment</h2>

            <p>{finalJudgment}</p>

          </section>
        )}

      </main>

    </div>
  );
}


export default App;