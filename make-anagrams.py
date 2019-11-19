#Run code with Python installed 
 
def permutations(A, B = ''):
    assert len(A) >= 0
    assert len(A) == len(set(A))
    if len(A) == 0:
        return [B]
    else:
        result = []
        for i in range(len(A)):
            result.extend(permutations ( A[0:i] + A[i + 1:], B + A[i] ))
        return result
        
print(permutations('focus'))
