import openai
import re

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

def plagiarism_detector(original_text, suspect_text):
    # Remove special characters and extra spaces from the text
    original_text = re.sub('[^a-zA-Z0-9 \n\.]', '', original_text)
    suspect_text = re.sub('[^a-zA-Z0-9 \n\.]', '', suspect_text)

    # Calculate the similarity score between the two texts
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Compare the similarity between the following two pieces of text:\n\nOriginal text: {original_text}\n\nSuspect text: {suspect_text}\n\n",
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.0
    )

    # Check the similarity score and return the result
    similarity_score = float(response.choices[0].text.strip())
    if similarity_score > 0.8:
        return "Plagiarism detected!"
    else:
        return "No plagiarism detected."
