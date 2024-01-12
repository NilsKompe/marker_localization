#!/usr/bin/env python3.8
from PIL import Image
from pathlib import Path


full_path = "/home/nils/jackal_ws/src/dynamic_object_jackal_slam/marker_localization/ml_detector/src"
# str(Path(full_path).parents[0])  # "path/to"
# str(Path(full_path).parents[1])  # "path"
# str(Path(full_path).parents[2]) 

image = Image.open(str(Path(full_path).parents[0]) + "/img/board_0.png")

rotated_image = image.rotate(180)

rotated_image.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/apriltags-003.png")
rotated_image.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/apriltags-004.png")
rotated_image.save(str(Path(full_path).parents[2]) + "/multi_jackal_simulator/multi_jackal_description/meshes/apriltags/images/apriltags-005.png")
