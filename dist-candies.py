from collections import Counter

def distribute_candies(candies):
    num_candies = Counter(candies)
    unique_candies = len(set(candies))
    num_sister = 0
    
    for candy in num_candies.keys():

        num_this_candy = num_candies[candy]
        if num_this_candy%2 == 0:
            unique_candies -= 1
            num_sister += num_candies[candy]

    return num_sister


def dist_candies(candies):

    # Lowest possible occurs when brother gets half and sister gets half
    num_sister = len(set(candies))//2

    num_candies = Counter(candies)

    for candy in num_candies.keys():
        num_this_candy = num_candies[candy]

        if num_this_candy%2 == 1:
            num_sister += 1

    return num_sister

def dist_candies2(candies):
    # Case when there's only one of half the candies
    max_sister = len(candies)/2

    return min(max_sister, len(set(candies)))
    

    


candies = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 10, 11, 12, 13, 14, 15]

print(dist_candies2(candies))