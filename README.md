
# Data Fetching and Processing Project

This project consists of several Python scripts and a build script to fetch, process, and analyze data from various sources using Elasticsearch.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
  - [accidents.py](#accidentspy)
  - [liquor.py](#liquorpy)
  - [mastodon.py](#mastodonpy)
  - [sensor.py](#sensorpy)
  - [weather.py](#weatherpy)
  - [fetch.py](#fetchpy)
- [Build Script](#build-script)
- [Dependencies](#dependencies)
- [API Endpoints](#api-endpoints)

## Prerequisites

Ensure you have the following installed:
- Python 3.7+
- Pip

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python packages:
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage

To run any of the scripts, use the following command:
```sh
python3 <script_name>.py
```

## Scripts

### accidents.py

Fetches accident data from the Elasticsearch index with support for scroll functionality.

### liquor.py

Fetches liquor data from the Elasticsearch index.

### mastodon.py

Fetches data from the Mastodon social network index in Elasticsearch.

### sensor.py

Fetches sensor data from the Elasticsearch index with support for scroll functionality.

### weather.py

Fetches weather data from the Elasticsearch index with support for scroll functionality.

### fetch.py

Fetches all data from a specified Fission function using the scroll API.

## Build Script

The `build.sh` script installs the required packages and prepares the deployment package.

```sh
#!/bin/sh
pip3 install -r ${SRC_PKG}/requirements.txt -t ${SRC_PKG} && cp -r ${SRC_PKG} ${DEPLOY_PKG}
```

Run the build script using:
```sh
sh build.sh
```

## Dependencies

The project dependencies are listed in `requirements.txt`:

```txt
elasticsearch8==8.11.0
```

Install them using:
```sh
pip3 install -r requirements.txt
```

## API Endpoints

The following API endpoints are available for fetching data:

### GET
- `/liquor/data`
- `/accidents/data`
- `/mastodon/data`
- `/sensors/data`
- `/weather/data`  

eg. `curl "http://127.0.0.1:9090/sensors/data" | jq '.'`
> Parameters  
- **scroll_id**: scroll_id is used to locate the documents (Can be None when first call)
- **size**: setting the size of returned documents (default = 5000)

eg. `curl "http://127.0.0.1:9090/sensors/data?size=100" | jq '.'`
> Return  
- **data**
- **scroll_id**: used for next search




# README

This repository contains several Python scripts for creating and inserting data into Elasticsearch indices. The scripts use the Elasticsearch Python client to interact with the Elasticsearch service. Each script serves a specific purpose, such as creating indices or bulk inserting data from JSON or CSV files.

## Requirements

- Python 3.x
- Elasticsearch
- Python packages: `elasticsearch`, `python-dotenv`

## Installation

1. Clone the repository.
2. Install the required Python packages:
    ```sh
    pip install elasticsearch python-dotenv
    ```
3. Ensure Elasticsearch is running and accessible.

## Scripts

### 1. `create_mastodon.py`
Creates an index for Mastodon social data in Elasticsearch.

### 2. `insert_mastodon.py`
Inserts Mastodon social data into the created Elasticsearch index from JSON files.

### 3. `insert_filter_mastodon.py`
Inserts filtered Mastodon social data into Elasticsearch.

### 4. `create_pedestrain.py`
Creates an index for pedestrian counting data.

### 5. `insert_pedestrain.py`
Inserts pedestrian counting data from a CSV file into the Elasticsearch index.

### 6. `create_weather.py`
Creates an index for weather station data.

### 7. `insert_weather.py`
Inserts weather station data from a CSV file into the Elasticsearch index.

### 8. `insert_liquor.py`
Inserts liquor license data from a CSV file into Elasticsearch.

### 9. `insert_crash.py`
Inserts road crash data from a CSV file into Elasticsearch.

### 10. `create_crash.py`
Creates an index for road crash data.

### 11. `create_liquor.py`
Creates an index for liquor license data.

### 12. `create_filter_mastodon.py`
Creates an index for filtered Mastodon social data.

## Usage

1. Create the necessary indices by running the respective `create_*` scripts.
2. Insert data by running the `insert_*` scripts with the appropriate data files.

### Example
To create and populate the Mastodon social data index:
```sh
python create_mastodon.py
python insert_mastodon.py
```

## Environment Variables
Create a `.env` file in the root directory with the following content:
```
ELASTIC_PSW=your_elasticsearch_password
```

Ensure to replace `your_elasticsearch_password` with your actual Elasticsearch password.

## License
This project is licensed under the MIT License.

For more details, refer to the individual script files.
```

# Geo-data reference
https://cloud.tencent.com/developer/article/1050321




# Elasticsearch

This repository contains several Python scripts for creating and inserting data into Elasticsearch indices. The scripts use the Elasticsearch Python client to interact with the Elasticsearch service. Each script serves a specific purpose, such as creating indices or bulk inserting data from JSON or CSV files.

## Requirements

- Python 3.x
- Elasticsearch
- Python packages: `elasticsearch`, `python-dotenv`

## Installation

1. Clone the repository.
2. Install the required Python packages:
    ```sh
    pip install elasticsearch python-dotenv
    ```
3. Ensure Elasticsearch is running and accessible.

## Scripts

### 1. `create_mastodon.py`
Creates an index for Mastodon social data in Elasticsearch.

### 2. `insert_mastodon.py`
Inserts Mastodon social data into the created Elasticsearch index from JSON files.

### 3. `insert_filter_mastodon.py`
Inserts filtered Mastodon social data into Elasticsearch.

### 4. `create_pedestrain.py`
Creates an index for pedestrian counting data.

### 5. `insert_pedestrain.py`
Inserts pedestrian counting data from a CSV file into the Elasticsearch index.

### 6. `create_weather.py`
Creates an index for weather station data.

### 7. `insert_weather.py`
Inserts weather station data from a CSV file into the Elasticsearch index.

### 8. `insert_liquor.py`
Inserts liquor license data from a CSV file into Elasticsearch.

### 9. `insert_crash.py`
Inserts road crash data from a CSV file into Elasticsearch.

### 10. `create_crash.py`
Creates an index for road crash data.

### 11. `create_liquor.py`
Creates an index for liquor license data.

### 12. `create_filter_mastodon.py`
Creates an index for filtered Mastodon social data.

## Usage

1. Create the necessary indices by running the respective `create_*` scripts.
2. Insert data by running the `insert_*` scripts with the appropriate data files.

### Example
To create and populate the Mastodon social data index:
```sh
python create_mastodon.py
python insert_mastodon.py
```

## Environment Variables
Create a `.env` file in the root directory with the following content:
```
ELASTIC_PSW=your_elasticsearch_password
```

Ensure to replace `your_elasticsearch_password` with your actual Elasticsearch password.

## License
This project is licensed under the MIT License.

For more details, refer to the individual script files.
```

# Geo-data reference
https://cloud.tencent.com/developer/article/1050321


# Elasticsearch - Jupyter

This folder contains the front-end of the project which is a Jupyter Notebook showcasing the visualisation for the data that we have collected.

# Scenarios:
1. The relationship between the location of car crashes and location of pubs.
2. The relationship between the weather and the flow of pedestrian.
3. How could the weather affect people's mood and emotion.
4. The changes of the sentiment score over a year.


#### [World_Cloud.py](./World_Cloud.py)
This file generates a world cloud based on the data that we have retrieved from Mastodon

To run this file, install the packages below first:
```bash
pip install wordcloud
pip install matplotlib
pip install nltk
```



# Mastodon

## Project Overview
This project is designed to collect and process data from various Mastodon servers, specifically focusing on the aus. Social and mastodon. Social servers. It aims to provide insights into the usage patterns and trends within these communities.

## Project Structure
- `harvester.py`: Script for collecting data from specified Mastodon servers.
- `request.py`: Handles API requests.
- `server.py`: Sets up and runs the server.
- `cleaner.py`: Cleans and processes the data.
- `token.json`: Stores tokens for accessing Mastodon servers.
- `MASTODON_SOCIAL_TOKEN`: Token for the mastodon.social server.
- `MASTODON_AU_TOKEN`: Token for the aus.social server.

## How to Run
1. Ensure Python and all necessary dependencies are installed.
2. Configure the `token.json` file, ensuring the tokens are up-to-date.


## To collect data
Navigate to the project directory in the command line and run the following command to start the server:
```bash
   python harvester.py .



# Testing
This repository contains unit test Python scripts for creating data and inserting it into Elasticsearch indices. These scripts simulate a server using the mock_client library and then perform operational checks against the simulated server.

## Requirements

- Python 3.x
- Elasticsearch
- Python packages: `elasticsearch`, `python-dotenv`
- Python packages: `unittest`

## Installation

1. Clone the repository.
2. Install the required packages:
    ```sh
    ./install.sh
    ```
3. Ensure Elasticsearch is running and accessible.

## Scripts

### 1. `test_API.sh`
test the server is running successful or not, echo the state code

### 2. `UT.sh`
run all avaliable unit test for the elasticsearch server



### Example
To create and populate the Mastodon social data index:
```sh
./UT.sh
./test_aip.sh
```

## Environment Variables
Create a `.env` file in the root directory with the following content:
```
ELASTIC_PSW=your_elasticsearch_password
```

Ensure to replace `your_elasticsearch_password` with your actual Elasticsearch password.

## License
This project is licensed under the MIT License.

For more details, refer to the individual script files.
```

# Geo-data reference
https://cloud.tencent.com/developer/article/1050321


