# Prerequisite

```
pip intsall elasticsearch
pip install dotenv

// forwarding 9200 to localhost
kubectl port-forward service/elasticsearch-master -n elastic 9200:9200
```

# Run

## Create index
```
python3 create_pedeatrain.py
python3 create_liquor.py
python3 create_mastodon.py
```

## Insert data
```
python3 insert_pedeatrain.py
python3 insert_liquor.py
python3 insert_mastodon.py
```

# Geo-data reference
https://cloud.tencent.com/developer/article/1050321