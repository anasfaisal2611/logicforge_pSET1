import heapq

def kthSmallest(matrix, k):
    n = len(matrix)
    
    # Min-heap banayenge
    heap = []
    
    # Step 1: har row ka first element heap mein daalo
    for row in range(n):
        # (value, row_index, column_index)
        heapq.heappush(heap, (matrix[row][0], row, 0))
    
    # Step 2: k times pop karo
    for _ in range(k):
        value, r, c = heapq.heappop(heap)
        
        # Step 3: agar us row mein next element hai
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    
    return value


# 🔽 Client Code / Driver Code
if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    
    print("Kth smallest element is:", kthSmallest(matrix, k))
