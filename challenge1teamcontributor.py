import heapq


def kthSmallest(matrix, k):
    n = len(matrix)
    # Min-heap
    heap = []
    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))

    for _ in range(k):
        value, r, c = heapq.heappop(heap)

        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return value
if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print("Kth Smallest Element:", kthSmallest(matrix, k))
