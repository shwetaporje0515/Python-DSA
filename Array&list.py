# Problem 1 : Given an array with some integer type values. Write a python script to sort array values

# Here two built-in functions are provided by python : sorted() and .sort()


# 1) sorted() :

arr = [5,10,2,79,3,4,56]

# sorted_arr = sorted(arr)
# print("sorted array is : ",sorted_arr)            or ->

print(sorted(arr))

# 2) .sort() :

arr1 = [10,45,11,96,45,75,13]
arr1.sort()

print("sorted array is : ",arr1)

    # To print array in descending order:

arr1.reverse()
print(arr1)

# sorting the string :

arr2 = ["b", "a", "d", "z", "e"]
arr2.sort()
print("sorted string array is:",arr2)

arr2.reverse()
print("sorted reverse string is: ",arr2)

# To reverse the given string: 

arr3 = ["shweta is a girl"]
arr3.sort()
arr3.reverse()
print(arr3)                     # not giving o/p



# ===============================================================================================================================================


# Problem 2 : Given a list of heterogeneous element. Write a python script to remove all non int value from list
# Heterogeneous list : mixed list of different datatypes
# isinstance is used : isinstance(object, type)

list1 = [10 , 20, "shweta", 10.5, -10, True, "hello"]

int_list = [x for x in list1 if isinstance(x, int) and not isinstance(x, bool)]
print("integere list : ",int_list)

    
    #to print only positive integers 
int_list1 = [x for x in list1 if isinstance(x, int) and not isinstance(x, bool) and x>0]
print("positive integere list : ",int_list1)

avg = sum(int_list1) / len(int_list1)
print("average of int list : ",avg)


# ============================================================================================================================================= 


# Problem 3 : Python program to calculate average of elements of a list

list2 = [15, 92, 23, 44, 65]

len = len(list2)
print("length of list2 : ",len)
sum = sum(list2)
print("sum of list2 : ",sum)

average = sum / len
print("average of list : ", average)

average1 = round(sum / len)             #to round off decimal no. upto 2 decimal point
print("rounded average of list 2 : ",average1)         


# =================================================================================================================================


# # Problem 4 : To create a list of First 'n' prime numbers


# n = int(input("enter the number to get prime numbers : "))
# # print(numbers(n))

# def n_prime(n):
#     primes = []
#     nm = 2

#     while len(primes) < n:
#         is_prime = True

#         for i in range(2, nm):
#         # for i in range(2, int(nm ** 0.5) + 1):
#             if nm % i == 0:
#                 is_prime = False
#                 break
            
#             # else:
#             #     primes.append(nm)
        
#         if is_prime:
#             primes.append(nm)
#         nm += 1
#     return primes

# # print("list of", n , "prime numbers is : " , numbers(n))

# print(n_prime(n))  
    
    #    enter the number to get prime numbers :  10
    #    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]



# ========================================================================================================


# Problem 5 : write a python script to create a list of n terms of fibonacci series

n = int(input("enter the number upto which you want the fib no series : "))

def fibonacci(n):
    if n <= 0:
        return []
    
    fib = [0, 1]
    for _ in range (n-2):
        fib.append(fib[-1] + fib[-2])
    
    return fib[:n]

print(fibonacci(n)) 
        