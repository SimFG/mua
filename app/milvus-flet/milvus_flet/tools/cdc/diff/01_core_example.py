"""
db --> collection --> partition

status:
entities num
load status
index status


then load partition
query all data
compare result

"""

from loguru import logger
import json
import collections.abc
from deepdiff import DeepDiff
from pymilvus import connections, Collection, db, list_collections
import threading


def convert_deepdiff(diff):
    if isinstance(diff, dict):
        return {k: convert_deepdiff(v) for k, v in diff.items()}
    elif isinstance(diff, collections.abc.Set):
        return list(diff)
    return diff


def get_collection_info(info, db_name, c_name, enable_compact):
    info[db_name][c_name] = {}
    c = Collection(c_name)
    if enable_compact:
        # flush and compact
        # logger.info(f"start flush and compact {db_name}.{c_name}")
        try:
            c.flush(timeout=10)
            c.compact(timeout=10)
            # logger.info(f"finished flush and compact {db_name}.{c_name}")
        except Exception as e:
            logger.warning(f"failed to flush and compact {db_name}.{c_name}: {e}")
    info[db_name][c_name]['name'] = c.name
    # logger.info(c.num_entities)
    info[db_name][c_name]['num_entities'] = c.num_entities
    # logger.info(c.schema)
    info[db_name][c_name]['schema'] = len([f.name for f in c.schema.fields])
    # logger.info(c.indexes)
    info[db_name][c_name]['indexes'] = [x.index_name for x in c.indexes]
    # logger.info(c.partitions)
    info[db_name][c_name]['partitions'] = len([p.name for p in c.partitions])
    try:
        replicas = len(c.get_replicas().groups)
    except Exception as e:
        logger.warning(e)
        logger.info(f"no replica for {db_name}.{c_name}")
        replicas = 0
    # logger.info(replicas)
    info[db_name][c_name]['replicas'] = replicas
    if replicas > 0:
        try:
            # logger.info(f"start query {db_name}.{c_name}")
            res = c.query(expr="", output_fields=["count(*)"], timeout=60)
            cnt = res[0]["count(*)"]
            # logger.info(cnt)
            info[db_name][c_name]['cnt'] = cnt
        except Exception as e:
            logger.warning(f"failed to query {db_name}.{c_name}: {e}")
            info[db_name][c_name]['cnt'] = -1

def get_cluster_info(host, port, user, password, enable_compact=False):
    try:
        connections.disconnect(alias='default')
    except Exception as e:
        logger.warning(e)
    if user and password:
        connections.connect(host=host, port=port, user=user, password=password)
    else:
        connections.connect(host=host, port=port)
    info = {}
    all_db = db.list_database()
    collection_cnt = 0
    # logger.info(f"db num: {len(all_db)}, all db: {all_db}")
    for db_name in all_db:
        info[db_name] = {}
        db.using_database(db_name)
        all_collection = list_collections()
        # logger.info(all_collection)
        threads = []
        collection_cnt += len(all_collection)
        for collection_name in all_collection:
            t = threading.Thread(target=get_collection_info, args=(info, db_name, collection_name, enable_compact))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    # logger.info(f"collection cnt: {collection_cnt}")
    # logger.info(json.dumps(info, indent=2))
    return info

def diff(upstream_host, upstream_port, downstream_host, downstream_port, user, password, enable_compact):
    upstream = get_cluster_info(upstream_host, upstream_port, user, password, enable_compact)
    downstream = get_cluster_info(downstream_host, downstream_port, user, password, enable_compact)
    diff = DeepDiff(upstream, downstream)
    diff = convert_deepdiff(diff)
    excludedRegex = [r"root(\[\'\w+\'\])*\['num_entities'\]"]
    diff = DeepDiff(upstream, downstream, exclude_regex_paths=excludedRegex)
    diff = convert_deepdiff(diff)
    return json.dumps(diff, indent=2)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='connection info')
    parser.add_argument('--upstream_host', type=str, default='10.100.36.179', help='milvus host')
    parser.add_argument('--downstream_host', type=str, default='10.100.36.178', help='milvus host')
    parser.add_argument('--upstream_port', type=str, default='19530', help='milvus host')
    parser.add_argument('--downstream_port', type=str, default='19530', help='milvus host')
    parser.add_argument('--port', type=str, default='19530', help='milvus port')
    parser.add_argument('--user', type=str, default='', help='milvus user')
    parser.add_argument('--password', type=str, default='', help='milvus password')
    parser.add_argument('--enable_compact', type=bool, default=False, help='enable compact')
    args = parser.parse_args()
    res = diff(args.upstream_host, args.upstream_port, args.downstream_host, args.downstream_port, args.user, args.password, args.enable_compact)
    # logger.info(f"diff exclude num entities: {diff}")
    logger.info(f"diff exclude num entities: {res}")
    # if diff:
    #     assert False, f"diff exclude num entities found between upstream and downstream {json.dumps(diff, indent=2)}"

import flet as ft

name = "Diff upstream and downstream milvus"

def example():
    up_host = ft.TextField(label="Upstream host", value="", col=8)
    up_port = ft.TextField(label="Upstream port", value="19530", col=4)
    down_host = ft.TextField(label="Downstream host", value="", col=8)
    down_port = ft.TextField(label="Downstream port", value="19530", col=4)
    user = ft.TextField(label="User", value="root", col=5)
    password = ft.TextField(label="Password", value="Milvus", col=5)
    enable_compact = ft.Checkbox(label="Enable compact", value=False, col=2)
    diff_result = ft.TextField(label="Diff result", value="", read_only=True, multiline=True, min_lines=10,)

    async def diff_click(e):
        diff_result.value = diff(up_host.value, up_port.value, down_host.value, down_port.value, user.value, password.value, enable_compact.value)
        await diff_result.update_async()
    diff_btn = ft.TextButton("Diff", icon=ft.icons.SEARCH, on_click=diff_click)

    return ft.Column([
        ft.ResponsiveRow([
            up_host, up_port, down_host, down_port
            ]),
        ft.ResponsiveRow([
            user, password, enable_compact
            ]),
        diff_btn,
        diff_result,
    ])