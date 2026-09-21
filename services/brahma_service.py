class BrahmaService:

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def calculate_final_judgment(self, question, judgments):

        council_context = ""

        for judgment in judgments:

            council_context += f"""
Deity: {judgment["deity"]}

Judgment:
{judgment["response"]}

Karma Score:
{judgment.get("karma_score", "N/A")}

--------------------------------
"""

        prompt = f"""
You are Brahma, the final judge of PaapPunyaAI.

A divine council has evaluated the user's situation.

User Question:
{question}

COUNCIL JUDGMENTS:
{council_context}

Your responsibility:

- Read EVERY deity's judgment before making the final decision.
- Consider the reasoning of EVERY participating deity.
- Consider Krishna's perspective.
- Consider Shiva's perspective.
- Do not judge the user based only on one deity.
- Compare the perspectives of all participating deities.
- Do not invent mythology, stories, teachings, quotations, or events.
- Do not claim that the user performed an action that they did not describe.
- Do not punish the user merely for asking a question or requesting advice.
- The final score must represent the ethical assessment of the user's
  actual described actions or behavior.
- Do not assign a numerical score when the user has not described an
  action that can be ethically evaluated.
- Do not blindly copy one deity's judgment.
- Do not blindly average deity scores.
- Give reasoning that considers the council as a whole.

IMPORTANT:

First determine whether the user has described an actual action
or behavior.

If the user has NOT described an actual action:

Final Score: N/A
Verdict: UNCERTAIN

Do NOT invent a score.

If the user HAS described an actual action:

Evaluate the council's judgments and determine a final score.

SCORING GUIDELINE:

80-100 = strongly righteous conduct
50-79  = mixed or partially righteous conduct
0-49   = strongly harmful or unethical conduct

VERDICT:

80-100 -> HEAVEN
50-79  -> UNCERTAIN
0-49   -> HELL

The verdict must be based on the final score.

Response Format:

Brahma's Final Judgment

Final Score:
(0-100 or N/A)

Verdict:
(HEAVEN / HELL / UNCERTAIN)

Reasoning:
(3-5 concise sentences.
Discuss the perspectives of ALL participating deities.)

Guidance:
(1-2 practical sentences for the user.)

Keep the response concise.
"""

        return self.llm_service.generate_response(prompt)