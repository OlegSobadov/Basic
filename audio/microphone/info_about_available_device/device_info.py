# import pyaudio
# import logging


# model
class DeviceInformer:
    def __init__(self):
        self.p = pyaudio.PyAudio()

    def get_audio_devices_info(self):
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
        return device_info['maxInputChannels'] > 0

    def get_available_input_devices(self):
        audio_devices_info = self.get_audio_devices_info()
        available_devices = []
        for device_info in audio_devices_info:
            if self.is_input_available(device_info):
                available_devices.append(device_info)
        return available_devices
