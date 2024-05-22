
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



