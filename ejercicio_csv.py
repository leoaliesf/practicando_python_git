import csv
import matplotlib.pyplot as plt

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
    world_popu= list(map(lambda items : items['World Population Percentage'] , data))
    country = list(map(lambda items : items['Country/Territory'] , data))
    world_popu = [float(i) for i in world_popu]
    def gene_pye(labels, values):
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels )
        plt.show()
    gene_pye(country, world_popu)
    
