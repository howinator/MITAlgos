import MergeSort
import random
import InsertionSort
import sys

def main(argv):

    if len(argv) == 0 or len(argv) > 1:
        print("Usage: SortTest.py [Algo]Sort")

    else: 
        algo = argv[0]
        failedTests = 0
        for eles in range(10000, 10010):
            isSorted = test(eles, algo)
            if isSorted == True:

                print("Test for ", eles, "PASSED.")
            else:
                failedTests += 1
                print("Test for ", eles, "FAILED.")

        if failedTests > 0:
            print(failedTests, "test(s) FAILED.")

def test(numElements, algo):

    A = []
    for ele in range(0, numElements):
        A.append(random.randint(0, 100000))

    if algo == "MergeSort":
        B = MergeSort.mergeSort(A)
    elif algo == "InsertionSort":
        B = InsertionSort.InsertionSort(A)

    isSorted = True
    for ele in range(0, numElements - 1):
        if B[ele] > B[ele + 1]:
            isSorted = False

    return isSorted

if __name__ == "__main__":
    import cProfile
    cProfile.run("main(sys.argv[1:])")

# main(sys.argv[1:])

