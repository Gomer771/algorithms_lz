import random

def main():
    my_list=[] 
    counter=0
    for i in range(1,101):
        my_list.append(random.randint(1,1000000))
    print(my_list)
    print('-'*200)
    for i in range(99):
        for j in range(99-i):
            counter+=1
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j] 
                print(my_list)
    print(counter)

main()

