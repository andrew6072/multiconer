import json
import uuid
import argparse


def parse_args():
    p = argparse.ArgumentParser(description='Data converting.', add_help=False)
    p.add_argument('--path_to_data', type=str,
                   help='Path to the data.', default=None)
    p.add_argument('--path_to_output', type=str,
                   help='Path to the output.', default=None)
    p.add_argument('--domain', type=str,
                   help='Domain of file.', default=None)
    return p.parse_args()


def convert_data(path_to_data, path_to_output, domain):
    with open(path_to_data, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data_list = []
    for _, dict_sent in enumerate(data):
        sent = dict_sent['sentence'].strip().split()
        sent_len = len(sent)
        sent_labels = ['O'] * sent_len

        for label in dict_sent['seq_label']:
            begin_pos = label[0]
            end_pos = label[1]
            label_name = label[2]
            sent_labels[begin_pos] = 'B-' + label_name
            for i in range(begin_pos + 1, end_pos + 1):
                if 0 <= i < sent_len:
                    sent_labels[i] = 'I-' + label_name

        fields = list([sent, ['_']*sent_len, ['_']*sent_len, sent_labels])
        id4 = uuid.uuid4()
        fields = [f'# id {id4}\tdomain={domain}'] + \
            [list(field) for field in zip(*fields)]
        data_list.append(fields)

    with open(path_to_output, 'w', encoding='utf-8') as f:
        data_str = []
        for _, fields in enumerate(data_list):
            str_fields = []
            str_fields.append(fields[0])
            for i in range(1, len(fields)):
                str_fields.append(' '.join(fields[i]))
            str_fields = '\n'.join(str_fields)
            data_str.append(str_fields)
        data_str = '\n\n'.join(data_str)
        f.write(data_str)


if __name__ == '__main__':
    sg = parse_args()
    convert_data(path_to_data=sg.path_to_data,
                 path_to_output=sg.path_to_output, domain=sg.domain)
