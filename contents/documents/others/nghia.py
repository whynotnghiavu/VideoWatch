import os
import subprocess
from time import sleep
# prettier --write  file_path
# pip install pyautogui
import pyautogui


def format(directory):
    exclude_dirs = [".git", "node_modules", "__pycache__"]
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            # Nếu file có đuôi là ".code-workspace" thì bỏ qua continue

            if file.endswith(".code-workspace"):
                continue

            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                subprocess.run(["code", file_path], check=True, shell=True)
                sleep(1)

                if os.name == 'nt':
                    pyautogui.hotkey('alt', 'shift', 'o')
                    pyautogui.hotkey('alt', 'shift', 'f')
                elif os.name == 'posix':
                    pyautogui.hotkey('alt', 'shift', 'o')
                    pyautogui.hotkey('ctrl', 'shift', 'i')
                sleep(0.5)
                # sleep(1)


if __name__ == "__main__":
    paths = [
        # "/home/vvn20206205/Desktop/einvoice-system/microservices/api-gateway/src",
        # "/home/vvn20206205/Desktop/einvoice-system/microservices/user-service/src",
        # "/home/vvn20206205/Desktop/einvoice-system/microservices/invoice-service/src",
        # "/home/vvn20206205/Desktop/einvoice-system/microservices/tct-demo/src",
        # "/home/vvn20206205/Desktop/vuvannghia/src",
        # "/home/vvn20206205/Desktop/einvoice-system/microservices/report-service/src",
        # "C:\\Users\\vvn20206205\\Downloads\\Nghia\\Git\\whynotnghiavu",
        # "C:\\Users\\vvn20206205\\Downloads\\Nghia\\Git\\whynotnghiavu\\nghia-contact-manager",
        # r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\nghia-extensions-video-VN\contents",

        # r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\VideoVN",
        # r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu",
        r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\VideoWatch",
    ]
    for path in paths:
        format(path)
