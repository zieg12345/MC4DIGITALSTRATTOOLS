def get_css():
    return """
    <style>
    /* Target the main Streamlit app container for background image */
    .stApp {
        background-image: url('https://images.alphacoders.com/116/1163408.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
    }

    /* Main content with semi-transparent background for readability */
    .main-content {
        padding: 20px;
        background-color: rgba(245, 245, 245, 0.85); /* Slightly transparent #f5f5f5 */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #2b2b2b;
        margin-bottom: 20px;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }

    /* Sidebar styling */
    .css-1lcbmhc { 
        background-color: rgba(224, 224, 224, 0.9);
        padding: 20px;
        border-radius: 10px;
        transition: all 0.3s ease;
        width: 250px;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }

    /* Sidebar content */
    .sidebar-content {
        display: none;
    }
    .sidebar-content.active {
        display: block;
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        margin-bottom: 10px;
        padding: 12px;
        background-color: #b0b0b0;
        color: #2b2b2b;
        border: none;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease;
        font-size: 16px;
        font-weight: 500;
        text-align: center;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }
    .stButton > button:hover {
        background-color: #909090;
        transform: scale(1.03);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    /* Download button styling (if used in imported sections) */
    .stDownloadButton > button {
        background-color: #b0b0b0;
        color: #2b2b2b;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease;
        font-size: 16px;
        font-weight: 500;
        padding: 12px;
        width: 100%;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }
    .stDownloadButton > button:hover {
        background-color: #909090;
        transform: scale(1.03);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    /* Header styling */
    h1 {
        text-align: center;
        color: #2b2b2b;
        font-size: 24px;
        font-weight: 600;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }

    /* Burger button */
    .burger-button {
        font-size: 24px;
        cursor: pointer;
        color: #2b2b2b;
        margin-bottom: 15px;
        background: none;
        border: none;
        padding: 5px;
        transition: all 0.2s ease;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }
    .burger-button:hover {
        color: #606060;
    }

    /* DataFrame styling */
    .stDataFrame {
        border: 1px solid #d0d0d0;
        border-radius: 5px;
        background-color: #ffffff;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }

    /* Dashboard iframe */
    .dashboard-iframe {
        border: none;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 100%;
        height: 600px;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        color: #666666;
        margin-top: 20px;
        font-size: 12px;
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .css-1lcbmhc { 
            width: 100%;
            padding: 10px;
        }
        .stButton > button {
            font-size: 14px;
            padding: 10px;
        }
        .stDownloadButton > button {
            font-size: 14px;
            padding: 10px;
        }
        h1 {
            font-size: 20px;
        }
        .dashboard-iframe {
            height: 400px;
        }
    }

    /* Add white stroke to all text elements */
    body, p, h1, h2, h3, h4, h5, h6, button, .stAlert, .stMarkdown, .stText, .stDataFrame, .stTable, 
    .stSelectbox, .stTextInput, .stButton, .stDownloadButton {
        text-shadow: 
            -2px -2px 0 #ffffff,
            2px -2px 0 #ffffff,
            -2px 2px 0 #ffffff,
            2px 2px 0 #ffffff,
            -2px 0 0 #ffffff,
            2px 0 0 #ffffff,
            0 -2px 0 #ffffff,
            0 2px 0 #ffffff;
    }
    </style>
    """

motivational_quotes = [
    "Trust in your inner strength—you’ve already crossed half the journey. – Zieg",
    "Exceptional work blooms from a heart that loves its craft. – Zieg",
    "True success lies in the bravery to press forward despite challenges. – Zieg",
    "The boundaries you see are merely shadows of your own imagination. – Zieg",
    "Set grand goals, toil relentlessly, remain steadfast, and choose wise companions. – Zieg",
    "Tomorrow is crafted by those who envision their dreams with wonder. – Zieg",
    "Don’t follow the ticking clock—mirror its persistence and keep advancing. – Zieg",
    "No age can stop you from pursuing new dreams or crafting fresh ambitions. – Zieg",
    "The greatest prize of your achievements is the person you grow into. – Zieg",
    "Launch from your current place, with your present tools, and give your all. – Zieg"
]