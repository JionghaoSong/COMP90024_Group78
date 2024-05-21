from flask import jsonify, request
from elasticsearch8 import Elasticsearch

def main():
    es = Elasticsearch(
        'https://elasticsearch-master.elastic.svc.cluster.local:9200',
        verify_certs=False,
        ssl_show_warn=False,
        basic_auth=('elastic', 'elastic')
    )

    scroll_id = request.args.get('scroll_id')
    size = request.args.get('size', default=5000, type=int)  

    try:
        if scroll_id is None:
            res = es.search(
                index="weather_station",
                scroll='1m', 
                size=size,  
                body={
                    "query": {"match_all": {}}
                    # "_source": ["sentiment", "created_at"]
                }
            )
        else:
            res = es.scroll(scroll_id=scroll_id, scroll='1m')

        scroll_id = res.get('_scroll_id')
        hits = res['hits']['hits']
        if hits:
            return jsonify({
                'scroll_id': scroll_id,
                'data': hits
            })
        else:
            return jsonify({'message': 'No more results found'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
