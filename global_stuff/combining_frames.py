import cv2
import os

num_frames = 100

frame_width, frame_height = 800, 600

frames_dir = "loading_images"

output_filename = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30  
output_video = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

for i in range(num_frames):
    frame_filename = os.path.join(frames_dir, f"loading_frame_{i:04d}.png")
    frame_img = cv2.imread(frame_filename)
    output_video.write(frame_img)

output_video.release()

print(f"Video saved as {output_filename}")
