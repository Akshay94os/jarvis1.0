![Project Banner](ironsnap2.gif)

# Jarvis 1.0: Your Desktop Voice Assistant

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Status: Active](https://img.shields.io/badge/status-active-success.svg)](https://github.com/Akshay94os/jarvis1.0)

## Overview

Jarvis 1.0 is a desktop voice assistant designed to simplify your daily computer interactions through natural language commands. It acts as your personal digital companion, capable of performing a wide array of tasks from sending messages and setting alarms to providing news updates and playing games, all controlled by your voice.

This project aims to demonstrate the power of voice-controlled automation for everyday desktop use, making your computing experience more intuitive and hands-free. It's ideal for users looking for a personalized and efficient way to interact with their system.

## Features

Jarvis 1.0 comes packed with a variety of functionalities to assist you:

### Core Voice Interaction
*   **Voice Commands**: Understands and responds to natural language voice commands.
*   **Greetings**: Greets you personally based on the time of day.
*   **Text-to-Speech**: Responds verbally to your queries and commands.

### Productivity & Utility
*   **Web Search**: Quickly search the web for information using your voice.
*   **News Reader**: Reads out the latest news headlines and summaries.
*   **Calculator**: Performs basic arithmetic calculations.
*   **Dictionary**: Look up definitions of words.
*   **Translator**: Translates spoken or typed phrases into other languages.
*   **Alarm Clock**: Set voice-activated alarms with custom messages.
*   **Remember Me**: Jot down notes or reminders that Jarvis can recall later.
*   **Focus Mode**: Helps you concentrate by managing distractions (e.g., blocking certain apps/websites).
*   **System Commands**: Execute basic system operations (e.g., opening applications).

### Communication & Entertainment
*   **WhatsApp Messaging**: Send messages to your contacts via WhatsApp using voice commands.
*   **Music Player**: Play local music files (e.g., `music.mp3`).
*   **Games**: Engage in simple, voice-controlled games.

### Advanced Capabilities
*   **Facial Recognition**: Potentially for user authentication or personalized interactions.
*   **Keyboard Control**: Simulate keyboard inputs for various tasks.

## Tech Stack

Jarvis 1.0 is built primarily with Python, leveraging several powerful libraries for its functionalities:

*   **Python 3.x**: The core programming language.
*   **`speech_recognition`**: For converting spoken language into text.
*   **`pyttsx3`**: For text-to-speech conversion, allowing Jarvis to speak.
*   **`pyaudio`**: A dependency for `speech_recognition` to handle microphone input.
*   **`datetime`**: For handling time-based operations (greetings, alarms).
*   **`webbrowser`**: For opening web pages and performing searches.
*   **`os` & `subprocess`**: For interacting with the operating system and running external commands.
*   **`pywhatkit`**: For automating WhatsApp messages.
*   **`wikipedia`**: For fetching information from Wikipedia during searches.
*   **`requests` & `json`**: For making HTTP requests to external APIs (e.g., news, translation services) and parsing responses.
*   **`opencv-python` (OpenCV)**: For computer vision tasks, specifically facial recognition (`faceRicognition.py`).
*   **`numpy`**: A fundamental package for scientific computing with Python, often a dependency for image processing libraries.

## Architecture

Jarvis 1.0 follows a modular architecture, where `AAAJarvis_main.py` serves as the central orchestrator. It listens for voice commands, processes them, and then dispatches tasks to specialized Python modules.

```
.
├── AAAJarvis_main.py       # Main entry point, voice command listener and dispatcher
├── GreetMe.py              # Handles personalized greetings
├── SearchNow.py            # Manages web searches
├── Whatsapp.py             # Integrates with WhatsApp for messaging
├── NewsRead.py             # Fetches and reads news
├── Calculatenumbers.py     # Performs calculations
├── Dictapp.py              # Provides dictionary lookup functionality
├── Translator.py           # Handles language translation
├── alarm.py                # Manages alarm setting and triggering
├── Remember.txt            # Stores user-defined reminders
├── FocusMode.py            # Implements focus mode logic
├── FocusGraph.py           # (Potentially) Visualizes focus data
├── faceRicognition.py      # Handles facial recognition tasks
├── game.py                 # Contains logic for simple games
├── keyboard.py             # Manages keyboard interactions
├── installModul.py         # Utility for installing required modules
└── ... (other utility scripts and data files)
```

The main script uses conditional logic (e.g., `if-elif-else` statements) to identify keywords in the user's spoken command and then calls the appropriate function or module to execute the requested task.

## Getting Started

Follow these steps to get Jarvis 1.0 up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
*   **`pip`**: Python's package installer (usually comes with Python).
*   **`PortAudio`**: Required by `pyaudio` for microphone access.
    *   **Windows**: Install `pipwin` first (`pip install pipwin`), then `pipwin install pyaudio`.
    *   **Linux (Debian/Ubuntu)**: `sudo apt-get install portaudio19-dev python3-pyaudio`
    *   **macOS**: `brew install portaudio` then `pip install pyaudio`

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Akshay94os/jarvis1.0.git
    cd jarvis1.0
    ```

2.  **Install required Python packages:**
    While a `requirements.txt` is not provided, you will need to install the libraries mentioned in the [Tech Stack](#tech-stack) section. Here's a common set:
    ```bash
    pip install speechrecognition pyttsx3 pyaudio datetime webbrowser wikipedia requests pywhatkit opencv-python numpy
    ```
    *Note: If you encounter issues with `pyaudio`, refer to the `PortAudio` prerequisites above.*

### Configuration

Some features require specific setup or data files:

*   **`password.txt`**: If any feature requires a password, it might be stored here. **Exercise caution and consider security implications if using this for sensitive data.**
*   **`Alarmtext.txt`**: Stores the messages for your alarms.
*   **`Remember.txt`**: Stores notes or reminders you ask Jarvis to remember.
*   **`focus.txt`**: Configuration for focus mode (e.g., blocked websites/applications).
*   **`music.mp3`**: Place your desired music file in the root directory if you want Jarvis to play it.

## Usage

To start Jarvis, simply run the main Python script:

```bash
python AAAJarvis_main.py
```

Jarvis will greet you and then listen for your commands. Here are some example commands you can try:

*   "Jarvis, what time is it?"
*   "Jarvis, open YouTube."
*   "Jarvis, search for Python tutorials on Google."
*   "Jarvis, tell me the news."
*   "Jarvis, calculate 5 plus 7."
*   "Jarvis, set an alarm for 7 AM saying good morning."
*   "Jarvis, remember to buy groceries."
*   "Jarvis, send a WhatsApp message to [Contact Name] saying hello."
*   "Jarvis, what is the definition of 'serendipity'?"
*   "Jarvis, play music."
*   "Jarvis, start focus mode."

## Development

### Setting Up Your Development Environment

1.  Ensure all [prerequisites](#prerequisites) and [installation](#installation) steps are completed.
2.  Open the project in your preferred Python IDE (e.g., VS Code, PyCharm).
3.  You can modify individual `.py` files to extend or customize Jarvis's functionality.

### Code Style Guidelines

*   Follow PEP 8 for Python code style.
*   Use clear and descriptive variable and function names.
*   Add comments where necessary to explain complex logic.

## Contributing

We welcome contributions to make Jarvis 1.0 even better!

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`
3.  **Make your changes** and ensure they adhere to the [code style guidelines](#code-style-guidelines).
4.  **Test your changes** thoroughly.
5.  **Commit your changes** with a clear and concise message: `git commit -m "feat: Add new feature X"`
6.  **Push your branch** to your forked repository: `git push origin feature/your-feature-name`
7.  **Open a Pull Request** to the `main` branch of the original repository, describing your changes in detail.

## Troubleshooting

*   **"No module named 'X'" error**: This means you're missing a required Python package. Install it using `pip install X`. Refer to the [Installation](#installation) section.
*   **`pyaudio` installation issues**: Ensure `PortAudio` is installed on your system before installing `pyaudio`. See [Prerequisites](#prerequisites).
*   **Jarvis doesn't respond**:
    *   Check your microphone settings and ensure it's properly connected and selected as the input device.
    *   Ensure your system's sound input is not muted.
    *   Verify that `AAAJarvis_main.py` is running without errors in the console.
*   **WhatsApp messages not sending**: Ensure you are logged into WhatsApp Web on your default browser and that `pywhatkit` has the necessary permissions.

## Roadmap

*   Integrate more third-party APIs (e.g., weather, calendar).
*   Improve natural language understanding for more complex commands.
*   Add support for custom hotkeys or wake words.
*   Develop a GUI for easier configuration and interaction.
*   Enhance facial recognition for more robust user authentication.

## License & Credits

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

**Developed by:**
*   Akshay94os (Original Author)

**Acknowledgments:**
*   Thanks to the open-source community for the powerful Python libraries that make this project possible.