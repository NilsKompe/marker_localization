#!/usr/bin/env python3.8
from PIL import Image
from pathlib import Path


full_path = "/home/nils/jackal_ws/src/dynamic_object_jackal_slam/marker_localization/ml_detector/src"
# str(Path(full_path).parents[0])  # "path/to"
# str(Path(full_path).parents[1])  # "path"
# str(Path(full_path).parents[2]) 

image = Image.open(str(Path(full_path).parents[0]) + "/img/board_4.png")
image.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/board_4.png")
rotated_image = image.rotate(180)
rotated_image.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/board_4_rotated.png")

image = Image.open(str(Path(full_path).parents[0]) + "/img/board_0.png")
image.save(str(Path(full_path).parents[2]) + "/gazebo_models/AruCo_Block_0/materials/textures/board_0.png")
image = Image.open(str(Path(full_path).parents[0]) + "/img/board_1.png")
image.save(str(Path(full_path).parents[2]) + "/gazebo_models/AruCo_Block_1/materials/textures/board_1.png")
image = Image.open(str(Path(full_path).parents[0]) + "/img/board_2.png")
image.save(str(Path(full_path).parents[2]) + "/gazebo_models/AruCo_Block_2/materials/textures/board_2.png")
image = Image.open(str(Path(full_path).parents[0]) + "/img/board_3.png")
image.save(str(Path(full_path).parents[2]) + "/gazebo_models/AruCo_Block_3/materials/textures/board_3.png")

