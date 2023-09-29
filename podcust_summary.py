import os
import json
import requests
import xmltodict

from airflow.decorators import dag, task
import pendulum
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

# from vosk import Model, KaldiRecognizer
# from pydub import AudioSegment

PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
EPISODE_FOLDER = "/home/omar/airflow_venv/python_scripts/episodes"


@dag(
    dag_id='podcast_summary_dag',
    schedule="*/5 * * * *",
    start_date=pendulum.datetime(2022, 5, 30),
    catchup=False,
)

def podcast_summary():

    create_database = SqliteOperator(
        task_id='create_table_sqlite',
        sql=r"""
        CREATE TABLE IF NOT EXISTS episodes (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT,
            transcript TEXT
        );
        """,
        sqlite_conn_id="podcasts"
    )
    @task()
    def get_episodes():
        data = requests.get(PODCAST_URL)
        feed = xmltodict.parse(data.text)
        episodes = feed["rss"]["channel"]["item"]
        print(f"Found {len(episodes)} episodes.")
        return episodes

    podcast_episodes = get_episodes()
    create_database.set_downstream(podcast_episodes)


    @task
    def load_episodes(episodes):
        hook = SqliteHook(sqlite_conn_id="podcasts")
        stored = hook.get_pandas_df("SELECT * FROM Episodes;")
        new_episodes = []
        for episode in episodes:
            if episode["link"] not in stored["link"].values:
                file_name = f"{episode['link'].split('/')[-1]}.mp3"
                new_episodes.append([episode['link'],episode['title'],file_name,episode['pubDate'],episode['description']])
        hook.insert_rows(table="Episodes",rows=new_episodes,target_fields=["link","title","filename","published","description"])

    load_episodes(podcast_episodes)

    @task
    def download_episodes(episodes):
        audio_files = []

        for episode in episodes[:3]:
            filename = f"{episode['link'].split('/')[-1]}.mp3"
            audio_path = os.path.join(filename)
            print(audio_path)
            # check whethear this file is exists or is not exists
            if not os.path.exists(audio_path):
                print(f"Downloading {filename}")
                audio = requests.get(episode["enclosure"]["@url"])
                with open(audio_path, "wb+") as file:
                    file.write(audio.content)
                    print(audio.url)
            audio_files.append({
                    "link": episode["link"],
                    "filename": filename
                })
        return audio_files

    audio_files = download_episodes(podcast_episodes)
summary = podcast_summary()
