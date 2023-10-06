import matplotlib.pyplot as plt
import cv2


def count_objects(args):
    file_name, img_dir, save_path, save_images = args
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

        # print(f"Number of objects found: {num_objects} ({file_name})")
        return {"file_name": file_name, "count": num_objects}
    except Exception as e:
        print(f"EXCEPTION::: {e}, {file_name} ::: ")
