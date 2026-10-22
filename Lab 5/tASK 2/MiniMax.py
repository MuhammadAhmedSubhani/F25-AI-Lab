import math

count = 0

def minimax(
             Depth, node, max1 ,scores, Target
        ):
    
    global count
    
    if Depth == Target:
        count += 1
        return scores[ node ]
    
    if max1:
        return max(
            minimax( Depth + 1, node * 2, False, scores, Target ),
            minimax( Depth + 1, node * 2 + 1, False, scores, Target )
        )
    else:
        return min(
            minimax( Depth + 1, node * 2, True, scores, Target ),
            minimax( Depth + 1, node * 2 + 1, True, scores, Target )
        )

scores = [
        3, 5, 2, 9, 0, 7
    ]

treeDepth = math.ceil(math.log2(len(scores)))

scores += [0] * ( 2**treeDepth - len(scores) )

result = minimax(0, 0, True, scores, treeDepth)

print("Value:", result)
print("Count:", count)