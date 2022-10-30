import csv

def reader_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            prueba =dict((iterable))
            data.append(prueba)
        return data
if __name__ == '__main__':
   data = reader_csv('d:\prueba\propython\world_population.csv')
   print (data[0])



