# Podcast Transcription Data Pipeline using Apache Airflow

## Project Overview

In this project, we'll create a data pipeline using Apache Airflow to download podcast episodes and automatically transcribe them using speech recognition. The results will be stored in a SQLite database, making it easy to query and analyze the transcribed podcast content.

While this project doesn't strictly require the use of Apache Airflow, it offers several advantages:

- We can schedule the project to run on a daily basis.
- Each task can run independently, and we receive error logs for troubleshooting.
- Tasks can be easily parallelized, and the project can run in the cloud if needed.
- It provides extensibility for future enhancements, such as adding more advanced speech recognition or summarization.

By the end of this project, you'll have a solid understanding of how to utilize Apache Airflow and a practical project that can serve as a foundation for further development.

## Project Steps

1. **Download Podcast Metadata XML and Parse**
   - Obtain the metadata for podcast episodes by downloading and parsing an XML file.

2. **Create a SQLite Database for Podcast Metadata**
   - Set up a SQLite database to store podcast metadata efficiently.

3. **Download Podcast Audio Files Using Requests**
   - Download the podcast audio files from their sources using the Python `requests` library.

4. **Transcribe Audio Files Using Vosk**
   - Implement audio transcription using the Vosk speech recognition library.

## Getting Started

### Local Setup

Before you begin, ensure that you have the following prerequisites installed locally:

- [Apache Airflow 2.3+](https://airflow.apache.org/docs/apache-airflow/stable/start/index.html)
- [Python 3.8+](https://www.python.org/downloads/)
- Python packages:
  - pandas
  - sqlite3
  - xmltodict
  - requests
  

Please follow the [Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html) to install Apache Airflow successfully.

### Data

During the project, we'll download the required data, including a language model for Vosk and podcast episodes. If you wish to explore the podcast metadata, you can find it [here](insert_metadata_link_here).

## Code

You can access the project code in the [code directory](https://github.com/3amory99/Podcust-Summary-Data-Pipeline-Using-Airflow.git).

## Project Usage

To run the data pipeline, follow the steps provided in the [steps.md](insert_steps_file_link_here) file.

