from hw2.TravellingSalesmanProblem.models.Point import Point


class DataLoader:
    def __init__(self, path):
        self._path = path

    def get_data(self):
        with open(self._path, 'r') as file:
            name = file.readline().strip().split()[1]
            file_type = file.readline().strip().split()[1]
            comment = file.readline().strip().split()[1]
            dimension = int(file.readline().strip().split()[1])
            edge_weight_type = file.readline().strip().split()[1]
            file.readline()

            points = {}

            for i in range(dimension):
                line = file.readline().strip().split()
                nr = int(line[0])
                x = float(line[1])
                y = float(line[2])
                p = Point(x, y, nr)
                points[nr] = p

            return points
        

if __name__ == "__main__":
    data_loader = DataLoader('../data/berlin52.tsp')
    data = data_loader.get_data()
    print(data)