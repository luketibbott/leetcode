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

        if num_this_candy%2 == 0:
            num_sister += num_this_candy

    return num_sister

candies = [1, 1, 2, 3]

print(dist_candies(candies))