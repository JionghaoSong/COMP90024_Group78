import requests

def fetch_all_data(base_url, initial_path='/sensor/data',max_retries = 3,size=5000):
    """Fetch all data from the Fission function using scroll API with retry on timeout."""
    data = []
    url = base_url + initial_path
    params = {'size': size}

    while True:
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()  
            result = response.json()
            if not result.get('data'):
                print("No more results found")
                break
            data.extend(result['data'])
            scroll_id = result.get('scroll_id')
            print(f"{size} records get.")
            if not scroll_id:
                print("No more results found")
                break       
            params['scroll_id'] = scroll_id
            params['size'] = size

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
    all_data = fetch_all_data(FISSION_ROUTER)
    print(f"Retrieved {len(all_data)} records")