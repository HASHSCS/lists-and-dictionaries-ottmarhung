# TODO: Implement a function that returns a list of numbers from 1 to n
def generate_numbers(n):
    a = []
    if n != 0:
        for i in range(1,n+1):
            a.append(i)
        return a
    else:
        return 0

# TODO: Implement a function that returns a dictionary where keys are numbers from 1 to n and values are their squares
def generate_squares(n):
        a = {}
        b = 0
        if n != 0:
            for i in range(1,n+1):
                b = i
                a[i] = b*b
            return a
        else:
            return 0

# TODO: Implement a function that merges two lists in an alternating fashion
def merge_lists(list1, list2):
    list3 =[]
    i = 0
    if len(list1)>= len(list2):
        for n in range(0,len(list2)):
            list3.append (list1[i])
            list3.append (list2[i])
            i+=1
        for n in range (0, len(list1)-len(list2)):
            list3.append (list1[i])
            i+=1
        return(list3)
    else:
        for n in range(0,len(list1)):
            list3.append (list1[i])
            list3.append (list2[i])
            i+=1
        for n in range (0, len(list2)-len(list1)):
            list3.append (list2[i])
            i+=1
        return(list3)

# TODO: Implement a function that returns a list and replicates the dictionary keys based on their respective values
def multiply_keys(data):
    i = 0
    a = []
    for i in data:
        for n in range(0, data[i]):
            a.append(i)
            print(a)
    return(a)


# TODO: Implement a function that converts a list of strings to a dictionary with the string as the key and its length as the value
def list_to_dict(items):
    dic = {}
    for i in items:
        dic[i] = len(i)
    return dic


# TODO: Implement a function to find the majority element in a list
def majority_element(nums):
    max_num = 0
    max_key = nums[0]
    dic = {}
    for i in nums:
        print(dic)
        if i in dic:
            dic[i]+= 1
        else:
            dic[i]=1
    for i in dic:
        if dic[i] >max_num:
            max_num = dic[i]
            max_key = i
    return max_key
# TODO: Implement a function that filters a dictionary based on a threshold value. If the value of any key in the dictionary is greater than the threshold, that key-value pair should be retained in the output dictionary. Otherwise, it should be excluded.
def filter_dictionary(data, threshold):
    pass
