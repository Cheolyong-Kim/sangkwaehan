from collections import Counter
import random

# 랜덤한 키워드를 출력하는 함수
# keyword_list에서 빈도수가 높게 나오는 단어를 10개 뽑고 그 리스트를 섞은 후 5개만 출력
def print_random_keyword(keyword_list):
    maximum = []
    cnt = Counter(keyword_list)
    order = cnt.most_common(10)

    for i in order:
        maximum.append(list(i)[0])

    random.shuffle(maximum)
    return maximum[:5]
