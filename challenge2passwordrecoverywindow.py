def minWindow(log, pattern):
    if not log or not pattern:
        return ""

    from collections import Counter

    # Frequency of characters in pattern
    pattern_count = Counter(pattern)

    required = len(pattern_count)   # unique chars needed
    formed = 0                      # chars matched with required frequency

    window_count = {}

    left = 0
    min_len = float("inf")
    min_window = ""
    for right in range(len(log)):
        char = log[right]
        window_count[char] = window_count.get(char, 0) + 1

        # If current char frequency matches pattern
        if char in pattern_count and window_count[char] == pattern_count[char]:
            formed += 1

        while left <= right and formed == required:
            char = log[left]

            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = log[left:right+1]

            window_count[char] -= 1
            if char in pattern_count and window_count[char] < pattern_count[char]:
                formed -= 1
            left += 1

    return min_window

if __name__ == "__main__":
    log = input("Enter log string: ")
    pattern = input("Enter pattern string: ")
    result = minWindow(log, pattern)
    print("Minimum Window Substring:", result)
