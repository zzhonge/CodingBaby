H, W = map(int,input().split())
CHESS = []
new_CHESS = []
for i in range(H):
    CHESS.append((input()))

for i in CHESS:
    for k in range(len(i)-7):
        for j in CHESS:
            new_CHESS.append(j[k:k+8])
print(new_CHESS)