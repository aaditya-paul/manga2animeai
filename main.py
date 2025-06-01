from scrape import scrape_mangadex_chapter
from termcolor import colored
print(colored("Enter Chapter Link from MangaDex:","green",attrs=["bold"]))
input_link = input().strip()
if input_link:
# Extract chapter ID from the link
    if "https://mangadex.org/chapter/" in input_link:
        chapter_id = input_link.split("https://mangadex.org/chapter/")[-1].split("/")[0]
    else:
        print(  "Invalid MangaDex chapter link.")
        exit(1)
# scrape
    scrape_mangadex_chapter(chapter_id, "mangadex_chapter")
