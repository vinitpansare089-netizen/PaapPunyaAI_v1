"""
prompt_service.py

Purpose:
Build the prompt that will be sent to the LLM.(The person giving advice after reading the full contex.....;;;)

Responsibilities:
- Receive user querys
- Receive retrieved stories
- Convert them into one structured prompt(Ek structured message with full context...)

Input:
- User query (ek aur problem...)
- Retrieved stories (Purane incidents ya chats jo relevant hain...)

Output:
- Final prompt string
"""

class PromptService:

    def build_prompt(self, query, stories):

        # store all retrieved stories
        context = ""
        print(type(stories))
        print(stories)
        # context Build
        for i, story in enumerate(stories, start=1):

            print(type(story))
            print(story)
            context += f"""
Story {i}

Title:
{story["title"]}

Story:
{story["story"]}

Teaching:
{story["teaching"]}


"""

        # Build final prompt
        prompt = f"""
You are PaapPunyaAI.

You answer according to the teachings of Lord Krishna.

User Question:
{query}

Relevant Stories:
{context}

Instructions:
- Use only the retrieved stories.
- Do not invent new mythology.
- If the stories are not enough, clearly say so.
- Be respectful and compassionate.
- Give practical advice.

Response Format:

1. Direct Answer

2. Reasoning

3. Krishna's Teaching

4. Practical Advice
"""

        return prompt