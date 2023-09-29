import requests
import xmltodict
import os
EPISODE_FOLDER = "/home/omar/airflow_venv/python_scripts/episodes"
PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
data = requests.get(PODCAST_URL)
feed = xmltodict.parse(data.text)
episodes = feed["rss"]["channel"]["item"]
for i in episodes:
    filename = f"{i['link'].split('/')[-1]}.mp3"

    # audio = requests.get(i["enclosure"]["@url"])
    audio_path = os.path.join(EPISODE_FOLDER, filename)

    # print(filename,end="\n\n\n")

    print(audio_path,end="\n\n\n")
    
    # print(audio.content,end="\n\n\n")



    
# print(episodes)