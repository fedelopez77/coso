import json

BUFFER_SIZE = 64 * (1024 ** 2)


def load_jsonl(path):
    with open(path, "r", buffering=BUFFER_SIZE) as f:
        return [json.loads(line) for line in f]


def export_jsonl(path, data):
    with open(path, "w", buffering=BUFFER_SIZE) as fp:
        for res in data:
            fp.write(json.dumps(res) + "\n")
