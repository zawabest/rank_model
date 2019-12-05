#!/usr/bin/env python
# coding: utf-8

import argparse
import pandas as pd
from pandasticsearch import DataFrame, Select
from elasticsearch import Elasticsearch
# xfrom elasticsearch.helpers import bulk, parallel_bulk
from tool.sink import ESSink

parser = argparse.ArgumentParser()
parser.add_argument('-es', help='ES host', type=str)
parser.add_argument('-name', help='ES user', type=str)
parser.add_argument('-password', help='ES password', type=str)
parser.add_argument('-index', help='ES table', type=str)
parser.add_argument('-cols', help='table wide', type=int, default=10)
parser.add_argument('-lines', help='table count', type=int, default=10)
group = parser.add_mutually_exclusive_group()
group.add_argument('-push', help='push test', action="store_true")
group.add_argument('-pull', help='push test', action="store_true")

args = parser.parse_args()
print('[params]', args)

host = args.es # '115.29.34.243:9200'
username = args.name # 'elastic'
password = args.password # 'superzsh123'
tablename = args.index # 'bigtable'
cols = args.cols # 100
lines = args.lines # 3000

es = Elasticsearch(
    [host],
    http_auth=(username, password)
)

if args.push:
    print("create data...")
    df = pd.DataFrame([[1]*cols]*lines)
    test_df = ESSink(df, es)

    print("push es...")
    test_df.to_es(tablename)

if args.pull:
    print("pull es...")
    data = es.search(index=tablename, body={"size":lines})
    data_df = Select.from_dict(data).to_pandas().drop(['_index', '_type', '_id', '_score'], axis=1)
    print(data_df.head(), data_df.shape)
    data_df.to_csv('save/'+tablename+'.csv', index=None)

print('done')
