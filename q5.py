import Testing


def main():
    results = []
    for i in range(5):
        results.append(Testing.testPenData()[1])

    print("Test Pen Data Results: Max: " + str(max(results)) + " Average: " + str(Testing.average(results)) +
          " Std Dev: " + str(Testing.stDeviation(results)))

    results = []
    for i in range(5):
        results.append(Testing.testCarData()[1])

    print("Test Car Data Results: Max: " + str(max(results)) + " Average: " + str(Testing.average(results)) +
          " Std Dev: " + str(Testing.stDeviation(results)))

main()