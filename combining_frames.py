import cv2
import os

# Number of frames captured
num_frames = 100

# Frame width and height (assuming all frames have the same size)
frame_width, frame_height = 800, 600

# Path to the directory containing the frames
frames_dir = "loading_images"

# Create a VideoWriter object to save the video
output_filename = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30  # Adjust the frames per second (FPS) as needed
output_video = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Loop through the frames and add them to the video
for i in range(num_frames):
    frame_filename = os.path.join(frames_dir, f"loading_frame_{i:04d}.png")
    frame_img = cv2.imread(frame_filename)
    output_video.write(frame_img)

# Release the VideoWriter and close the video file
output_video.release()

print(f"Video saved as {output_filename}")
