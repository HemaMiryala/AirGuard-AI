def get_aqi_category_info(aqi):
    """
    Returns (category, color_hex, emoji, health_effect, recommended_action)
    """
    if aqi <= 50:
        return "Good", "#00E400", "😊", "Air quality is considered satisfactory, and air pollution poses little or no risk.", "Normal outdoor activity. Maintain greenery."
    elif aqi <= 100:
        return "Moderate", "#FFFF00", "🙂", "Air quality is acceptable; however, there may be some health concern for a small number of people.", "Sensitive people take precautions."
    elif aqi <= 200:
        return "Poor", "#FF7E00", "😷", "Members of sensitive groups may experience health effects. The general public is not likely to be affected.", "Mask recommendation. Reduce outdoor exercise."
    elif aqi <= 300:
        return "Very Poor", "#FF0000", "⚠️", "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.", "Avoid unnecessary outdoor activity. Use air purifier if available."
    else:
        return "Severe", "#8F3F97", "☠️", "Health warnings of emergency conditions. The entire population is more likely to be affected.", "Stay indoors. Protect children, elderly, asthma patients."

def get_trend(current_aqi, predicted_aqi):
    diff = predicted_aqi - current_aqi
    if diff > 10:
        return "↑ Increasing pollution", "red"
    elif diff < -10:
        return "↓ Decreasing pollution", "green"
    else:
        return "→ Stable conditions", "gray"
