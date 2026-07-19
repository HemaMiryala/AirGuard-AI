def get_custom_css():
    return """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    *{
        font-family:'Inter',sans-serif;
    }

    /* ===========================================
       Animated Background
    =========================================== */

    @keyframes gradientBG{
        0%{background-position:0% 50%;}
        50%{background-position:100% 50%;}
        100%{background-position:0% 50%;}
    }

    .stApp{
        background:linear-gradient(-45deg,#e0eafc,#cfdef3,#e2e2e2,#fdfbfb);
        background-size:400% 400%;
        animation:gradientBG 15s ease infinite;
    }

    /* ===========================================
       Hide Streamlit Branding
    =========================================== */

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    #MainMenu{
        visibility:hidden;
    }

    /* ===========================================
       Sidebar
    =========================================== */

    section[data-testid="stSidebar"]{
        background:rgba(16,55,92,0.96)!important;
        backdrop-filter:blur(12px);
        border-right:1px solid rgba(255,255,255,.15);
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p{
        color:white!important;
    }

    section[data-testid="stSidebar"] .stMarkdown{
        color:white!important;
    }

    /* ===========================================
       SELECT BOX (FIX)
    =========================================== */

    div[data-baseweb="select"]{
        background:white!important;
        border-radius:12px!important;
        border:1px solid #CBD5E1!important;
    }

    div[data-baseweb="select"] *{
        color:#1E293B!important;
    }

    div[data-baseweb="select"] span{
        color:#1E293B!important;
        font-weight:600!important;
    }

    div[data-baseweb="select"] svg{
        fill:#1E293B!important;
    }

    div[role="listbox"]{
        background:white!important;
        border-radius:12px!important;
    }

    div[role="option"]{
        color:#1E293B!important;
        background:white!important;
    }

    div[role="option"]:hover{
        background:#E2E8F0!important;
    }

    /* ===========================================
       RADIO BUTTONS
    =========================================== */

    div[role="radiogroup"]{
        background:rgba(255,255,255,.90);
        border-radius:12px;
        padding:10px;
    }

    div[role="radiogroup"] label{
        color:#1E293B!important;
        font-weight:600;
    }

    /* ===========================================
       BUTTONS
    =========================================== */

    .stButton>button{

        width:100%;
        height:55px;

        border:none;
        border-radius:15px;

        color:white!important;

        font-size:18px;
        font-weight:700;

        background:linear-gradient(135deg,#1976D2,#1259A7);

        transition:.35s;

        box-shadow:
        0 10px 25px rgba(25,118,210,.35);
    }

    .stButton>button:hover{

        transform:translateY(-3px);

        background:
        linear-gradient(135deg,#1565C0,#0D47A1);

        box-shadow:
        0 14px 35px rgba(25,118,210,.45);
    }

    /* ===========================================
       METRIC CARDS
    =========================================== */

    [data-testid="metric-container"]{

        background:
        rgba(255,255,255,.70);

        backdrop-filter:blur(12px);

        border-radius:20px;

        padding:20px;

        border:
        1px solid rgba(255,255,255,.80);

        box-shadow:
        0 8px 25px rgba(0,0,0,.08);

        transition:.3s;
    }

    [data-testid="metric-container"]:hover{

        transform:translateY(-5px);

        box-shadow:
        0 15px 35px rgba(0,0,0,.12);

    }

    [data-testid="stMetricLabel"]{

        color:#475569!important;

        font-weight:600;
    }

    [data-testid="stMetricValue"]{

        color:#10375C!important;

        font-size:28px!important;

        font-weight:700!important;
    }

    /* ===========================================
       HEADINGS
    =========================================== */

    h1{
        color:#10375C!important;
    }

    h2,h3,h4,h5{

        color:#334155!important;
    }

    p,span,li{

        color:#475569;
    }

    /* ===========================================
       DATAFRAME
    =========================================== */

    table{

        background:white!important;

        border-radius:15px;

        overflow:hidden;

    }

    table *{

        color:#334155!important;

    }

    /* ===========================================
       ALERTS
    =========================================== */

    div[data-testid="stAlert"]{

        border-radius:15px;

    }

    /* ===========================================
       EXPANDERS
    =========================================== */

    details{

        background:
        rgba(255,255,255,.75);

        border-radius:16px;

        padding:10px;

        margin-bottom:12px;

        border:1px solid rgba(255,255,255,.65);

    }

    /* ===========================================
       GLASS CARD
    =========================================== */

    .glass-card{

        background:
        rgba(255,255,255,.75);

        backdrop-filter:blur(12px);

        border-radius:22px;

        padding:24px;

        border:
        1px solid rgba(255,255,255,.70);

        box-shadow:
        0 8px 30px rgba(0,0,0,.06);

        margin-bottom:20px;
    }

    /* ===========================================
       DOWNLOAD BUTTON
    =========================================== */

    div.stDownloadButton>button{

        background:#0F6CBD!important;

        color:white!important;

        border-radius:12px;

        border:none;

    }

    div.stDownloadButton>button:hover{

        background:#0C5AA6!important;

    }

    </style>
    """
def get_hero_section():
    return """
    <div style="
        text-align:center;
        padding:45px 20px;
        margin-bottom:10px;
    ">

        <h1 style="
            font-size:58px;
            font-weight:700;
            margin-bottom:10px;
            background:linear-gradient(90deg,#10375C,#1976D2);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
            background-clip:text;
        ">
            🌍 AirGuard AI
        </h1>

        <p style="
            font-size:24px;
            color:#5F6B7A;
            font-weight:400;
            margin-top:5px;
            margin-bottom:20px;
        ">
            Next-Generation Air Quality Intelligence & Prediction
        </p>

        <div style="
            display:inline-block;
            padding:12px 24px;
            border-radius:50px;
            background:rgba(255,255,255,0.70);
            backdrop-filter:blur(10px);
            border:1px solid rgba(255,255,255,0.60);
            box-shadow:0 8px 25px rgba(0,0,0,0.08);
            font-size:16px;
            color:#334155;
            font-weight:600;
        ">
            🤖 AI Powered • 🌤 Live Weather • 🌫 Real-Time AQI • 📈 Tomorrow Prediction
        </div>

    </div>
    """


def get_footer():
    return """
    <br>

    <div style="
        margin-top:40px;
        padding:35px;
        border-radius:22px;
        text-align:center;
        background:linear-gradient(135deg,#10375C,#0A2540);
        color:white;
        box-shadow:0 10px 35px rgba(0,0,0,.18);
    ">

        <h2 style="
            color:white;
            margin-bottom:10px;
            font-size:28px;
        ">
            🌍 AirGuard AI
        </h2>

        <p style="
            color:#E2E8F0;
            font-size:17px;
            margin-bottom:8px;
        ">
            AI-Powered Air Quality Prediction & Health Advisory System
        </p>

        <hr style="
            opacity:0.20;
            margin:20px 0;
        ">

        <div style="
            display:flex;
            justify-content:center;
            gap:30px;
            flex-wrap:wrap;
            color:#CBD5E1;
            font-size:15px;
        ">

            <span>🤖 Random Forest</span>
            <span>📊 Streamlit</span>
            <span>🌤 OpenWeather API</span>
            <span>📈 Plotly</span>

        </div>

        <div style="
            margin-top:22px;
            color:#94A3B8;
            font-size:14px;
        ">
            Built with ❤️ for AI Hackathon 2026
        </div>

        <div style="
            margin-top:8px;
            color:#64748B;
            font-size:13px;
        ">
            Version 2.0 • © 2026 AirGuard AI • All Rights Reserved
        </div>

    </div>
    """