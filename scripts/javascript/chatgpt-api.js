// Importing the necessary libraries
const axios = require('axios');

// Function to generate prompt using ChatGPT API
async function generatePrompt(prompt){
    const apiKey = 'YOUR_API_KEY'; // Replace with your actual API key
    const endpoint = 'https://api.openai.com/v1/chat/completions';

    // Constructing the request payload
    const data = {
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 100,
    };

    try {
        const response = await axios.post(endpoint, data, {
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data.choices[0].message.content;
    } catch (error) {
        console.error('Error generating prompt:', error);
        throw error;
    }
}

// Example usage
generatePrompt('Write a JavaScript function to reverse a string.')
    .then(response => {
        console.log('Generated code:', response);
    })
    .catch(error => {
        console.error('Error:', error);
    });