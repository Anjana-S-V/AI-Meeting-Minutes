import sounddevice as sd

print("Available audio input devices:\n")

devices = sd.query_devices()

for idx, device in enumerate(devices):
    if device["max_input_channels"] > 0:
        print(f"Device ID {idx}: {device['name']}")
