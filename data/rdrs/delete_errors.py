import json

corrected_text = "Отзыв: Мазь для наружного применения Вертекс \"Клотримазол\" - эффективное средство\nЭто очень эффективное противогрибковое средство, для наружнего приминения. Если у вас на ногах появился грибок, то КЛОТРИМАЗОЛ вам поможет. Мазь нужно наносить тонким слоем на кожу 2-3 раза в день, но перед тем как нанести мазь, нужно хорошо промыть и высушить кожу, и только потом можно наносить средство. Продолжение пользования этим средством, зависит от тяжести вашего грибкового заболевания. Ну примерное применение по времени, от одной до четырёх недель. Мне он помог за полтары недели. Срок годности у него два года. Передозировки нет. Продается это средство без рецепта врача. Побочные эффекты-Зуд, жжение покалывания в местах нанесения",

def delete_error(path_to_data):
    # Load the data from the JSON file
    with open(path_to_data, 'r') as f:
        data = json.load(f)

    # Iterate over the list and remove the dictionary if the 'text_id' is '862354'
    data = [d for d in data if d.get('text_id') != '862354']
    # for d in data:
    #     if d.get('text_id') == '862354':
    #         d['text'] = corrected_text

    # Write the modified data back to the JSON file
    with open(path_to_data, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    for i in range(1,6):
        path_to_data = f'data/interim/{i}/train.json'
        delete_error(path_to_data)