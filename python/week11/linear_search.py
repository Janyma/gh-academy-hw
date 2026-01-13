def linear_search(list_, target):
    if len(list_) == 0:
        return -1
    else:
        for i in range(len(list_)):
            if list_[i] == target:
                return i
        return -1
    
if __name__ == "__main__":
    my_list= [2, 4, 1, 7,4]
    target = 7
    result = linear_search(my_list, target)

    if (result != -1):
        print(f"Element found at index {result}")
    else:
        print("Not found")

