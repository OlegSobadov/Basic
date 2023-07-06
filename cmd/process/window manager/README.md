# Window Management Tool

**Table of Contents**
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Terminating Processes](#terminating-processes)
  - [Window Management](#window-management)
- [Hotkeys](#hotkeys)
- [*Continued Background Operation*](#continued-background-operation)
- [Requirements](#requirements)
- [License](#license)

## Introduction
The Window Management Tool is a Python script that provides functionality for terminating processes and managing `any chosen window` on a Windows operating system.



## Installation
To use the Window Management Tool, follow these steps:
1. Clone the repository or download the source code.
2. Install the required dependencies listed in the [Requirements](#requirements) section.

## Usage
### Terminating Processes
The tool allows you to terminate specific processes by their names.

### Window Management
The tool provides options to hide, show, and set windows as topmost.

To run the Window Management Tool, open a terminal or command prompt and navigate to the project directory. Then, run the following command:
````bash
python window_manager.py
````


## Hotkeys

The Window Management Tool utilizes hotkeys for quick access to its functionalities. The following hotkeys are available:

- **Ctrl+Alt+G:** Show the GUI window.
- **Ctrl+Alt+H:** Hide the GUI window.
- **Ctrl+Alt+T:** Set the GUI window as topmost.
- **Ctrl+Alt+R:** Remove the topmost setting from the GUI window.


## Continued Background Operation
`After closing the script`, the Window Management Tool `continues running in the background`, allowing you to access its features through the hotkeys.

## Requirements
The Window Management Tool has the following dependencies:
- Python 3.x
- psutil
- win32gui
- win32con
- keyboard

To install the dependencies, run the following command:

    pip install -r requirements.txt


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

