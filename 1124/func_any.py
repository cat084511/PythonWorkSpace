def out_csvdata(**kwargs):
    print([kwargs[x] if x in kwargs else '-' for x in ['B','L','D']])

# main
eat = {}
while True:
    menu = input('朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：')
    if menu == '':
        break
    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        eat[token] = menu
    else:
        print('記号が間違っています。登録しません')
        continue
out_csvdata(**eat)