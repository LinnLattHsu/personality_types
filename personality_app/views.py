from django.shortcuts import render
import joblib
import os
from django.conf import settings
from .constants import IMPORTANCE_SCORES, TYPE_AVERAGES
# Create your views here.

model_path = os.path.join(settings.BASE_DIR, 'personality_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'scaler.pkl')

rf_model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

feature_names = [
        'social_energy', 'alone_time_preference', 'talkativeness', 'deep_reflection', 'group_comfort',
        'party_liking','listening_skill','empathy','creativity','organization','leadership','risk_taking',
        'public_speaking_comfort','curiosity','routine_preference','excitement_seeking','friendliness',
        'emotional_stability','planning','spontaneity','adventurousness','reading_habit','sports_interest',
        'online_social_usage','travel_desire','gadget_usage','work_style_collaborative','decision_speed',
        'stress_handling'
    ]
# Benchmarks derived from your Colab analysis
ORIGINAL_DATA = {
    'Extrovert': {
        'party_liking': 8.0,
        'public_speaking_comfort': 7.9,
        'excitement_seeking': 8.0,
        'alone_time_preference': 3.0,
        'talkativeness': 8.0
    },
    'Introvert': {
        'party_liking': 2.1,
        'public_speaking_comfort': 3.1,
        'excitement_seeking': 3.1,
        'alone_time_preference': 8.0,
        'talkativeness': 3.0
    },
    'Ambivert': {
        'party_liking': 5.0,
        'public_speaking_comfort': 5.5,
        'excitement_seeking': 5.5,
        'alone_time_preference': 5.5,
        'talkativeness': 5.5
    }
}
# def dashboard(request):
#     # 1. Load your linked files
#     model = joblib.load('personality_model.pkl')
#     scaler = joblib.load('scaler.pkl')
#
#     # 2. Get user scores (Assuming you saved them in Session or DB)
#     user_data = request.session.get('user_scores')
#     # SAFETY CHECK: If the user hasn't taken the test yet, user_data is None
#     if user_data is None:
#         # Option A: Redirect them to the test
#         # return redirect('check_personality')
#
#         # Option B: Provide default scores so the page doesn't crash
#         user_data = {feature: 5 for feature in feature_names}
#
#     # 3. Logic for "Power Players" (Insight #1)
#     # Sort user scores based on the IMPORTANCE_SCORES weights
#     power_players = []
#     for trait, weight in IMPORTANCE_SCORES.items():
#         power_players.append({
#             'name': trait.replace('_', ' ').title(),
#             'score': user_data.get(trait),
#             'impact': weight * 100
#         })
#
#     # 4. Logic for "Trait Synergy" (Insight #3)
#     # Based on your Heatmap's 1.00 correlation between social_energy and party_liking
#     synergy_text = ""
#     soc = int(user_data.get('social_energy', 0))
#     party = int(user_data.get('party_liking', 0))
#
#     if soc >= 8 and party >= 8:
#         synergy_text = "Your high Social Energy and Party Liking suggest a 'High-Engagement' personality."
#     elif soc <= 4 and party <= 4:
#         synergy_text = "You prefer meaningful small-group interactions over large social scenes."
#
#     return render(request, 'dashboard.html', {
#         'power_players': power_players,
#         'synergy_text': synergy_text,
#         'averages': TYPE_AVERAGES,
#         'user_scores': user_data
#     })
from django.shortcuts import render, redirect


def dashboard(request):
    # Use 'Extrovert' averages as the "Original Data" example for the dashboard
    # base_stats = ORIGINAL_DATA['Extrovert']
    all_averages = {
        'labels': ['Party Liking', 'Public Speaking', 'Excitement Seeking', 'Alone Time', 'Talkativeness'],
        'extrovert': [8.0, 7.9, 8.0, 3.0, 8.0],
        'introvert': [2.1, 3.1, 3.1, 8.0, 3.0],
        'ambivert': [5.0, 5.5, 5.5, 5.5, 5.5]
    }

    # POWER PLAYERS: Using fixed original scores
    power_players = [
        {'name': 'Party Liking', 'score': 5},
        {'name': 'Public Speaking Comfort', 'score': 6},
        {'name': 'Excitement Seeking', 'score': 6},
        {'name': 'Alone Time Preference', 'score': 6},
        {'name': 'Talkativeness', 'score': 6},
    ]

    # TRAIT SYNERGY: Hardcoded from your Interaction Heatmap correlations
    # In your original data, Social Energy and Party Liking have a 1.00 correlation
    synergy_text = "Original Data Analysis: High Social Energy (1.00) perfectly correlates with Party Liking in the dataset."

    comparison_data = {
        'labels': ['Party Liking', 'Public Speaking', 'Excitement', 'Alone Time', 'Talkativeness'],
        'extrovert': [8.0, 7.9, 8.0, 3.0, 8.0],  #
        'introvert': [2.1, 3.1, 3.1, 8.0, 3.0],  #
        'ambivert': [5.0, 5.5, 5.5, 5.5, 5.5]  #
    }

    # Keeping your Power Players logic for the sidebar
    # power_players = [
    #     {'name': 'Party Liking', 'score': 8.0},
    #     {'name': 'Public Speaking Comfort', 'score': 7.9},
    #     {'name': 'Excitement Seeking', 'score': 8.0},
    #     {'name': 'Alone Time Preference', 'score': 3.0},
    #     {'name': 'Talkativeness', 'score': 8.0},
    # ]
    curiosity_stats = {
        'Extrovert': 6.97,
        'Ambivert': 6.50,
        'Introvert': 6.01
    }

    # Social Averages for Ambivert comparison
    social_stats = {
        'labels': ['Curiosity', 'Party Liking', 'Talkativeness'],
        'extrovert': [6.97, 8.0, 8.0],
        'ambivert': [6.50, 5.0, 5.5],
        'introvert': [6.01, 2.1, 3.0]
    }


    return render(request, 'dashboard.html', {
        'power_players': power_players,
        # 'synergy_text': synergy_text,
        'synergy_text': "Analysis shows Extroverts lead in active curiosity (6.97), while Ambiverts maintain the most stable social scores (5.5).",
        'original_stats': ORIGINAL_DATA
    })
def check_personality(request):
    feature_names = [
        'social_energy', 'alone_time_preference', 'talkativeness', 'deep_reflection', 'group_comfort',
        'party_liking','listening_skill','empathy','creativity','organization','leadership','risk_taking',
        'public_speaking_comfort','curiosity','routine_preference','excitement_seeking','friendliness',
        'emotional_stability','planning','spontaneity','adventurousness','reading_habit','sports_interest',
        'online_social_usage','travel_desire','gadget_usage','work_style_collaborative','decision_speed',
        'stress_handling'
    ]
    categories = {
        "Social & Engagement": [
            "social_energy", "talkativeness", "group_comfort",
        "party_liking", "public_speaking_comfort", "friendliness",
        "online_social_usage"
        ],
        "Mindset & Reflection": [
            "deep_reflection", "creativity", "curiosity", "reading_habit"
        ],
        "Work & Decision Making": [
            "organization", "leadership", "planning", "work_style_collaborative",
        "decision_speed", "routine_preference"
        ],
        "Emotional Intelligence": [
            "empathy", "listening_skill", "emotional_stability", "stress_handling"
        ],
        "Lifestyle & Adventure": [
            "alone_time_preference", "risk_taking", "excitement_seeking",
            "spontaneity", "adventurousness", "sports_interest",
            "travel_desire", "gadget_usage"
        ]
    }
    categorized_list = [item for sublist in categories.values() for item in sublist]
    categories["Other Traits"] = [f for f in feature_names if f not in categorized_list]

    context = {'features': feature_names,'categories':categories}
    if request.method == 'POST':
        # ၁။ Form မှ data များကို ယူခြင်း
        inputs = [float(request.POST.get(f, 5)) for f in feature_names]

        # ၂။ Scaler နှင့် Model ကို သုံး၍ Prediction လုပ်ခြင်း
        scaled_data = scaler.transform([inputs])
        probabilities = rf_model.predict_proba(scaled_data)[0]

        # ၃။ ရလဒ်ကို context ထဲသို့ ထည့်သွင်းခြင်း
        context['proba'] = {
            'Ambivert': round(probabilities[0] * 100, 2),
            'Extrovert': round(probabilities[1] * 100, 2),
            'Introvert': round(probabilities[2] * 100, 2)
        }


    return render(request, 'check.html', context)
    # if request.method == 'POST':
    #     try:
    #         user_inputs = [float(request.POST.get(f, 5)) for f in feature_names]
    #
    #         scaled_data = scaler.transform([user_inputs])
    #         probabilities = rf_model.predict_proba(scaled_data)[0]
    #
    #         context['proba'] = {
    #             'Ambivert': round(probabilities[0] * 100, 2),
    #             'Extrovert': round(probabilities[1] * 100, 2),
    #             'Introvert': round(probabilities[2] * 100, 2)
    #         }
    #     except Exception as e:
    #         context['error'] = str(e)
    #
    # return render(request, 'check.html', context)


import pandas as pd


def statistics(request):
    # 1. Get the path to your CSV file
    csv_path = os.path.join(settings.BASE_DIR, 'personality_synthetic_dataset.csv')

    # 2. Load and process data
    df = pd.read_csv(csv_path)

    # 3. Get descriptive stats and format them for the template
    # We transpose (.T) so traits are rows, and reset index to keep trait names
    desc = df.describe().T.reset_index()
    desc.columns = ['trait', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']

    # Round numbers to 2 decimal places for a clean UI
    desc = desc.round(2)

    # Convert to a list of dictionaries that Django can loop through
    stats_list = desc.to_dict('records')

    return render(request, 'statistics.html', {'stats': stats_list})