import os
import subprocess
import tkinter as tk
import win32gui, win32con
import keyboard
import psutil


subprocess_running = False  # mark
                            # Flag to indicate if the subprocess is running
subprocess_pythonw = None  # Reference to the subprocess instance
si = None  # STARTUPINFO for subprocess
hidden_window_handle = None  # Store the handle of the previously hidden window
hidden_items = []  # Store the handles of the items to be hidden
topmost_items = []  # Store the handles of the items to be topmost

def terminate_process():
    """
    Terminate the specified process by name.

    Retrieves the process name from the entry field in the GUI.
    Uses the taskkill command to terminate the process forcefully.

    Updates the status label with the result of the termination.
    """
    process_name = entry.get()
    text = f'close process to {process_name}.exe'
    command_cmd = f"taskkill /im {process_name}.exe /f"
    result = os.popen(command_cmd).read()
    update_status_label(result)


def show_window():
    """
    Show the previously hidden items and bring the application window to the front.

    Clears the list of hidden items.
    """
    global hidden_items

     # Show the previously hidden items
    for item in hidden_items:
        win32gui.ShowWindow(item, win32con.SW_SHOW)

    hidden_items = []  # Reset the list of hidden items

    # Uncomment the lines below if you want to make the application window visible and bring it to the front
    # root.deiconify()  # Make the application gui window visible
    # win32gui.SetForegroundWindow(root.winfo_id())  # Bring the application window to the front


def hide_window():
    """
    Hide the application window and desired items.

    Stores the handles of the hidden items in the `hidden_items` list.
    """
    global hidden_items
    # Uncomment the lines below if you want to make the application window invisible
    # root.withdraw() # Make the application gui window invisible

    # Hide the desired items and store their handles
    item_handles = [win32gui.GetForegroundWindow()]
    # Add additional items to be hidden to the 'item_handles' list

    for item_handle in item_handles:
        win32gui.ShowWindow(item_handle, win32con.SW_HIDE)
        hidden_items.append(item_handle)


def set_window_topmost():
    """
    Set the application window and desired items as topmost.

    Stores the handles of the topmost items in the `topmost_items` list.
    """
    global topmost_items
    item_handles = [win32gui.GetForegroundWindow()]
    for hwnd in item_handles:
        # Get the class name of the window
        class_name = win32gui.GetClassName(hwnd)
        if class_name != "TaskManagerWindow":
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            topmost_items.append(hwnd)

def remove_window_topmost():
    """
    Remove the topmost setting from the application window and desired items.

    Resets the `topmost_items` list.
    """
    global topmost_items
    # hwnd = win32gui.GetForegroundWindow()
    hwnds = topmost_items.copy()
    def callback(hwnd, hwnds):
        for hwnd in hwnds:
            win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # Enumerate all top-level windows and exclude Task Manager
    win32gui.EnumWindows(callback, hwnds)

    # topmost_items = [] # Reset
    topmost_items.clear() # Reset the list of topmost items

def on_hotkey_press():
    """
    Callback function for the "ctrl+alt+g" hotkey.

    Shows the application window.
    """
    show_window()


def on_hotkey_press_hide():
    """
    Callback function for the "ctrl+alt+h" hotkey.

    Hides the application window.
    """
    hide_window()

def on_closing():
    """
    Callback function for the window close event.

    Terminates the subprocess and destroys the application window.
    """
    global subprocess_pythonw
    subprocess_pythonw.terminate()
    root.destroy()


# gui - def 
def update_status_label(text):
    """
    Update the status label text.

    Args:
        text (str): The text to be displayed in the status label.
    """
    status_label.config(text=text)
    

# Create the GUI app
root = tk.Tk()
root.title('Terminate Process')


# Create labels, entry, buttons fields
status_label = tk.Label(root, text='')
status_label.pack()


default_entry = 'notepad'
entry = tk.Entry(root)
entry.insert(0, default_entry)
entry.pack()

b_terminate = tk.Button(root, text='Terminate', command=terminate_process)
b_terminate.pack()

b_close = tk.Button(root, text="Close", command=on_closing)
b_close.pack()


keyboard.add_hotkey("ctrl+alt+g", on_hotkey_press)
keyboard.add_hotkey("ctrl+alt+h", on_hotkey_press_hide)

keyboard.add_hotkey("ctrl+alt+t", set_window_topmost)
keyboard.add_hotkey("ctrl+alt+r", remove_window_topmost)


if __name__ == '__main__':
    def running_after_close():
        """
        Check if the subprocess is still running after the main window is closed.

        If the subprocess is not running, start a new instance of the script with a hidden console window.
        """
        global subprocess_running, subprocess_pythonw, si

        for proc in psutil.process_iter(['name', 'cmdline']):
            if 'pythonw.exe' in proc.info['name'].lower() and __file__ in proc.info['cmdline']:
                subprocess_running = True
                break
            
        if not subprocess_running:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = win32con.SW_HIDE

            subprocess_pythonw = subprocess.Popen(['pythonw', __file__], creationflags=subprocess.CREATE_NO_WINDOW, startupinfo=si)
            root.destroy() # Close gui script.py to continues running in the background (process)

    running_after_close()
    root.mainloop()