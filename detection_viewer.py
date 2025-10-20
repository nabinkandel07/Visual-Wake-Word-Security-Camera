import os
import cv2
import config

cfg = config.load_config()
save_path = cfg['save_path']

if not os.path.exists(save_path):
    print("No detections folder found.")
else:
    files = [f for f in os.listdir(save_path) if f.endswith('.jpg')]
    files.sort(reverse=True)  # Newest first
    print(f"Found {len(files)} detections:")
    for f in files:
        print(f"- {f}")
    
    if files:
        # Display the latest
        img = cv2.imread(os.path.join(save_path, files[0]))
        cv2.imshow("Latest Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
