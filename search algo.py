def first(x,y):
    result = ""
    x1 = len(x)
    y1 = len(y)
    i = 0
    j = 0
    while i <= x1 - 1 and j <= y1 - 1 :
        if x[i] != y[j]: break
        result += x[i]
        i = i + 1
        j = j + 1
    return result

def second(array,low,high):
    if low == high: return array[low]
    if high > low :
        mid = (low + high) // 2

        x = second(array,low,mid)
        y = second(array,mid+1,high)

        return first(x,y)

def run():
    array = ['hayqwe','hayasd','hayzxc']
    n = len(array)
    answer = second(array,0,n-1)
    if len(answer):print("The longest common prefix is ",answer)
    else:print("NO MATCH FOUND!!!")
    #return answer

run()
