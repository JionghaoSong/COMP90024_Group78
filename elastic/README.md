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
python3 create_mastodon.py

```

## Insert data
```
python3 insert_mastodon.py

```