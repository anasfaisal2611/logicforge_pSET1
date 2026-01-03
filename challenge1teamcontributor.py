def teamContribution(contributions):
    n = len(contributions)
    
    # Output array
    impact = [1] * n
    
    # Step 1: Left product
    left_product = 1
    for i in range(n):
        impact[i] = left_product
        left_product *= contributions[i]
    
    # Step 2: Right product
    right_product = 1
    for i in range(n - 1, -1, -1):
        impact[i] *= right_product
        right_product *= contributions[i]
    
    return impact


# 🔽 Driver / Client Code
if __name__ == "__main__":
    contributions = [1, 2, 3, 4]
    result = teamContribution(contributions)
    print("Impact Array:", result)
