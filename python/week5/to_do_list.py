def to_do():
    to_do_list=[]
    while(True):
        command=input("please give the command")
        if(command=="add"):
            a=input("Please give the task name: ")
            to_do_list.append(a)
        if(command=="view"):
            print(to_do_list)
        if(command=="delete"):
            b=input("Please give the name of task which you want to delete: ")
            if(b in to_do_list):
                to_do_list.remove(b)
        if(command=="exit"):
            return "Bye"
    
    
print(to_do())

    