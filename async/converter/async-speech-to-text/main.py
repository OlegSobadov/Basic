import threading
import asyncio
import speech_recognition as sr
import tkinter as tk
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename="data/main.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")



async def recognize_speech():
    """
    Perform speech recognition on audio from the microphone.

    Returns:
        str: The recognized speech command.
    """
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        logging.info("Listening for voice commands...")

        try:
            audio = await loop.run_in_executor(None, r.listen, source)
            command = await loop.run_in_executor(None, r.recognize_google, audio)
            return command
        except sr.UnknownValueError:
            logging.error("Unable to recognize the speech.")
        except sr.RequestError:
            logging.error("Speech recognition service is unavailable.")

    return None

async def listen_for_voice_commands():
    """
    Continuously listen for voice commands and perform actions based on the recognized commands.
    """
    while True:
        command = await recognize_speech()
        if command:
            logging.info(f"Command: {command}")
            # Perform actions based on the recognized command

def start_listening_thread():
    """
    Start listening for voice commands in a separate thread.
    """
    thread = threading.Thread(target=start_listening)
    thread.start()

def start_listening():
    """
    Start listening for voice commands.
    """
    global loop, thread
    if not loop.is_running():
        loop.run_until_complete(listen_for_voice_commands())

def stop_listening_thread():
    """
    Stop listening for voice commands in a separate thread.
    """
    thread = threading.Thread(target=stop_listening)
    thread.start()

def stop_listening():
    """
    Stop listening for voice commands.
    """
    global loop, is_listening
    if loop.is_running():
        logging.info("Stopped listening for voice commands.")
        loop.stop()

loop = asyncio.get_event_loop()
thread = None

def create_gui():
    """
    Create the GUI with Start and Stop buttons.
    """
    root = tk.Tk()

    start_button = tk.Button(root, text="Start Listening", command=start_listening_thread)
    start_button.pack()

    stop_button = tk.Button(root, text="Stop Listening", command=stop_listening_thread)
    stop_button.pack()

    root.mainloop()


if __name__ == "__main__":
    create_gui()