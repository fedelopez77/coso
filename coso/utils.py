import json

BUFFER_SIZE = 64 * (1024 ** 2)


def get_jsonl_data(path):
    with open(path, "r", buffering=BUFFER_SIZE) as f:
        return [json.loads(line) for line in f]
