import pyaudio
import logging


logging.basicConfig(level=logging.ERROR)

class DeviceInformer:

    def __init__(self):
        self.p = pyaudio.PyAudio()


    def get_audio_devices_info(self):
        """
        Retrieve the information of all audio devices connected to the system.

        Returns:
            A list of dictionaries, where each dictionary represents an audio device with keys 'index' and 'name'.
        """
        try:
            device_info_list = []
            for device_index in range(self.p.get_device_count()):
                device_info = self.p.get_device_info_by_index(device_index)
                device_info_list.append(device_info)
            return device_info_list
        except Exception as exc:
            logging.error(f"An error occurred during device retrieval: {exc}")
            return []
        

    def is_input_available(self, device_info):
        """
        Check if the audio device has available input channels.

        Args:
            device_info (dict): Dictionary containing information about the audio device.

        Returns:
            bool: True if the audio device has available input channels, False otherwise.
        """
        return device_info['maxInputChannels'] > 0
    

    def get_available_input_devices(self):
        """
        Retrieve the available input audio devices.

        Prints the index and name of audio devices that have available input channels.
        """
        audio_devices_info = self.get_audio_devices_info()
        available_devices = []
        for device_info in audio_devices_info:
            if self.is_input_available(device_info):
                available_devices.append(device_info)
        return available_devices
    

def display_available_devices():
    device_information = DeviceInformer()
    available_devices = device_information.get_available_input_devices()

    if available_devices:
        print("Available Audio Devices:")
        print("-----------------------")
        for index, device_info in enumerate(available_devices):
            device_index = device_info.get('index', '')
            device_name = device_info.get('name', '')
            print(f"Device Index: {device_index}\nDevice Name: {device_name}\n")
    else:
        print("No available audio input devices.")

if __name__ == '__main__':
    display_available_devices()
