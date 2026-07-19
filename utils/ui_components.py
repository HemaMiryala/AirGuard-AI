def get_custom_css():
    return """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    /* Main Background with animated gradient */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #e0eafc, #cfdef3, #e2e2e2, #fdfbfb);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(16, 55, 92, 0.95) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    section[data-testid="stSidebar"] *, 
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
    }

    /* Headings */
    [data-testid="stMain"] h1, [data-testid="stMain"] h1 * {
        font-family: 'Inter', sans-serif;
        color: #1E293B !important;
        font-weight: 700;
    }
    [data-testid="stMain"] h2, [data-testid="stMain"] h2 *, 
    [data-testid="stMain"] h3, [data-testid="stMain"] h3 *, 
    [data-testid="stMain"] h4, [data-testid="stMain"] h4 *, 
    [data-testid="stMain"] h5, [data-testid="stMain"] h5 *, 
    [data-testid="stMain"] h6, [data-testid="stMain"] h6 * {
        font-family: 'Inter', sans-serif;
        color: #334155 !important;
        font-weight: 600;
    }

    /* Normal text */
    [data-testid="stMain"] p, 
    [data-testid="stMain"] span, 
    [data-testid="stMain"] li {
        color: #475569 !important;
    }

    /* Labels */
    [data-testid="stMain"] label, 
    [data-testid="stMain"] .st-caption,
    [data-testid="stMain"] [data-testid="stCaptionContainer"] {
        color: #64748B !important;
    }

    /* Glassmorphism Metric Cards */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.15);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: #1E293B !important;
    }
    
    [data-testid="stMetricLabel"] *, [data-testid="stMetricLabel"] {
        color: #475569 !important;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #1976D2, #1259A7) !important;
        color: white !important;
        height: 55px;
        width: 100%;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(25, 118, 210, 0.3);
    }
    
    .stButton>button *, .stButton>button p {
        color: white !important;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #1259A7, #0d47a1) !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(25, 118, 210, 0.4);
    }

    /* Inputs */
    div[role="radiogroup"], div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    /* Success Alerts */
    div[data-testid="stAlert"] {
        border-radius: 15px;
        backdrop-filter: blur(5px);
    }

    /* DataFrame Tables */
    table {
        border-radius: 15px;
        overflow: hidden;
        background: rgba(255,255,255,0.7);
    }
    
    table, th, td, [data-testid="stDataFrame"] * {
        color: #334155 !important;
    }
    
    /* Hide Streamlit Footer & Header */
    footer { visibility: hidden; }
    header { visibility: hidden; }
    
    /* Custom Card for Info */
    .glass-card {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    </style>
    """

def get_hero_section():
    return """
    <div style="text-align:center; padding: 40px 0; animation: fadeIn 1.5s ease-in;">
        <h1 style="font-size:56px; margin-bottom: 10px; background: -webkit-linear-gradient(45deg, #10375C, #1976D2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🌍 AirGuard AI
        </h1>
        <div style="font-size:24px; color:#5F6B7A; font-weight: 300;">
            Next-Generation Air Quality Intelligence & Prediction
        </div>
    </div>
    """

def get_footer():
    return """
    <div style="background: linear-gradient(135deg, #10375C, #0a2540); padding: 30px; border-radius: 20px; text-align: center; color: white; margin-top: 50px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <h3 style="color: white; margin-bottom: 10px; font-size: 24px;">🌍 AirGuard AI</h3>
        <p style="color: #9CA3AF; font-size: 16px; margin-bottom: 5px;">Built with ❤️ for the AI Hackathon</p>
        <p style="color: #6B7280; font-size: 14px;">Powered by Random Forest, Streamlit & OpenWeather API • v2.0</p>
        <div style="margin-top: 15px; font-size: 12px; color: #4B5563;">© 2026 AirGuard AI. All rights reserved.</div>
    </div>
    """
