# In a month of 30 days my schedule is as follows
#
# booked = [ 1, 3, 9, 12, 13, 18, 26, 27, 28, 29 ]
# travel = [ 4, 5, 15, 16, 21, 22 ]
# Write a function that takes these two lists as parameters and
# returns a list of days when I am free to study

def booked_travel_study():
    booked = [1, 3, 9, 12, 13, 18, 26, 27, 28, 29]
    travel = [4, 5, 15, 16, 21, 22]
    # study = []
    all_days = set(range(1, 31))
    busy_days = set(booked + travel)
    free_days = sorted(all_days - busy_days)

    print("Your schedule for study are:", free_days)
booked_travel_study()