import random
from datetime import datetime, timedelta

# Define the activities, times of day, and impact metrics
activities = {
    'Health Education': {
        'times': ['Morning', 'Afternoon'],
        'impact_metric': 'people educated'
    },
    'Community Outreach': {
        'times': ['Morning', 'Afternoon', 'Evening'],
        'impact_metric': 'households visited'
    },
    'Environmental Clean-Up': {
        'times': ['Morning'],
        'impact_metric': 'kg of waste collected'
    },
    'Medical Assistance': {
        'times': ['Morning', 'Afternoon', 'Evening'],
        'impact_metric': 'patients assisted'
    },
    'Administrative Support': {
        'times': ['Afternoon'],
        'impact_metric': 'hours contributed'
    }
}

# Define sample locations around the health center
locations = ['North Wing', 'Community Hall', 'East Garden', 'Outreach Post', 'Admin Block']

def random_date():
    today = datetime.now()
    day_of_week = today.weekday()
    start_of_week = today - timedelta(days=day_of_week)
    random_day = random.randint(0, 6)
    return start_of_week + timedelta(days=random_day)

def generate_synthetic_data(num_entries=100):
    synthetic_data = []
    for _ in range(num_entries):
        activity_name, activity_details = random.choice(list(activities.items()))
        time_of_day = random.choice(activity_details['times'])
        date = random_date()
        volunteer_id = random.randint(1, 100)
        location = random.choice(locations)
        impact = random.randint(1, 100)  # Simplified impact metric
        synthetic_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'day': date.strftime('%A'),
            'activity': activity_name,
            'time_of_day': time_of_day,
            'volunteer_id': volunteer_id,
            'location': location,
            'impact_metric': activity_details['impact_metric'],
            'impact': impact
        })
    return synthetic_data

# Enhanced Example Usage
if __name__ == "__main__":
    data = generate_synthetic_data(10)  # Generate data for 10 entries
    for entry in data:
        print(entry)

