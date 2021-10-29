from models.event import *


event1 = Event("25/12/21", "Christmas", 50, 1, "santa themed event", True)
event2 = Event("14/02/2021", "Valentines", 3, 2, "a night of voyerism", True)
event3 = Event("02/03/2019", "Holly's baby shower", 300, 10, "waste of time and money", False)

event_list = [event1, event2, event3]

def add_new_event(event):
    event_list.append(event)

def remove_event(event):
    event_list.remove[event]