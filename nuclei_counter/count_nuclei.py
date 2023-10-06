import os
from pathlib import Path
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import argparse

pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

from tqdm.contrib.concurrent import process_map

parser = argparse.ArgumentParser(description="Process and count nuclei in images.")
parser.add_argument(
    "--img_dir",
    help="Path to the directory containing images.",
)

parser.add_argument(
    "--output_dir",
    default=Path(os.getcwd()) / "results",
    help="Save directory for results files.",
)

parser.add_argument(
    "--save_images",
    action="store_true",
    help="Include this flag to save transformed images used for counting.",
)

parser.add_argument(
    "--output_count_filename",
    default="count_results.csv",
    help="Output file name of the resulting CSV. Defaults to count_results.csv",
)

args = parser.parse_args()

img_dir = Path(args.img_dir)
output_file_name = args.output_count_filename
save_path = args.output_dir
save_images = args.save_images

file_names = os.listdir(img_dir)
os.makedirs(save_path, exist_ok=True)

def count_objects(file_name):
    if not file_name.lower().endswith((".png", ".jpg")):
        return None
    try:
        img = cv2.imread(str(img_dir / file_name))
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply thresholding
        thresh = cv2.threshold(gray, 11, 255, cv2.THRESH_BINARY)[1]
        # Apply morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        plt.imshow(opening)
        if save_images:
            cv2.imwrite(str(save_path / f"transformed_{file_name}"), opening)
        # Find contours
        contours, _ = cv2.findContours(
            opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Count the number of contours
        num_objects = len(contours)

        print(f"Number of objects found: {num_objects} ({file_name})")
        return {"file_name": file_name, "count": num_objects}
    except Exception as e:
        print(f"EXCEPTION::: {e}, {file_name} ::: ")


results = process_map(count_objects, file_names)
df = pd.DataFrame([result for result in results if result is not None])
df.to_csv(save_path / output_file_name, index=False)
