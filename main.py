import os
import platform

if __name__ == '__main__':
    print(f"Current directory: {os.path.dirname(__file__)}")
    print(f"OS: {platform.system()}")
    print(f"Arhcitecture: {platform.processor()}")