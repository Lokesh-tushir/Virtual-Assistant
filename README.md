<h1>Code Explanation</h1>
    <h2>1. Importing necessary modules</h2>
    <p>
        The script imports the following modules:
    </p>
    <ul>
        <li>speech_recognition for voice input</li>
        <li>pyttsx3 for text-to-speech conversion</li>
        <li>datetime for time and date-related operations</li>
        <li>os for operating system-dependent functionalities</li>
        <li>wikipedia for fetching information from Wikipedia</li>
        <li>pyjokes for generating jokes</li>
        <li>pyautogui for controlling the mouse and keyboard</li>
        <li>ctypes for system-level operations</li>
        <li>requests for making HTTP requests</li>
        <li>psutil for retrieving system information</li>
        <li>operator for mathematical operations</li>
        <li>smtplib for sending emails</li>
        <li>phonenumbers for phone number parsing and handling</li>
        <li>pywhatkit for WhatsApp-related operations</li>
        <li>Various custom functions for different tasks</li>
    </ul>

<h2>2. Initializing the text-to-speech engine</h2>
    <p>
        The pyttsx3 engine is initialized and configured with a specific voice and speech rate.
    </p>

<h2>3. Defining helper functions</h2>
    <ul>
        <li><strong>wish_me()</strong>: Greets the user based on the current time.</li>
        <li><strong>take_command()</strong>: Listens to user input using the speech recognition module and returns the recognized text.</li>
        <li><strong>speak(audio)</strong>: Converts the given text to speech using the pyttsx3 engine
