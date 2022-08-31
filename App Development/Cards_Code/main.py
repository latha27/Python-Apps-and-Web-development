import random

cards = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
cards_list = list(cards.keys())

N=6

A=''.join(random.choice(cards_list) for _ in range(N))
B=''.join(random.choice(cards_list) for _ in range(N))
print("Alec cards:", A)
print("Bob  cards:", B)

def solution(A, B):

    alecwins = 0
    for i in list(range(len(A))):
        if (cards[A[i]] > cards[B[i]]):
            alecwins = alecwins+1
    return alecwins
print(solution(A, B))




