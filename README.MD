# AI Assistant
![LOGO](LOGO.jpg)


## Description

It is an AI Assistant application that can recognize speech, interact with users, and provide text-to-speech responses. It uses the [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) model for generating text responses.

## Features

- Speech recognition using the Google Speech Recognition API.
- Interaction with the Falcon model for generating responses.
- Text-to-speech conversion using the gTTS (Google Text-to-Speech) library.


## Installation

1. Download the Packages EXE's [ZIP file](https://github.com/RyanBaig/AI-Assistant/raw/master/AI%20Assistant.zip)
2. Unzip the file.
3. Run the **main.exe** file. It will open a console/terminal window.


## Usage

1. Run the unzipped executable or the `main.py` script.

2. When the application is running, speak to the AI Assistant. If your speech contains the word "Omar," the Assistant will send the rest of your speech to the DialoGPT model for generating a response.

3. The generated text response will be displayed, and the AI Assistant will also convert it to speech and play it.

## Configuration

You can customize the behavior of the AI Assistant by modifying the code in `main.py` and the options in `setup.py`.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Test your changes to ensure they work as expected.
5. Submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as you see fit.


