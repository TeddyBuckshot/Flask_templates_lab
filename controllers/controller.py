from flask import render_template, request
from app import app
from models.event import Event
from models.planner import add_new_event, event_list, remove_event

@app.route('/events')
def index():
    return render_template('index.html', title='Planner', events=event_list)

@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_date = request.form['date']
    event_name = request.form['name']
    event_description = request.form['description']
    event_guests = request.form['no_of_guests']
    event_location = request.form['room_location']
    event_recurring = False
    if "recurring" in request.form:
        event_recurring = True
    new_event = Event(event_date,event_name,event_guests,event_location,event_description,event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title='Planner', events=event_list)

@app.route('/events/delete/<index>', methods=['POST'])
def delete_event(index):
    remove_event(int(index))
    return render_template('index.html', title='Planner', events=event_list)