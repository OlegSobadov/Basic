import unittest
from device_info import DeviceInformer

class DeviceInformerTestCase(unittest.TestCase):
    def setUp(self):
        self.device_manager = DeviceInformer()

    def test_get_audio_devices_info(self):
        device_info_list = self.device_manager.get_audio_devices_info()
        self.assertIsInstance(device_info_list, list)
        self.assertGreater(len(device_info_list), 0)

    def test_is_input_available(self):
        device_info = {
            'index': 5,
            'name': 'Microphone (Realtek High Definition Audio)',
            # 'maxInputChannels': 2
        } # change to real device information;
        is_input_available = self.device_manager.is_input_available(device_info)
        self.assertTrue(is_input_available)

    def test_get_available_input_devices(self):
        available_devices = self.device_manager.get_available_input_devices()
        self.assertIsInstance(available_devices, list)

if __name__ == '__main__':
    unittest.main()
