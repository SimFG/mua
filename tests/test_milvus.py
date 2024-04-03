from milvus_connector.core.milvus import Milvus


def test_milvus():
    m = Milvus()
    m.show_collections()
    # print(m.json().list_collections())
