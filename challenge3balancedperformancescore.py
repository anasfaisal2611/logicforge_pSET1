def findMedianSortedArrays(scoresA, scoresB):
    # Ensure A is smaller array
    if len(scoresA) > len(scoresB):
        scoresA, scoresB = scoresB, scoresA

    m, n = len(scoresA), len(scoresB)
    low, high = 0, m

    while low <= high:
        # Partition positions
        partA = (low + high) // 2
        partB = (m + n + 1) // 2 - partA

        # Left and Right values
        maxLeftA = float("-inf") if partA == 0 else scoresA[partA - 1]
        minRightA = float("inf") if partA == m else scoresA[partA]

        maxLeftB = float("-inf") if partB == 0 else scoresB[partB - 1]
        minRightB = float("inf") if partB == n else scoresB[partB]

        # Correct partition found
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            # Odd total length
            if (m + n) % 2 == 1:
                return float(max(maxLeftA, maxLeftB))
            # Even total length
            else:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2

        # Move left
        elif maxLeftA > minRightB:
            high = partA - 1

        # Move right
        else:
            low = partA + 1
if __name__ == "__main__":
    scoresA = list(map(int, input("Enter scores of Team A: ").split()))
    scoresB = list(map(int, input("Enter scores of Team B: ").split()))

    median = findMedianSortedArrays(scoresA, scoresB)
    print("Median Score:", median)
