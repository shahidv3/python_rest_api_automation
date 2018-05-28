import csv

global input
global nr



def read_csv(self, inputcsv):
    ''' read csv input file and convert it to dict '''
    with open(inputcsv) as f:
        reader = csv.DictReader(f)
        input = [r for r in reader]
        return input