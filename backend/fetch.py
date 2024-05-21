import requests

def fetch_all_data(base_url, initial_path='/liquor-fetch'):
    """Fetch all data from the Fission function using scroll API."""
    data = []
    url = base_url + initial_path
    params = {}
  
    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching data: {response.text}")
            break
        
        result = response.json()
        if not result.get('data'):
            print("No more results found")
            break
        
        data.extend(result['data'])
        scroll_id = result.get('scroll_id')
        if not scroll_id:
            print("No more results found")
            break
        # Update params for the next request with the new scroll_id
        params['scroll_id'] = scroll_id
    return data

if __name__ == '__main__':
    FISSION_ROUTER = 'http://127.0.0.1:9090'  # Replace with your Fission router URL
    all_data = fetch_all_data(FISSION_ROUTER,'/liquor-fetch')
    print(f"Retrieved {len(all_data)} records")
