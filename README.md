# AI-Powered "Visual Wake Word" Security Camera
To expand the AI-Powered "Visual Wake Word" Security Camera project, I've added more code files for enhanced functionality. These include a configuration script for easy settings management, an alert system for notifications (e.g., email on detection), a viewer script to browse saved detections, and a requirements.txt file for dependencies. This makes the project more robust, user-friendly, and production-ready. A Raspberry Pi-based security camera that uses AI (TensorFlow Lite with MobileNet SSD) to detect specific objects (e.g., a person) as a "wake word," reducing data processing by only activating on detections.


### Requirements
- Same as before: Raspberry Pi with PiCamera, Python 3.7+, libraries from `requirements.txt`.
- For alerts: Install `smtplib` (built-in) and optionally `twilio` for SMS (`pip install twilio`).
- Ensure the TFLite model and labels are in the project directory.

### Additional Code Files
Save these alongside `camera_detector.py` in the project directory.


#### requirements.txt (Dependency List)
Save this file for easy installation.

```
opencv-python==4.8.0.76
tflite-runtime==2.11.0
picamera==1.13
numpy==1.21.5
```

### Setup and Usage
- **Install Dependencies**: Run `pip install -r requirements.txt`.
- **Configure**: Edit `config.json` (created on first run) with your settings.
- **Run**: Execute `python camera_detector.py` for detection, `python detection_viewer.py` to view saved images.
- **Alerts**: Set up email credentials in config for notifications.
- **Testing**: Test with the viewer script after detections.


## Features
- Real-time object detection using a lightweight TFLite model.
- Saves images only when the target object is detected.
- Low-power, edge-optimized for Raspberry Pi.
- Customizable detection thresholds and objects.

## Requirements
- Raspberry Pi with PiCamera.
- Python libraries: `opencv-python`, `tflite-runtime`, `picamera`, `numpy`.
- Pre-trained MobileNet SSD TFLite model and COCO labels.

## Installation
1. Install dependencies: `pip install opencv-python tflite-runtime picamera numpy`.
2. Download model and labels from TensorFlow Hub.
3. Enable PiCamera in `raspi-config`.

## Usage
- Run `python camera_detector.py`.
- Camera detects persons and saves images (e.g., `detection_20231001-120000.jpg`).
- Press 'q' to quit.

## Configuration
- Change `TARGET_LABEL` in the code for other objects.
- Adjust `THRESHOLD` for sensitivity.

## Contributing
Fork and submit PRs for improvements!






