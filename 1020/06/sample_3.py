# 初期化
marks = ('S','H','C','D') # 4 種類のマーク
cards = [] # デッキ用リスト
for m in marks:
    for i in range(13):
        cards.append([m,i+1])
print('-'*10)
print(cards)
print('-'*10)
# 1 枚選択
import random # 乱数用モジュール
r = random.randrange(52) # 0〜51 の乱数生成
print(f'選んだカードは{cards[r]}です')