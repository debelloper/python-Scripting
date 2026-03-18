import pyautogui # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore

# Get screen resolution
screen_size = pyautogui.size()

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 20.0, screen_size)

print("Recording started... Press CTRL+C to stop.")

try:
    while True:
        # Take screenshot
        img = pyautogui.screenshot()
        
        # Convert to numpy array
        frame = np.array(img)
        
        # Convert colors (RGB → BGR for OpenCV)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Write frame
        out.write(frame)

except KeyboardInterrupt:
    print("Recording stopped.")

# Release resources
out.release()
cv2.destroyAllWindows()