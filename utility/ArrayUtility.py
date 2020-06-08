import json

def stringToChar2dArray(input):
    return json.loads(input)


if __name__ == "__main__":
    print(stringToChar2dArray('[["a", "b"], ["c", "d"]]'))