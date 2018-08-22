import json
from collections import defaultdict
from operator import itemgetter

BUFFER_SIZE = 64 * (1024 ** 2)


def load_jsonl(path):
    with open(path, "r", buffering=BUFFER_SIZE) as f:
        return [json.loads(line) for line in f]


def export_jsonl(path, data):
    with open(path, "w", buffering=BUFFER_SIZE) as fp:
        for res in data:
            fp.write(json.dumps(res) + "\n")


def load(path):
    with open(path, "r", buffering=BUFFER_SIZE) as f:
        return f.readlines()


def export(path, data):
    with open(path, "w", buffering=BUFFER_SIZE) as fp:
        for res in data:
            fp.write(res + "\n")


def count_freqs(data):
    freqs = defaultdict(int)
    for item in data:
        freqs[item] += 1
    return freqs


def order_freqs(freqs, reverse=True):
    return sorted(freqs.items(), key=itemgetter(1), reverse=reverse)
