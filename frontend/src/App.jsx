import { useState } from "react";
import "./App.css";

const DEITIES = [
  {
    name: "Krishna",
    symbol: "ॐ",
    subtitle: "Dharma • Wisdom • Detachment",
    description: "The voice of righteous action and clarity.",
  },
  {
    name: "Shiva",
    symbol: "ॐ",
    subtitle: "Transformation • Discipline • Detachment",
    description: "The voice of inner transformation and ego.",
  },
  {
    name: "Asura",
    symbol: "◈",
    subtitle: "Ambition • Power • Desire",
    description: "The voice that challenges conventional morality.",
  },
];

function parseResponse(text) {
  if (!text) return {};

  const getSection = (name, nextSections = []) => {
    const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

    let pattern = `${escaped}:\\s*([\\s\\S]*?)`;

    if (nextSections.length > 0) {
      pattern += `(?=\\n\\n(?:${nextSections.join("|")}):|$)`;
    } else {
      pattern += "$";
    }

    const match = text.match(new RegExp(pattern, "i"));

    return match ? match[1].trim() : "";
  };

  return {
    directAnswer: getSection("Direct Answer", [
      "Reasoning",
      "Teaching",
      "Karma Score",
      "Practical Advice",
    ]),

    reasoning: getSection("Reasoning", [
      "Teaching",
      "Karma Score",
      "Practical Advice",
    ]),

    teaching: getSection("Teaching", [
      "Karma Score",
      "Practical Advice",
    ]),

    karmaScore: getSection("Karma Score", [
      "Practical Advice",
    ]),

    practicalAdvice: getSection("Practical Advice"),
  };
}

function Thinking({ deity }) {
  return (
    <div className="thinking">
      <div className="thinking-orbit">
        <span></span>
        <span></span>
        <span></span>
      </div>

      <div>
        <div className="thinking-title">
          {deity.toUpperCase()} IS CONTEMPLATING
        </div>

        <div className="thinking-subtitle">
          Searching the ancient wisdom...
        </div>
      </div>
    </div>
  );
}

function DeityCard({ deity, judgment, thinking }) {
  const parsed = judgment ? parseResponse(judgment.response) : {};

  return (
    <article className={`deity-card ${deity.name.toLowerCase()}`}>
      <div className="card-top">

        <div className="deity-emblem">
          <span>{deity.symbol}</span>
        </div>

        <div className="deity-heading">
          <div className="deity-name">
            {deity.name}
          </div>

          <div className="deity-subtitle">
            {deity.subtitle}
          </div>
        </div>

        <div className="card-status">
          {thinking ? "CONTEMPLATING" : "DELIVERED"}
        </div>
      </div>

      <div className="divider"></div>

      {thinking ? (
        <Thinking deity={deity.name} />
      ) : judgment ? (
        <div className="deity-content">

          {parsed.directAnswer && (
            <section className="wisdom-section">
              <span className="section-label">
                DIRECT ANSWER
              </span>

              <p>{parsed.directAnswer}</p>
            </section>
          )}

          {parsed.reasoning && (
            <section className="wisdom-section">
              <span className="section-label">
                REASONING
              </span>

              <p>{parsed.reasoning}</p>
            </section>
          )}

          {parsed.teaching && (
            <section className="teaching-box">
              <span className="section-label">
                TEACHING
              </span>

              <p>"{parsed.teaching}"</p>
            </section>
          )}

          {parsed.practicalAdvice && (
            <section className="wisdom-section">
              <span className="section-label">
                PRACTICAL ADVICE
              </span>

              <p>{parsed.practicalAdvice}</p>
            </section>
          )}

        </div>
      ) : null}
    </article>
  );
}

function App() {
  const [question, setQuestion] = useState("");
  const [judgments, setJudgments] = useState([]);
  const [thinkingIndex, setThinkingIndex] = useState(-1);
  const [finalJudgment, setFinalJudgment] = useState("");
  const [loading, setLoading] = useState(false);

  const askCouncil = async () => {
    if (!question.trim() || loading) return;

    setLoading(true);
    setJudgments([]);
    setFinalJudgment("");
    setThinkingIndex(0);

    try {
      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          question: question.trim(),
        }),
      });

      if (!response.ok) {
        throw new Error(`Backend returned ${response.status}`);
      }

      const data = await response.json();

      /*
       * The backend returns all judgments together.
       *
       * We reveal them progressively so the experience
       * feels like a council deliberation.
       */

      for (let i = 0; i < data.judgments.length; i++) {

        setThinkingIndex(i);

        // Thinking time before each deity speaks
        await new Promise((resolve) =>
          setTimeout(resolve, 3500)
        );

        setJudgments((previous) => [
          ...previous,
          data.judgments[i],
        ]);

        // Small pause before next deity
        await new Promise((resolve) =>
          setTimeout(resolve, 1800)
        );
      }

      setThinkingIndex(-1);

      // Brahma preparation
      await new Promise((resolve) =>
        setTimeout(resolve, 2500)
      );

      setFinalJudgment(data.final_judgment);

    } catch (error) {
      console.error("Council error:", error);

      alert(
        `Unable to connect to PaapPunyaAI backend.\n\n${error.message}`
      );
    } finally {
      setThinkingIndex(-1);
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <div className="dust dust-one"></div>
      <div className="dust dust-two"></div>
      <div className="dust dust-three"></div>

      <header className="hero">

        <div className="brand-symbol">
          ॐ
        </div>

        <div className="eyebrow">
          TRINOVOUS • ETHICAL REASONING SYSTEM
        </div>

        <h1>
          Paap<span>Punya</span>AI
        </h1>

        <p className="hero-title">
          THE DIVINE ETHICAL COUNCIL
        </p>

        <p className="hero-description">
          Present your dilemma before the council.
          <br />
          Three perspectives. One final judgment.
        </p>

      </header>

      <main>

        <section className="question-section">

          <div className="question-label">
            YOUR DILEMMA
          </div>

          <div className="question-box">

            <textarea
              value={question}
              maxLength={500}
              placeholder="Speak your dilemma..."
              onChange={(e) =>
                setQuestion(e.target.value)
              }
              disabled={loading}
            />

            <div className="question-footer">

              <span>
                {question.length}/500
              </span>

              <button
                onClick={askCouncil}
                disabled={!question.trim() || loading}
              >
                {loading
                  ? "THE COUNCIL DELIBERATES"
                  : "ASK THE COUNCIL"}
              </button>

            </div>

          </div>

        </section>

        {(loading || judgments.length > 0) && (
          <section className="council-section">

            <div className="section-heading">

              <div>
                <span className="eyebrow">
                  THE COUNCIL
                </span>

                <h2>
                  Three perspectives
                </h2>
              </div>

              <div className="council-line"></div>

            </div>

            <div className="deity-grid">

              {DEITIES.map((deity, index) => {

                const judgment = judgments.find(
                  (item) =>
                    item.deity.toLowerCase() ===
                    deity.name.toLowerCase()
                );

                const isThinking =
                  thinkingIndex === index &&
                  !judgment;

                return (
                  <DeityCard
                    key={deity.name}
                    deity={deity}
                    judgment={judgment}
                    thinking={isThinking}
                  />
                );
              })}

            </div>

          </section>
        )}

        {finalJudgment && (
          <section className="brahma-section">

            <div className="brahma-symbol">
              ॐ
            </div>

            <div className="eyebrow">
              THE FINAL WORD
            </div>

            <h2>
              Brahma's Judgment
            </h2>

            <div className="brahma-divider"></div>

            <div className="brahma-content">
              {finalJudgment}
            </div>

          </section>
        )}

      </main>

      <footer>
        <span>PAAPPUNYAAI</span>
        <span>THE COUNCIL IS LISTENING</span>
      </footer>

    </div>
  );
}

export default App;