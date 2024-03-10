
import random
from datetime import datetime, timedelta

# Define the activities with their times, impact metrics, and a placeholder for comments
activities_with_comments = {
    'Health Education': {
        'times': ['Morning', 'Afternoon'],
        'impact_metric': 'people educated',
        'comment': 'Improves community health awareness, reducing long-term healthcare costs.'
    },
    'Community Outreach': {
        'times': ['Morning', 'Afternoon', 'Evening'],
        'impact_metric': 'households visited',
        'comment': 'Strengthens community bonds and spreads eco-friendly practices.'
    },
    'Environmental Clean-Up': {
        'times': ['Morning'],
        'impact_metric': 'kg of waste collected',
        'comment': 'Directly reduces environmental pollution and promotes cleaner habitats.'
    },
    'Medical Assistance': {
        'times': ['Morning', 'Afternoon', 'Evening'],
        'impact_metric': 'patients assisted',
        'comment': 'Provides critical healthcare services, enhancing community well-being.'
    },
    'Administrative Support': {
        'times': ['Afternoon'],
        'impact_metric': 'hours contributed',
        'comment': 'Supports the efficient operation of eco-initiatives through skilled volunteerism.'
    }
}

# Helper function to generate a random date within the next week
def random_date():
    today = datetime.now()
    day_of_week = today.weekday()
    start_of_week = today - timedelta(days=day_of_week)  # Assuming Monday is the start of the week
    random_day = random.randint(0, 6)  # Random day of the week
    return start_of_week + timedelta(days=random_day)

# Generate synthetic data
def generate_synthetic_data(num_entries=100):
    synthetic_data = []
    for _ in range(num_entries):
        activity_name, activity_details = random.choice(list(activities_with_comments.items()))
        time_of_day = random.choice(activity_details['times'])
        comment = activity_details['comment']
        date = random_date()
        volunteer_id = random.randint(1, 100)  # Assuming IDs range from 1 to 100
        synthetic_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'day': date.strftime('%A'),
            'activity': activity_name,
            'time_of_day': time_of_day,
            'volunteer_id': volunteer_id,
            'comment': comment
        })
    return synthetic_data

# Example usage
if __name__ == "__main__":
    data = generate_synthetic_data(108)  # Adjusted to generate 108 entries as per the user's execution command
    for entry in data:
        print(entry)
