import os
import easyocr
import subprocess
from time import sleep
reader = easyocr.Reader(['en'])  # Add languages you expect
# folder = "mangadex_chapter" 

def run_ollama(prompt, model="llama3"):
    try:
        process = subprocess.Popen(
            ['ollama', 'run', model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors="ignore"
        )

        stdout, stderr = process.communicate(prompt)

        if stderr:
            print("❌ Error:", stderr)
        return stdout

    except Exception as e:
        print("Exception occurred:", str(e))

# def create_script(folder):



def analyse_images (folder):
    
    base_prompt = f"""
    You are a professional anime screenwriter.
    
    Based on the following manga dialogues and scenes, write:
    1. A short summary of the story.
    2. A structured anime script, with scene headings, character actions, and dialogues.
    
    Manga Content:
    """
    # Your folder with images
    for file in sorted(os.listdir(folder)):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder, file)
            print(f"\n🔍 OCR on {file}:")

            results = reader.readtext(image_path, detail=0)
            with open("extracted_text.txt", "a", encoding="utf-8") as f:
                # print(f"Text in {file}:")
                f.write(f"Text in {file}:\n")
                for text in results:
                    print(text)
                    f.write(  text + "\n")
    
    print(f"✅ Text extracted  saved to extracted_text.txt\n")
    sleep(5)  # Just to ensure the file is written before we read it
    if not os.path.exists("extracted_text.txt"):
        print("❌ No text extracted. Please check your images.")
        return
    
    with open("extracted_text.txt", "r", encoding="utf-8") as f:
        manga_content = f.read()
    print("📝 Generating script...")
    base_prompt += manga_content
    script = run_ollama(base_prompt)
    print("📜 Script generated:\n")
    print(script)
    with open("anime_script.txt", "w", encoding="utf-8") as f:
        f.write(script)
    print("✅ Script saved to anime_script.txt\n")
    
if __name__ == "__main__":
    folder = "mangadex_chapter"  # Folder with your images
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist. Please scrape a chapter first.")
    else:
        analyse_images(folder)
