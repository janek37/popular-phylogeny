import itertools
import json

from data import LIFE

if __name__ == "__main__":
    print(json.dumps(LIFE.serialize(itertools.count())))
