import json
import os

CONFIG_FILE = 'config.json'

# Default config
default_config = {
    "model_path": "ssd_mobilenet_v1_1_metadata_1.tflite",
    "labels_path": "coco_labels.txt",
    "threshold": 0.5,
    "target_label": "person",
    "resolution": [640, 480],
    "framerate": 30,
    "save_path": "./detections/",
    "alert_email": "your_email@example.com",  # For alerts
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "smtp_user": "your_email@example.com",
    "smtp_pass": "your_password"  # Use app password for Gmail
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        save_config(default_config)
        return default_config

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    config = load_config()
    print("Current config:", config)
    # Edit and save if needed
