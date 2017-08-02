import Location
import Employee
from math import sqrt,pow
from functools import reduce
class Recommend(object):
    def __init__(self, employee, town, frame_all, frame_employee, frame_hotel):
        self.emp = employee
        self.town = town
        self.hotels = []
        self.location = []
        self.employee = []
        self.frame_all = frame_all
        self.frame_e = frame_employee
        self.frame_h = frame_hotel

    def createLocation(self):
        self.location = Location.Location(self.town, self.frame_all)

    def createEmployee(self):
        self.employee = Employee.Employee(self.emp, self.frame_e)
        self.employee.preference()

    def findHotels(self):
        self.location.findHotelReviews(self.frame_h)
        self.hotels = self.location.suggestions

    def recommend(self):
        self.createEmployee()
        self.createLocation()
        self.findHotels()
        ranks = []
        for i in self.hotels:
            ranks.append((i[0], self.similarity(self.employee.preferences, i[1])))
        return sorted(ranks, key=lambda x: x[1], reverse=True)[:3]

    def recommendWithPrice(self):
        self.createLocation()
        self.createEmployee()
        self.findHotels()
        ranks = []
        w1 = 0.8
        w2 = 0.2
        for i in self.hotels:
            hotel_price = self.frame_all[self.frame_all.HotelName == i[0]].RateBkd.unique()
            similarities = self.similarity(self.employee.preferences, i[1])
            equation = w1 * similarities + w2 * (1 / (sum(hotel_price) / len(hotel_price)))
            ranks.append((i[0], equation))
        return sorted(ranks, key=lambda x: x[1], reverse=True)[:4]

    def similarity(self,l1, l2):
        return reduce(lambda x, y: x + y, [a * b for a, b in zip(l1, l2)]) / (
        sqrt(sum(map(lambda x: pow(x, 2), l1))) * sqrt(sum(map(lambda x: pow(x, 2), l2))))