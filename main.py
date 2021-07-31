import radixSort
if __name__ == "__main__":
    from json import load
    from time import time
    arr = []
    start = float(time())
    with open("10000.json", 'r') as file:
        arr = load(file)
    radixSort.radixSort(arr)
    end = float(time() - start)
    print(f"Radix: {end} seconds")
