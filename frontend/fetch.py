import requests

def fetch_all_data(base_url, initial_path='/liquor-fetch', max_retries = 5):
    """Fetch all data from the Fission function using scroll API with retry on timeout."""
    data = []
    url = base_url + initial_path
    params = {}
    # max_retries = 5

    while True:
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            result = response.json()
            print("5000 records get.")
            if not result.get('data'):
                print("No more results found")
                break
            data.extend(result['data'])
            scroll_id = result.get('scroll_id')
            if not scroll_id:
                print("No more results found")
                break
            params['scroll_id'] = scroll_id

        except requests.exceptions.Timeout:
            max_retries -= 1
            if max_retries <= 0:
                print("Maximum retries reached after timeout. Stopping.")
                break
            else:
                print(f"Timeout occurred. Retrying... ({max_retries} retries left)")
                continue
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            break
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    return data

if __name__ == '__main__':
    FISSION_ROUTER = 'http://127.0.0.1:9090'
    all_data = fetch_all_data(FISSION_ROUTER, '/weather5k-fetch')
    print(f"Retrieved {len(all_data)} records")