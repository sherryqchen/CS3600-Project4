import Testing
import csv

def main():
    with open('rerun.csv', 'w') as csvfile:
        fieldnames = ['perceptrons', 'max', 'average', 'std_dev']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvfile.write("Pen Data Test Results \n")
        writer.writeheader()

        for hiddenlayers in xrange(0,41,5):
            results = []
            for i in range(5):
                print "Hidden Layer Perceptrons: " + str(hiddenlayers) + " Iteration: " + str(i+1)
                results.append(Testing.testPenData([hiddenlayers])[1])
            writer.writerow({'perceptrons': hiddenlayers, 'max': max(results), 'average': Testing.average(results),
                             'std_dev': Testing.stDeviation(results)})
            print "Test Pen Data Results: Hidden Layer Perceptrons: " + str(hiddenlayers) + " Max: " + str(max(results)) + \
                  " Average: " + str(Testing.average(results)) + " Std Dev: " + str(Testing.stDeviation(results))

        csvfile.write("Car Data Test Results \n")
        writer.writeheader()
        for hiddenlayers in xrange(0,41,5):
            results = []
            for i in range(5):
                print "Hidden Layer Perceptrons: " + str(hiddenlayers) + " Iteration: " + str(i + 1)
                results.append(Testing.testCarData([hiddenlayers])[1])

            writer.writerow({'perceptrons': hiddenlayers, 'max': max(results), 'average': Testing.average(results),
                            'std_dev': Testing.stDeviation(results)})
            print "Test Car Data Results: Hidden Layer Perceptrons: " + str(hiddenlayers) + " Max: " + str(max(results)) \
                  + " Average: " + str(Testing.average(results)) + " Std Dev: " + str(Testing.stDeviation(results))
main()