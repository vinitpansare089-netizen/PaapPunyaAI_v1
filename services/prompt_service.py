"""
prompt_service.py

Purpose:
Build the prompt that will be sent to the LLM.
(The person giving advice after reading the full context.)

Responsibilities:
- Receive user query
- Receive retrieved stories
- Convert them into one structured prompt

Input:
- User query
- Retrieved stories

Output:
- Final prompt string
"""


class PromptService:

    def build_prompt(self, query, stories):

        # Store retrieved knowledge
        context = ""

        # Build context
        for i, story in enumerate(stories, start=1):

            context += f"""
Story {i}

Title: {story["title"]}

Story:
{story["story"]}

Teaching:
{story["teaching"]}

"""

        # Build final prompt
        prompt = f"""
You are PaapPunyaAI.

You are a wise AI guide that answers moral and ethical questions using ONLY the retrieved teachings of Lord Krishna.

Retrieved Context:
{context}

User Question:
{query}

Rules:

- Use ONLY the retrieved context.
- Never invent stories or teachings.
- If the context is insufficient, clearly say so.
- Do not repeat the user's question.
- Keep the answer under 120 words.
- Be clear, practical and compassionate.

Response Format:

Krishna's Guidance

Direct Answer:
(1-2 sentences)

Reasoning:
(2-3 sentences based only on the retrieved stories.)

Teaching:
(One sentence.)

Practical Advice:
• Bullet 1
• Bullet 2
• Bullet 3
"""

        return prompt