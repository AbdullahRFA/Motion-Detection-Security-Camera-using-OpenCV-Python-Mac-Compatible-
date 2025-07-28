import cv2  # Import the OpenCV library for computer vision tasks
import subprocess  # Used to play audio using the macOS 'afplay' command
import time  # Used to manage time-based cooldown for playing sound

# Open the default camera (index 0)
cam = cv2.VideoCapture(0)

# Cooldown setup to prevent repeated sound triggering too quickly
last_played = 0  # Tracks the last time the alert sound was played
cooldown = 1  # Minimum interval (in seconds) between alert sounds

# Main loop: keeps running while camera is open
while cam.isOpened():
    # Capture two consecutive frames for motion comparison
    ret1, frame1 = cam.read()
    ret2, frame2 = cam.read()

    # Compute the absolute difference between the two frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding to highlight changes (motion areas)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in holes (makes motion areas more prominent)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours (continuous curves/edges) in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Flag to track whether motion is detected
    motion_detected = False

    # Loop through all detected contours
    for c in contours:
        # Ignore small movements (noise) by checking the area
        if cv2.contourArea(c) < 5000:
            continue

        # Get the bounding rectangle around the motion
        x, y, h, w = cv2.boundingRect(c)

        # Draw the rectangle on the frame
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mark that motion has been detected
        motion_detected = True

    # Get the current time to check for cooldown
    current_time = time.time()

    # If motion is detected and enough time has passed since last alert
    if motion_detected and (current_time - last_played > cooldown):
        # Play custom alert sound using macOS's afplay
        subprocess.Popen(['afplay', './Audio/alert.wav'])

        # Update the last_played time
        last_played = current_time

    # Display the current frame with motion rectangles (if any)
    cv2.imshow('Security Cam', frame1)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(10) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()