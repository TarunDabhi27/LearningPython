import  json
if __name__ == '__main__':
    with open('sample.json') as f:
        data = json.load(f)
        print(data)