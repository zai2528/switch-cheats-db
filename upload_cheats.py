from bs4 import BeautifulSoup
import requests
import time
import datetime
import os
import rarfile
import shutil
import cloudscraper

scraper = cloudscraper.create_scraper()
page = scraper.get("https://gbatemp.net/download/cheat-codes-sxos-and-ams-main-cheat-file-updated.36311/")

soup = BeautifulSoup(page.content, "html.parser")

dl_url = "https://gbatemp.net/" + soup.find("a", {"class": "inner"}).get("href")
print(dl_url)

version = dl_url.split("=")[1]
with open("VERSION", 'w') as version_file:
    version_file.write(version)

date = datetime.datetime.today()
date_str = str(date).split()[0] + " - " + str(date.hour) + ":" + str(date.minute)

with open("DATE", 'w') as date_file:
    date_file.write(date_str)

if os.path.exists("out"):
    shutil.rmtree("out")
os.mkdir("out")
os.chdir("out")

dl = scraper.get(dl_url, allow_redirects=True)
open("titles.rar", "wb").write(dl.content)

rf = rarfile.RarFile("titles.rar")
rf.extractall()

shutil.make_archive("titles", "zip", base_dir="titles")
os.rename("titles", "contents")
shutil.make_archive("contents", "zip", base_dir="contents")