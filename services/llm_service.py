"""
llm_service.py

Purpose:
Communicate with the LLM through Ollama.

Responsibilities:
- Send prompt to Ollama
- Receive generated response
- Return response

Input:
- Prompt

Output:
- LLM Response 
"""
import ollama


class LLMService:

    def __init__(self, model_name="phi3"):
        self.model_name = model_name
        
    def generate_response(self, prompt):

            response = ollama.chat(
                 model = self.model_name,
                 messages = [{
                      'role': "user",
                      "content": prompt
                 }]
            )

            return response["messages"]["content"]
