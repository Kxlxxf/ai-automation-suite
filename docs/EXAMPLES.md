# Examples of Using ChatGPT

This document outlines practical examples of how to use ChatGPT in Python, JavaScript, and Bash scripts.

## Python Example

```python
import openai

# Set up the OpenAI API client
openai.api_key = 'your-api-key'

# Define a function for getting a response from ChatGPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == '__main__':
    user_prompt = 'What are the main features of Python?'
    print(chat_with_gpt(user_prompt))
```

## JavaScript Example

```javascript
const openai = require('openai');

// Set up your OpenAI API key
openai.apiKey = 'your-api-key';

// Function to chat with GPT
async function chatWithGpt(prompt) {
    const response = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: prompt }],
    });
    return response.choices[0].message.content;
}

// Example usage
chatWithGpt('What is the capital of France?')
    .then(response => console.log(response));
```

## Bash Script Example

```bash
#!/bin/bash

# Basic script to interact with ChatGPT API using curl
API_KEY="your-api-key"

function chat_with_gpt() {
    local prompt="$1"
    response=$(curl https://api.openai.com/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $API_KEY" \
        -d '{"model":"gpt-3.5-turbo", "messages":[{"role":"user","content":"'$prompt'"}]}')
    echo $response | jq -r '.choices[0].message.content'
}

# Example usage
chat_with_gpt "Tell me a joke!"
```

Replace `'your-api-key'` with your actual OpenAI API key in the examples above.