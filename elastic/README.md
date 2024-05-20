# Prerequisite

```
pip install elasticsearch
pip install python-dotenv

// forwarding 9200 to localhost
kubectl port-forward service/elasticsearch-master -n elastic 9200:9200
```

# Run

## Create index
```
python3 create_weather.py
python3 create_pedestrain.py
python3 create_liquor.py
python3 create_mastodon.py
python3 create_crash.py
```

## Insert data
```
python3 insert_weather.py
python3 insert_pedestrain.py
python3 insert_liquor.py
python3 insert_mastodon.py
python3 insert_crash.py
```


