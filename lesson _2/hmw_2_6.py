goods = []
features = {'Имя': '', 'Цена': '', 'Количество': '', 'ед.': ''}
analytics = {'Имя': [], 'Цена': [], 'Количество': [], 'ед.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', Чтобы продолжить нажмите 'Enter', Для просмотра аналитики нажмите 'A': ").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите значение "{f}": ')
        features[f] = float(feature_) if (f == 'Количество' or f == 'Цена') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
