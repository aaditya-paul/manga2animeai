import os
from PIL import Image

def stitch_images_vertically(image_folder, output_path):
    # Load all images from folder sorted by filename
    image_files = sorted(
        [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    )

    images = [Image.open(os.path.join(image_folder, f)) for f in image_files]

    # Calculate total width and height
    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)

    # Create a blank canvas with max_width and total_height
    stitched_img = Image.new('RGB', (max_width, total_height), color=(255, 255, 255))

    # Paste images one by one vertically
    y_offset = 0
    for img in images:
        # If image width is smaller, paste it centered horizontally
        x_offset = (max_width - img.width) // 2
        stitched_img.paste(img, (x_offset, y_offset))
        y_offset += img.height

    # Save the stitched image
    stitched_img.save(output_path)
    print(f"Stitched image saved at {output_path}")

if __name__ == "__main__":
    folder_path = "mangadex_chapter"   # folder with your images
    output_file = "stitched_manhwa.png"  # output stitched image path
    stitch_images_vertically(folder_path, output_file)
   



