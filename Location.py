import Hotel
class Location(object):
    def __init__(self, town, frame):
        self.town = town
        self.frame = frame
        self.hotels = []
        self.suggestions = []

    def findHotels(self):
        self.hotels = self.frame[self.frame.Town == self.town].HotelName.unique()

    def findHotelReviews(self, frame_hotel):
        self.findHotels()
        reviews = []
        for i in self.hotels:
            temp = Hotel.Hotel(i, frame_hotel)
            temp.preference()
            reviews.append((i, temp.preferences))
        self.suggestions = reviews
