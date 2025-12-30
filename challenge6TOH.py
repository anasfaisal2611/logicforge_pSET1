def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    # Base case
    if n == 1:
        print(f"Disk 1 moved from {from_rod} to {to_rod}")
        return

    # Step 1: Move n-1 disks from source to auxiliary
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)

    # Step 2: Move nth disk from source to destination
    print(f"Disk {n} moved from {from_rod} to {to_rod}")

    # Step 3: Move n-1 disks from auxiliary to destination
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    towerOfHanoi(n, 'A', 'C', 'B')
