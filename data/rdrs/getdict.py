import json

if __name__ == '__main__':
    path_to_data = 'data/interim/1/train.json'
    with open(path_to_data, 'r', encoding='utf-8') as f:
            data = json.load(f)

    documents = data
    for document in documents:
        if document['text_id'] == "4690641":
            with open('utils/data.json', 'w', encoding='utf-8') as f:
                json.dump(document, f, ensure_ascii=False, indent=4)
            exit()
        
