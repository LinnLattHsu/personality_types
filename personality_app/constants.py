# constants.py
# Data derived from your 'Top 10 Most Influential Traits' chart
IMPORTANCE_SCORES = {
    'party_liking': 0.18,
    'public_speaking_comfort': 0.11,
    'excitement_seeking': 0.10,
    'alone_time_preference': 0.09,
    'talkativeness': 0.08,
}

# Data derived from your 'Comparison of Top 5 Key Features' chart
TYPE_AVERAGES = {
    'party_liking': {'Introvert': 2, 'Ambivert': 5, 'Extrovert': 8},
    'public_speaking_comfort': {'Introvert': 2, 'Ambivert': 5, 'Extrovert': 8},
    'excitement_seeking': {'Introvert': 3, 'Ambivert': 6, 'Extrovert': 8},
    'alone_time_preference': {'Introvert': 8, 'Ambivert': 6, 'Extrovert': 3},
    'talkativeness': {'Introvert': 3, 'Ambivert': 5.5, 'Extrovert': 8},
    # ... add others from your bar chart
}