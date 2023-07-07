# Audio Device Information

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Structure](#structure)
- [Contributing](#contributing)
- [License](#license)

## Description
Audio Device Management is a Python project that allows you to manage and retrieve information about audio devices connected to the system. It provides functionalities to check the availability of input channels and perform various operations on audio devices.

The project consists of the following components:
- `main.py`: The main entry point of the project.
- `device_info.py`: Contains the `DeviceInformer` class for managing audio devices.
- `user_interface.py`: Handles the user interface and interaction.

## Installation
1. Clone the repository:
    ````shell
    git clone https://github.com/OlegSobadov/audio-device-management.git
    ````

2. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```
    
## Usage
To use the Audio Device Management project, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Run the following command to display available audio input devices:
    ```shell
    python user_interface.py
    ```


Example output:
    ````shell
    Device Index: 0
    Device Name: Microsoft Sound Mapper - Input

    Device Index: 5
    Device Name: Microphone (Realtek High Definition Audio)

    Device Index: 11
    Device Name: Microphone (Realtek HD Audio Mic input)


3. Follow the on-screen instructions to interact with the available devices.

## Testing

The project includes comprehensive test cases to ensure the correctness of its functionality. To run the tests, execute the following command:

```shell
python -m unittest discover tests
```

## Structure
```shell
audio-device-information/
  ├── main.py
  ├── device_info.py
  ├── user_interface.py
  ├── tests/
  │   └── test_device_info.py
  └── README.md
```


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).


