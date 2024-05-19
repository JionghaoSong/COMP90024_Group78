# Project Name

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
   python server.py
