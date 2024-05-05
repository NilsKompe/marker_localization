#!/usr/bin/env python3.8
from PIL import Image
from pathlib import Path
import pathlib, os, time, glob

full_path = pathlib.Path(__file__).parent.resolve()
path_to_images = str(Path(full_path).parents[0]) + "/img/"
filelist = glob.glob(os.path.join(path_to_images, "*"))
for f in filelist:
    os.remove(f)
# desired_number_of_markers = 12
desired_number_of_markers = (len(os.listdir(str(Path(full_path).parents[2]) + "/gazebo_models"))-2)
while len(os.listdir(path_to_images)) < desired_number_of_markers:
    print("waiting for all ArUco boards to be generated.", "There are ", len(os.listdir(path_to_images)), "boards, but ",desired_number_of_markers, " Gazebo blocks")
    time.sleep(1)
image_jackal_marker = Image.open(path_to_images + "board_0.png")
image_jackal_marker.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/board_1.png")
rotated_image = image_jackal_marker.rotate(180)
rotated_image.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/board_1_rotated.png")

for i in range(1,desired_number_of_markers):
    image = Image.open(path_to_images + "board_%i.png"%i)
    image.save(str(Path(full_path).parents[2]) + "/gazebo_models/AruCo_Block_%i/materials/textures/board_%i.png"%(i+1,i+1))

    

