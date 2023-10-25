import os
import requests
import speech_recognition as sr
from gtts import gTTS

try:
    # Function to send a query to the DialoGPT model using the Hugging Face API
    def query(payload):
        """
        Query the API with the given payload and return the generated text.
        
        Parameters:
            payload (dict): The payload containing the input data for the API.
            
        Returns:
            str: The generated text from the API response.
        """
        # Define the API token and model URL
        api_token = "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"
        api_url = f"https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
        
        # Set the headers with the API token
        headers = {"Authorization": f"Bearer {api_token}"}
        
        # Send a POST request with the payload to the API
        response = requests.post(api_url, headers=headers, json=payload)
        
        # Get the generated text from the API response
        output = response.json()["generated_text"]
        
        return output

    # Function to process speech input
    def process_speech():
        """
            Process speech input by:
            - Creating a speech recognizer
            - Recording audio from a microphone
            - Recognizing speech using Google's speech recognition
            - Sending the detected speech to the DialoGPT model for generating a response
            - Printing the generated text
            - Converting the generated text to speech and saving it as an audio file
            - Playing the generated audio
        """
        # Create a speech recognizer
        recognizer = sr.Recognizer()
        
        # Use a microphone as the audio source
        with sr.Microphone() as source:
            print("Listening...")
            # Record audio from the microphone
            audio = recognizer.listen(source)
    
        # Recognize speech using Google's speech recognition
        print("Detected speech:", recognizer.recognize_google(audio))
        detected_speech: str = recognizer.recognize_google(audio)
        if "omar" in detected_speech.lower():
            print("sent: ", detected_speech.lower().replace("omar", ""))

            # Send the detected speech to the DialoGPT model for generating a response
            response = query(detected_speech.lower().replace("omar", ""))

            # Print the generated text
            print("Generated text:", response)

            # Convert the generated text to speech and save it as an audio file
            gTTS(text=response, lang='en').save("audio.mp3")

            # Play the generated audio
            os.system("start audio.mp3")
        else:
            return

except Exception as e:
    print("An error occurred:", e)


# Call the process_speech function to start the speech processing
process_speech()
