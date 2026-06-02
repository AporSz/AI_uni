import csv

class DataLoader:
    def __init__(self, path):
        self._path = path

    def get_data_play_tennis(self):
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
        
    def get_data_heart_disease(self):
        with open(self._path) as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',')
            entries = []
            for row in spamreader:
                entry = {}
                entry['age'] = int(row['ï»¿age'])
                entry['sex'] = int(row['sex'])
                entry['cp'] = int(row['cp'])
                entry['trestbps'] = int(row['trestbps'])
                entry['chol'] = int(row['chol'])
                entry['fbs'] = int(row['fbs'])
                entry['restecg'] = int(row['restecg'])
                entry['thalach'] = int(row['thalach'])
                entry['exang'] = int(row['exang'])
                entry['oldpeak'] = float(row['oldpeak'])
                entry['slope'] = int(row['slope'])
                entry['ca'] = int(row['ca'])
                entry['thal'] = int(row['thal'])
                entry['target'] = int(row['target'])

                entries.append(entry)

            return entries

if __name__ == "__main__":
    data_loader = DataLoader('hw1/part2/data/PlayTennis.csv')
    data = data_loader.get_data_play_tennis()
    list(map(lambda x: print(x), data))