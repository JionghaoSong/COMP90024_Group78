from flask import jsonify
from elasticsearch import Elasticsearch

def main():
    es = Elasticsearch(
            'https://elasticsearch-master.elastic.svc.cluster.local:9200',
            verify_certs=False,
            ssl_show_warn=False,
            basic_auth=('elastic', 'elastic')
        )
    try:
        res = es.search(index="liquor", body={
            "query": {
                "match_all": {}
            }
        })
        if res['hits']['hits']:
            return jsonify(res['hits']['hits'])
        else:
            return jsonify({'message': 'No results found'}) 
    except Exception as e:
        return jsonify({'error': str(e)}), 500