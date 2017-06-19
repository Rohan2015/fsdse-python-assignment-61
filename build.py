def solution(list_of_nums):
    even_count = 0
    odd_count = 0
    for i in list_of_nums:
        if i%2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    #print even_count, odd_count
    keys = ['ODD','EVEN']
    values = [odd_count,even_count]
    dic = dict(zip(keys,values))
    #print d
    return dic

solution([1, 2, 3, 5, 8, 9])
