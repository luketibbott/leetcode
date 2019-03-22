class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for _ in range(K):
            i = A.index(min(A))
            A[i] *= -1
            
        return sum(A)