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