import pandas as pd
import numpy as np
import Recommend

path = 'Recc_Topics_Location.csv'
path_hotel = 'Hotel_Topic_comments.csv'
path_employees = 'Employee_Topic_comments.csv'
path_town = 'Town_Topic_comments.csv'

frame_all = pd.read_csv(path,error_bad_lines=False,encoding='ISO-8859-1')
frame_hotel = pd.read_csv(path_hotel,error_bad_lines=False,encoding='ISO-8859-1')
frame_employees = pd.read_csv(path_employees,error_bad_lines=False,encoding='ISO-8859-1')
frame_town = pd.read_csv(path_town,error_bad_lines=False,encoding='ISO-8859-1')

# Test the recommendations sytstem
available_towns = frame_all.Town.unique()
summary_frame = pd.DataFrame({'count':frame_all.groupby(['PNumber','HotelName','Town']).size()}).reset_index()


test_set =  summary_frame.sample(5522).reset_index()
results = []
score = 0
total = 0
for i in test_set.PNumber.unique():
    list_of_Towns = test_set[test_set.PNumber == i].Town.unique()
    test_list = []
    for j in list_of_Towns:
        hotel_visited = list(test_set[(test_set.PNumber == i) &  (test_set.Town == j) ].HotelName.unique())
        rec = Recommend.Recommend(i,j,frame_all,frame_employees,frame_hotel)
        # Recommendation without price included
        # recommendations = [h[0] for h in rec.recommend()]
        # Recommendation with price included
        recommendations = [h[0] for h in rec.recommendWithPrice()]
        #test_list.append((i,j,recommendations,hotel_visited))
    if not set(hotel_visited).isdisjoint(recommendations):
        score +=1
    total +=1
    #results.append(test_list)
print(score)
print(total)
print(score/total)