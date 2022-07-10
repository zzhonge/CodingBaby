N = int(input())
wordlist = []
for i in range(N):
    A = input()
    wordlist.append(A)

wordlist2 = set(wordlist)
wordlist2 = list(wordlist2)

wordlist3 = []
for i in wordlist2:
    wordlist3.append((len(i),i))
wordlist3.sort()

for len,i in wordlist3:
    print(i)