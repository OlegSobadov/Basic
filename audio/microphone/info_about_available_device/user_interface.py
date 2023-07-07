from device_info import DeviceInformer

def display_available_devices():
    device_manager = DeviceInformer()
    available_devices = device_manager.get_available_input_devices()

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
