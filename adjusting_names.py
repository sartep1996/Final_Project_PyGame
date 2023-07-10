import os

folder_path = '/Users/petrasanskaitis/Desktop/Programavimas Python/CodeAcademy/Final_Project_PyGame/Images/Player_sprites_pistol' # Replace with the actual folder path

for filename in os.listdir(folder_path):
    if filename.endswith("_p.png"):
        new_filename = filename[:-6] + ".png" 
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")
