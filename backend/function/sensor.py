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
    try:
        if scroll_id is None:
            res = es.search(
                index="sensor_data",
                scroll='1m', 
                size=100,  
                body={"query": {"match_all": {}}}
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