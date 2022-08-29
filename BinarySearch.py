def linear_search(array,value):
    for i in array:
        print(i)
        if i == value:
            return  f"Value Found at index {array.index(i)}"
        
    return "Not Found"


def binary_search(array,value):
    left_index=0
    right_index = len(array) -1 
    mid_index = 0
    
    for i in range(len(array)):
        print(i)
        mid_index=(left_index + right_index) //2
        if value == array[mid_index]:            
            return f"Value Found at index {mid_index}"
        if array[mid_index] > value:
            right_index = mid_index - 1
            # print("Greater")
            # print(mid_index)
            # print(array[mid_index])
        else:
            left_index = mid_index + 1
            # print("Less")
            # print(array[mid_index])
            # print(mid_index)
    return -1


def binary_search_recursion(array,value,left_index,right_index):
    mid_index=(left_index + right_index)//2
    if value == array[mid_index]:
        return f"Value Found at index {mid_index}"
    if value > array[mid_index]:
        left_index+=1
        return binary_search_recursion(array,value,left_index,right_index)
    else:
        right_index-=1
        return binary_search_recursion(array,value,left_index,right_index)
            
    
        

# print(linear_search([1,2,3,4,5,6,7,8,9,10],10))
# print(binary_search([1,2,3,4,5,6,7,8,9,10],10))
array=[1,2,3,4,5,6,7,8,9,10]
print(binary_search_recursion(array,3,0,(len(array)-1)))