import csv

class DataLoader:
    def __init__(self, path):
        self._path = path

    def get_data(self):
        with open(self._path) as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',')
            entries = []
            for row in spamreader:
                entry = {}
                entry['Outlook'] = row['Outlook']
                entry['Temperature'] = row['Temperature']
                entry['Humidity'] = row['Humidity']
                entry['Wind'] = row['Wind']
                entry['Play Tennis'] = row['Play Tennis']
                entries.append(entry)

            return entries
        

if __name__ == "__main__":
    data_loader = DataLoader('hw1/part2/data/PlayTennis.csv')
    data = data_loader.get_data()
    list(map(lambda x: print(x), data))