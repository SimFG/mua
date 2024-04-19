from dotenv import load_dotenv

from mucli._milvus import milvus_cli


def main():
    load_dotenv()
    milvus_cli()


if __name__ == "__main__":
    main()
