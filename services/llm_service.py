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
from ollama import Client

client = Client(host="http://host.docker.internal:11434")


class LLMService:

    def __init__(self, model_name="phi3"):
        self.model_name = model_name
        
    def generate_response(self, prompt):

            response = client.chat(
                 model = self.model_name,
                 messages = [{
                      'role': "user",
                      "content": prompt
                 }],
                  options={
                    "temperature": 0.2,
                    # "num_predict": 120
               }
          )
                    
            
            return response["message"]["content"] 
