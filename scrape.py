import os
import requests
from analyse import analyse_images  # Assuming you have an analyse.py with a function to analyze images
# Your target chapter ID
# chapter_id = "618517ca-fd8d-4b50-a265-b3bb42432bd4"
output_folder = "mangadex_chapter"

def scrape_mangadex_chapter(chapter_id, output_folder):
    # Step 1: Get chapter info from MangaDex API
    chapter_api_url = f"https://api.mangadex.org/at-home/server/{chapter_id}"
    res = requests.get(chapter_api_url)
    if res.status_code != 200:
        print("Failed to fetch chapter metadata.")
        return

    data = res.json()
    print("Chapter metadata fetched successfully.")
    # print(data)
    base_url = data["baseUrl"]
    chapter_data = data["chapter"]
    hash_val = chapter_data["hash"]
    image_filenames = chapter_data["data"]

    # Step 2: Create folder to save images
    os.makedirs(output_folder, exist_ok=True)

    # Step 3: Download each image
    for i, filename in enumerate(image_filenames, 1):
        img_url = f"{base_url}/data/{hash_val}/{filename}"
        img_data = requests.get(img_url).content

        ext = os.path.splitext(filename)[1]
        out_path = os.path.join(output_folder, f"page_{i:03d}{ext}")
        with open(out_path, "wb") as f:
            f.write(img_data)
        print(f"Downloaded page {i}")

    print("✅ Download complete.")
    print(f"Images saved in folder: {output_folder}")
    print("Analysing and extracting text from images...")
    # Analyse images and extract text
    analyse_images(output_folder)
if __name__ == "__main__":
    print("Enter Chapter Link from MangaDex:")
    input_link = input().strip()
    if input_link:
        # Extract chapter ID from the link
        if "https://mangadex.org/chapter/" in input_link:
            chapter_id = input_link.split("https://mangadex.org/chapter/")[-1].split("/")[0]
        else:
            print("Invalid MangaDex chapter link.")
            exit(1)
    # scrape
    scrape_mangadex_chapter(chapter_id, output_folder)
