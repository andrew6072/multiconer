import json
import argparse
from nltk.tokenize import word_tokenize


def parse_args():
    p = argparse.ArgumentParser(description='Data converting.', add_help=False)
    p.add_argument('--path_data', type=str,
                   help='Path to the data.', default=None)
    p.add_argument('--path_output', type=str,
                   help='Path to the output.', default='./rdrs_converted.conll')
    p.add_argument('--domain', type=str,
                   help='Domain of file.', default=None)
    return p.parse_args()


def get_pos_span(text, begin, end):
    cut1 = text[0:begin]
    span = text[begin:end]
    begin_pos = len(word_tokenize(cut1))
    end_pos = begin_pos + len(word_tokenize(span)) - 1
    return begin_pos, end_pos


def convert_data(path_to_data, path_to_output, domain):
    with open(path_to_data, 'r', encoding='utf-8') as f:
        data = json.load(f)

    documents = data
    list_fields = []
    for document in documents:
        # print(document['text_id'])

        entities = document['entities']

        text = document['text']

        words = word_tokenize(text)
        
        labels = ['O'] * len(words)
        
        

        # print(text)
        # print()
        # print(words)
        # print("Words len:",len(words))
        # print("Labels len:",len(labels))
        # print()

        for no_entity, entity in entities.items():
            label = entity['MedEntityType']
            is_first_word_in_span = True
            for span in entity['spans']:
                begin_pos, end_pos = get_pos_span(
                    text, span['begin'], span['end'])
                # print(no_entity, text[span['begin']:span['end']],
                #       begin_pos, end_pos, label)
                for i in range(begin_pos, end_pos+1):
                    labels[i] = 'I-' + label
                if is_first_word_in_span:
                    labels[begin_pos] = 'B-' + label
                    is_first_word_in_span = False

        fields = list([words, ['_']*len(words), ['_']*len(words), labels])
        fields = [f'# id {document["text_id"]}\tdomain={domain}'] + \
            [list(field) for field in zip(*fields)]
        list_fields.append(fields)

        # print()

    with open(path_to_output, 'w', encoding='utf-8') as f:
        data_str = []
        for _, fields in enumerate(list_fields):
            str_fields = []
            str_fields.append(fields[0])
            for i in range(1, len(fields)):
                str_fields.append(' '.join(fields[i]))
            str_fields = '\n'.join(str_fields)
            data_str.append(str_fields)
        data_str = '\n\n'.join(data_str)
        f.write(data_str)


if __name__ == '__main__':
    # sg = parse_args()
    # convert_data(path_to_data=sg.path_data,
    #              path_to_output=sg.path_output, domain=sg.domain)

    domains = ['test', 'train', 'valid']
    for i in range(1,6):
        print(i)
        for domain in domains:
            print(domain)
            convert_data(path_to_data=f"data/interim/{i}/{domain}.json", path_to_output=f"proccessed_data/{i}/{domain}.conll", domain=domain)
        
    # convert_data(path_to_data='data/interim/1/train.json',
    #              path_to_output='./rdrs_converted.conll', domain='domain')
