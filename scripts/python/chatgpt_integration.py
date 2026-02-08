import openai
import json

class ChatGPTIntegration:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_code(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def analyze_code(self, code):
        prompt = f"Analyze the following code:\n{code}\nProvide feedback and suggest improvements."
        return self.generate_code(prompt)

    def generate_documentation(self, code):
        prompt = f"Generate documentation for the following code:\n{code}
        "
        return self.generate_code(prompt)

    def save_results(self, filename, results):
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)

# Example usage:
# integration = ChatGPTIntegration(api_key='YOUR_API_KEY_HERE')
# code = "print('Hello, World!')"
# feedback = integration.analyze_code(code)
# integration.save_results('results.json', feedback)
