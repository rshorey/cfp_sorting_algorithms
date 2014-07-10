import itertools
import random


#easiset way to use:
#permute_sort(rand_list(10))
#bubble_sort(rand_list(10))


def permute_sort(numbers):
    permutations = itertools.permutations(numbers) #finds every permutation of the list
    for p in permutations:
        num_correctly_ordered = 1 #so we can count how many are in the right order.
        #index starting with 1 bc we're counting comparisons, so we'll end up
        #with 1 less than the length of the list in the end than the length of the list
        
        for i in range(1,len(p)):
            if p[i] < p[i-1]:
                break #there's an unsorted pair, so the list is no good
            else:
                num_correctly_ordered += 1 #the pair is correctly sorted
                
        if num_correctly_ordered == len(p): #every element is in the right order, so we return
            return p
            
            
    
def bubble_sort(numbers):
    pos = 1 #the original position of the number we're comparing
    while pos < len(numbers):
        new_pos = pos #the position of the number we're comparing after it has moved
        while new_pos > 0:
            if numbers[new_pos] < numbers[new_pos-1]: #numbers are in wrong order
                
                #reorder numbers
                swap_num = numbers[new_pos]
                numbers[new_pos] = numbers[new_pos-1]
                numbers[new_pos-1] = swap_num
                
                #reset position
                new_pos -= 1
                
            else: #get out of inner loop and start working on the next number
                new_pos = 0
                pos += 1
                
    return numbers

def rand_list(n,low=0,high=10000): #get a random list for sorting of length n
    return [random.randint(low,high) for x in range(0,n)]
    