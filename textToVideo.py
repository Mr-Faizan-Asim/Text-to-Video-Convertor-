import cv2
import numpy as np

# Define the phrases to be displayed
phrases = ["Welcome", "To the World Of Dreamers", "Let's Dream together"]

# Define video parameters
fps = 30  # Frames per second
duration_per_phrase = 2  # Duration for each phrase in seconds
frame_size = (640, 480)  # Frame size (width, height)

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('text_to_video.avi', fourcc, fps, frame_size)

# Create a loop to generate frames and write them to the video
for phrase in phrases:
    for t in range(fps * duration_per_phrase):
        # Create a blank frame with a black background
        frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)

        # Calculate the position of the text
        text_position = (int(frame_size[0] / 4), int(frame_size[1] / 2))

        # Define the path to the Arial Bold font file (change to the actual path)
        font_path = 'path_to_arial_bold.ttf'  # Replace with the actual path

        # Load the Arial Bold font
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2
        font_color = (255, 255, 255)  # White
        cv2.putText(frame, phrase, text_position, font, font_scale, font_color, font_thickness, lineType=cv2.LINE_AA)

        # Write the frame to the video
        out.write(frame)

        # Display the frame on screen
        cv2.imshow('Text to Video', frame)
        cv2.waitKey(1000 // fps)  # Display each frame for the appropriate duration

# Release the VideoWriter and close the display window
out.release()
cv2.destroyAllWindows()

# Display a message when the video is created
print("Video created successfully!")

# Close all OpenCV windows
cv2.destroyAllWindows()
