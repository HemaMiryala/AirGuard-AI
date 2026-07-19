# WHO Guideline Thresholds (24-hour mean generally, µg/m³)
WHO_GUIDELINES = {
    "PM2.5": 15,
    "PM10": 45,
    "NO2": 25,
    "SO2": 40,
    "O3": 100, # 8-hour mean
    "CO": 4000
}

def evaluate_pollutant_status(value, pollutant):
    threshold = WHO_GUIDELINES.get(pollutant, float('inf'))
    if value <= threshold * 0.5:
        return "Safe"
    elif value <= threshold:
        return "Moderate"
    else:
        return "High"

def get_dynamic_health_recommendations(aqi, pollutants):
    recommendations = []
    
    # AQI Based
    if aqi <= 50:
        recommendations.append("Overall air quality is excellent. Normal outdoor activity is perfectly fine.")
    elif aqi <= 100:
        recommendations.append("Air quality is acceptable. Unusually sensitive individuals should consider limiting prolonged outdoor exertion.")
    elif aqi <= 200:
        recommendations.append("Reduce prolonged or heavy outdoor exercise. Sensitive groups should wear masks.")
    elif aqi <= 300:
        recommendations.append("Avoid prolonged or heavy exertion outdoors. Wear N95 masks when stepping out. Use an air purifier indoors.")
    else:
        recommendations.append("Health alert: Stay indoors and keep windows closed. Run air purifiers continuously.")

    # Pollutant Based
    if pollutants.get("PM2.5", 0) > WHO_GUIDELINES["PM2.5"]:
        recommendations.append("High PM2.5 detected: Fine particles can enter the bloodstream. N95 masks are highly recommended outdoors.")
    if pollutants.get("O3", 0) > WHO_GUIDELINES["O3"]:
        recommendations.append("High Ozone levels: Asthmatics should keep inhalers handy and avoid afternoon outdoor activities.")
    if pollutants.get("NO2", 0) > WHO_GUIDELINES["NO2"]:
        recommendations.append("Elevated NO2: Can irritate airways. Avoid exercising near heavy traffic areas.")
        
    return recommendations

def get_dynamic_environmental_suggestions(aqi, pollutants):
    suggestions = [
        "🌱 **Tree Plantation**: Plant air-purifying indoor plants like Snake Plant or Aloe Vera."
    ]
    
    if pollutants.get("NO2", 0) > WHO_GUIDELINES["NO2"] or pollutants.get("CO", 0) > WHO_GUIDELINES["CO"]:
        suggestions.append("🚗 **Reduce Vehicle Emissions**: High combustion pollutants detected. Carpool, use public transport, or switch to an EV.")
        
    if pollutants.get("PM10", 0) > WHO_GUIDELINES["PM10"] or pollutants.get("PM2.5", 0) > WHO_GUIDELINES["PM2.5"]:
        suggestions.append("♻️ **Waste Management**: High particulate matter. Avoid burning garbage, wood, or dry leaves.")
        
    if aqi > 100:
        suggestions.append("💡 **Energy Conservation**: High overall pollution. Conserving electricity reduces power plant emissions.")
        
    suggestions.append("📢 **Community Awareness**: Educate your neighbors about the current air pollution trends.")
    return suggestions

def get_pollutant_explanations(pollutants):
    explanations = []
    
    details = {
        "PM2.5": {
            "name": "PM2.5 (Fine Particulate Matter)",
            "desc": "Tiny dust particles that enter deep into the lungs",
            "sources": "Vehicle exhaust, burning of fuels, forest fires.",
            "impacts": "Can penetrate deep into lungs and enter the bloodstream, causing cardiovascular and respiratory diseases."
        },
        "PM10": {
            "name": "PM10 (Coarse Particulate Matter)",
            "desc": "Larger dust particles",
            "sources": "Dust from construction sites, landfills, and agriculture, wind-blown dust.",
            "impacts": "Irritates eyes, nose, and throat. Aggravates asthma and bronchitis."
        },
        "NO2": {
            "name": "Nitrogen Dioxide (NO₂)",
            "desc": "Pollution mainly from vehicle exhaust",
            "sources": "Burning of fossil fuels, primarily from vehicle emissions and power plants.",
            "impacts": "Inflames lung lining, increases susceptibility to respiratory infections."
        },
        "SO2": {
            "name": "Sulfur Dioxide (SO₂)",
            "desc": "Pollution from industries and fuel burning",
            "sources": "Burning of sulfur-containing fossil fuels (coal, oil) at power plants and industrial facilities.",
            "impacts": "Causes breathing difficulties, especially in people with asthma."
        },
        "O3": {
            "name": "Ground-level Ozone (O₃)",
            "desc": "Not emitted directly into the air, but created by chemical reactions.",
            "sources": "Reactions between oxides of nitrogen (NOx) and volatile organic compounds (VOC) in sunlight.",
            "impacts": "Triggers asthma, reduces lung function, and causes breathing pain."
        },
        "CO": {
            "name": "Carbon Monoxide (CO)",
            "desc": "Carbon monoxide, harmful in high amounts",
            "sources": "Incomplete combustion of carbon-containing fuels (cars, trucks, small engines).",
            "impacts": "Reduces the amount of oxygen that can be transported in the blood stream to critical organs."
        }
    }
    
    for pol, val in pollutants.items():
        if pol in details:
            status = evaluate_pollutant_status(val, pol)
            
            # Status colors: Safe (green), Moderate (orange), High (red)
            status_color = "#00E400" if status == "Safe" else "#FF7E00" if status == "Moderate" else "#FF0000"
            
            explanations.append({
                "symbol": pol,
                "name": details[pol]["name"],
                "value": round(val, 2),
                "threshold": WHO_GUIDELINES[pol],
                "status": status,
                "status_color": status_color,
                "desc": details[pol]["desc"],
                "sources": details[pol]["sources"],
                "impacts": details[pol]["impacts"]
            })
            
    return explanations

def get_pollutant_interactions(pollutants):
    interactions = []
    pm25_high = pollutants.get("PM2.5", 0) > WHO_GUIDELINES["PM2.5"]
    no2_high = pollutants.get("NO2", 0) > WHO_GUIDELINES["NO2"]
    o3_high = pollutants.get("O3", 0) > WHO_GUIDELINES["O3"]
    so2_high = pollutants.get("SO2", 0) > WHO_GUIDELINES["SO2"]
    
    if pm25_high and no2_high:
        interactions.append("⚠️ **Synergistic Risk (PM2.5 + NO₂):** High levels of both fine particles and nitrogen dioxide significantly multiply the risk of severe cardiovascular events and acute asthma attacks compared to either pollutant alone.")
        
    if o3_high and pm25_high:
        interactions.append("⚠️ **Smog Alert (O₃ + PM2.5):** The combination of ground-level ozone and fine particulates strongly indicates photochemical smog, which severely reduces lung capacity and causes chest pain upon inhalation.")
        
    if so2_high and pm25_high:
        interactions.append("⚠️ **Acidic Particles (SO₂ + PM2.5):** Sulfur dioxide can react to form acidic aerosols, which attach to PM2.5 particles, driving corrosive damage deep into the respiratory tract.")
        
    if not interactions:
        interactions.append("✅ No major severe synergistic interactions detected currently.")
        
    return interactions

def get_risk_assessment(aqi, pollutants):
    risk_level = "Low"
    color = "#00E400" # Green
    
    if aqi > 300:
        risk_level = "Critical Emergency"
        color = "#8F3F97"
    elif aqi > 200:
        risk_level = "High Risk"
        color = "#FF0000"
    elif aqi > 100:
        risk_level = "Moderate Risk"
        color = "#FF7E00"
        
    # Check for individual pollutants spiking despite moderate AQI
    spikes = [pol for pol, val in pollutants.items() if val > WHO_GUIDELINES.get(pol, float('inf')) * 2]
    if spikes and risk_level in ["Low", "Moderate Risk"]:
        risk_level = "Elevated Specific Risk"
        color = "#FF7E00"
        
    assessment = f"**Overall Health Risk Level**: <span style='color:{color};font-weight:bold;'>{risk_level}</span>"
    
    if spikes:
        assessment += f"<br>⚠️ Critical spikes detected in: {', '.join(spikes)}. Immediate precautions advised for these specific pollutants."
        
    return assessment

def get_forecast_summary(aqi, category, pollutants):
    summary = f"The forecasted AQI is {aqi}, falling into the **{category}** category."
    
    high_pols = [pol for pol, val in pollutants.items() if val > WHO_GUIDELINES.get(pol, float('inf'))]
    if high_pols:
        summary += f" Be aware that {', '.join(high_pols)} levels are predicted to exceed WHO safety guidelines."
    else:
        summary += " All major pollutants are expected to remain within WHO safety guidelines."
        
    return summary
