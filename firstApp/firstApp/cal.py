def cal():
    print("cal")
    x=int(input("enter valueof one:"))
    y=int(input("enter value of second:"))
    print("press 1 for add\n press 2 for sub\n press 3 for mul\n press 4 for div")
    option = int(input("==>"))


    def add():
        res=x + y
        print(res)
    def sub():
        res=x - y
        print(res)
    def mul():
        res=x * y
        print(res)
    def div():
        res=x / y
        print(res)
    if(option ==1):
        add()
    elif(option ==2):
        sub()
    elif(option ==3):
        mul()
    elif(option ==4):
        div()
cal()