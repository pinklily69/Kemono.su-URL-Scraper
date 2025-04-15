import scraper_module

import os
from datetime import datetime

def load_config():
    import configparser
    config = configparser.ConfigParser()
    config.read("config.ini")
    base_url = config.get("Kemono", "base_url")
    max_pages = config.getint("Kemono", "max_pages")
    return base_url, max_pages

base_url, max_pages = load_config()

urls = scraper_module.run_scraper(base_url, max_pages)

# Save URLs to file
date_str = datetime.now().strftime("%Y-%m-%d")
output_folder = "stolen-urls"
os.makedirs(output_folder, exist_ok=True)
output_filename = f"{output_folder}/kemono_stolen_urls_{date_str}.txt"

if urls:
    with open(output_filename, "w", encoding="utf-8") as file:
        for url in sorted(urls):
            file.write(url + "\n")
    print(f"\n✅ Success! {len(urls)} URLs saved to '{output_filename}'.")
else:
    print("⚠️ No URLs found.")
