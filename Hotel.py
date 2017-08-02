class Hotel(object):
    def __init__(self, hotel, frame):
        self.hotel = hotel
        self.frame = frame
        self.preferences = []

    def preference(self):
        self.preferences = self.findTopicsFullVector()

    def findTopicsHotels(self):
        temp = self.frame.loc[self.frame.HotelName == self.hotel]
        maxes = temp.comments
        if len(maxes) < 4:
            aux = sorted(zip(maxes, temp.Category), key=lambda x: x[0], reverse=True)
            return [i[1] for i in aux]
        else:
            res = sorted(zip(maxes, temp.Category), key=lambda x: x[0], reverse=True)
            return [i[1] for i in res[0:3]]

    def findTopicsFullVector(self):
        temp = self.frame.loc[self.frame.HotelName == self.hotel]
        maxes = zip(temp.comments, temp.Category)
        return self.commsToVector(list(maxes))

    def commsToVector(self,ls):
        from functools import reduce
        categories = ['Breakfast', 'Gym', 'Location', 'Meals', 'Parking', 'Wifi']
        dictCetegory = dict([(c, 0.0) for c in categories])
        totalComments = reduce(lambda x, y: x + y, [i[0] for i in ls], 0)
        for i, z in ls:
            dictCetegory[z] = i / totalComments
        return [value for _, value in dictCetegory.items()]