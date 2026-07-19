def get_custom_css():
    return """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    /* ==========================
       Animated Background
    ========================== */
    @keyframes gradientBG {
        0% {background-position:0% 50%;}
        50% {background-position:100% 50%;}
        100% {background-position:0% 50%;}
    }

    .stApp{
        font-family:'Inter',sans-serif;
        background:linear-gradient(-45deg,#e0eafc,#cfdef3,#e2e2e2,#fdfbfb);
        background-size:400% 400%;
        animation:gradientBG 15s ease infinite;
    }

    /* ==========================
       Sidebar
    ========================== */

    section[data-testid="stSidebar"]{
        background:rgba(16,55,92,0.95)!important;
        backdrop-filter:blur(12px);
        border-right:1px solid rgba(255,255,255,.15);
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label{
        color:white!important;
    }

    /* ==========================
       Selectbox (FIXED)
    ========================== */

    div[data-baseweb="select"]{
        background:white!important;
        border-radius:12px!important;
        border:1px solid #CBD5E1!important;
        color:#1E293B!important;
    }

    div[data-baseweb="select"] *{
        color:#1E293B!important;
    }

    div[data-baseweb="select"] span{
        color:#1E293B!important;
        font-weight:600;
    }

    div[data-baseweb="select"] svg{
        fill:#1E293B!important;
    }

    div[role="listbox"]{
        background:white!important;
        color:#1E293B!important;
        border-radius:10px!important;
    }

    div[role="option"]{
        color:#1E293B!important;
        background:white!important;
    }

    div[role="option"]:hover{
        background:#E2E8F0!important;
    }

    /* ==========================
       Radio Buttons
    ========================== */

    div[role="radiogroup"]{
        background:rgba(255,255,255,.85);
        padding:10px;
        border-radius:12px;
    }

    div[role="radiogroup"] label{
        color:#1E293B!important;
        font-weight:500;
    }

    /* ==========================
       Main Headings
    ========================== */

    [data-testid="stMain"] h1{
        color:#1E293B!important;
        font-weight:700;
    }

    [data-testid="stMain"] h2,
    [data-testid="stMain"] h3,
    [data-testid="stMain"] h4,
    [data-testid="stMain"] h5{
        color:#334155!important;
        font-weight:600;
    }

    p,li,span{
        color:#475569;
    }

    /* ==========================
       Metric Cards
    ========================== */

    [data-testid="metric-container"]{
        background:rgba(255,255,255,.65);
        backdrop-filter:blur(12px);
        border-radius:20px;
        padding:20px;
        border:1px solid rgba(255,255,255,.8);
        box-shadow:0 8px 25px rgba(0,0,0,.08);
        transition:.3s;
    }

    [data-testid="metric-container"]:hover{
        transform:translateY(-5px);
        box-shadow:0 15px 35px rgba(0,0,0,.12);
    }

    [data-testid="stMetricValue"]{
        color:#1E293B!important;
        font-weight:700!important;
        font-size:28px!important;
    }

    [data-testid="stMetricLabel"]{
        color:#475569!important;
    }

    /* ==========================
       Buttons
    ========================== */

    .stButton>button{
        width:100%;
        height:55px;
        border:none;
        border-radius:14px;
        background:linear-gradient(135deg,#1976D2,#1259A7);
        color:white!important;
        font-weight:700;
        font-size:18px;
        transition:.3s;
        box-shadow:0 8px 20px rgba(25,118,210,.35);
    }

    .stButton>button:hover{
        transform:translateY(-2px);
        background:linear-gradient(135deg,#1259A7,#0D47A1);
    }

    /* ==========================
       DataFrames
    ========================== */

    table{
        border-radius:15px;
        overflow:hidden;
    }

    table,
    th,
    td{
        color:#334155!important;
    }

    /* ==========================
       Alerts
    ========================== */

    div[data-testid="stAlert"]{
        border-radius:15px;
    }

    /* ==========================
       Glass Card
    ========================== */

    .glass-card{
        background:rgba(255,255,255,.75);
        backdrop-filter:blur(10px);
        border-radius:20px;
        padding:24px;
        border:1px solid rgba(255,255,255,.5);
        box-shadow:0 6px 25px rgba(0,0,0,.06);
        margin-bottom:20px;
    }

    /* ==========================
       Hide Streamlit Branding
    ========================== */

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    </style>
    """


def get_hero_section():
    return """
    <div style="text-align:center;padding:40px 0;">
        <h1 style="font-size:56px;
        background:linear-gradient(45deg,#10375C,#1976D2);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        font-weight:700;">
            🌍 AirGuard AI
        </h1>

        <div style="font-size:23px;
        color:#5F6B7A;
        font-weight:300;">
            Next-Generation Air Quality Intelligence & Prediction
        </div>
    </div>
    """


def get_footer():
    return """
    <div style="
        margin-top:50px;
        padding:30px;
        border-radius:20px;
        text-align:center;
        background:linear-gradient(135deg,#10375C,#0A2540);
        box-shadow:0 10px 30px rgba(0,0,0,.15);">

        <h2 style="color:white;margin-bottom:10px;">
            🌍 AirGuard AI
        </h2>

        <p style="color:#D1D5DB;">
            Built with ❤️ for AI Hackathon
        </p>

        <p style="color:#9CA3AF;">
            Random Forest • Streamlit • OpenWeather API
        </p>

        <hr style="opacity:.2;">

        <p style="color:#6B7280;font-size:13px;">
            © 2026 AirGuard AI | Version 2.0
        </p>

    </div>
    """