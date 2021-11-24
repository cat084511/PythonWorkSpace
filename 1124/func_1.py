def combine_list(list1, list2):
    if type(list1) is list and type(list2) is list:
       return list1+list2
    else:
        print("引数がリストではありません")
        return [str(list1),str(list2)]
# main
# 正常な引数
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz'))
print(combine_list(10, 'abc'))