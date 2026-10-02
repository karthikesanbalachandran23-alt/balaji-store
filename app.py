import streamlit as st
from urllib.parse import quote
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="BALAJI MALIGAI",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SHOP DETAILS
# =========================================================

SHOP_NAME = "BALAJI MALIGAI"
PHONE = "7558110544"
WHATSAPP = "917558110544"
UPI_ID = "mmk541994@okicici"

ADDRESS = (
    "2/172 Main Road, Annapanpettai, "
    "Thirukadaiyur (PO), Mayiladuthurai (Dist)"
)

MAP_LINK = "https://maps.app.goo.gl/voLpdqGVrMMMGkXf8"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #0f2742;
    margin-bottom: 0;
}

.sub-title {
    font-size: 18px;
    color: #667085;
    margin-bottom: 20px;
}

.hero {
    background: linear-gradient(
        135deg,
        #07111f,
        #0f2742,
        #123b5d
    );
    padding: 40px;
    border-radius: 24px;
    color: white;
    margin: 20px 0 30px 0;
}

.hero h1 {
    font-size: 38px;
    margin: 0 0 10px 0;
}

.hero p {
    font-size: 18px;
    margin: 0;
    opacity: 0.9;
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #0f2742;
    margin-top: 30px;
    margin-bottom: 18px;
}

.product-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 10px;
    min-height: 220px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    text-align: center;
}

.product-emoji {
    font-size: 48px;
    margin-bottom: 10px;
}

.product-name {
    font-size: 18px;
    font-weight: 700;
    color: #102a43;
    min-height: 48px;
}

.product-unit {
    color: #667085;
    font-size: 14px;
    margin-top: 5px;
}

.product-price {
    color: #087f5b;
    font-size: 22px;
    font-weight: 800;
    margin-top: 8px;
}

.info-box {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 15px;
}

.footer {
    background: #07111f;
    color: white;
    padding: 30px;
    border-radius: 20px;
    margin-top: 40px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PRODUCTS
# =========================================================

PRODUCTS = [

    # ---------------- STAPLES ----------------

    {
        "name": "Sona Masoori Rice",
        "category": "Staples",
        "unit": "5 kg",
        "price": 300,
        "emoji": "🍚"
    },
    {
        "name": "Idli Rice",
        "category": "Staples",
        "unit": "5 kg",
        "price": 280,
        "emoji": "🍚"
    },
    {
        "name": "Raw Rice",
        "category": "Staples",
        "unit": "5 kg",
        "price": 290,
        "emoji": "🍚"
    },
    {
        "name": "Basmati Rice",
        "category": "Staples",
        "unit": "1 kg",
        "price": 140,
        "emoji": "🍚"
    },
    {
        "name": "Wheat",
        "category": "Staples",
        "unit": "1 kg",
        "price": 55,
        "emoji": "🌾"
    },
    {
        "name": "Rava",
        "category": "Staples",
        "unit": "500 g",
        "price": 35,
        "emoji": "🌾"
    },
    {
        "name": "Maida",
        "category": "Staples",
        "unit": "500 g",
        "price": 30,
        "emoji": "🌾"
    },
    {
        "name": "Besan Flour",
        "category": "Staples",
        "unit": "500 g",
        "price": 55,
        "emoji": "🌾"
    },
    {
        "name": "Poha",
        "category": "Staples",
        "unit": "500 g",
        "price": 45,
        "emoji": "🌾"
    },
    {
        "name": "Vermicelli",
        "category": "Staples",
        "unit": "500 g",
        "price": 50,
        "emoji": "🍜"
    },

    # ---------------- DAL ----------------

    {
        "name": "Toor Dal",
        "category": "Dal & Pulses",
        "unit": "1 kg",
        "price": 160,
        "emoji": "🫘"
    },
    {
        "name": "Urad Dal",
        "category": "Dal & Pulses",
        "unit": "1 kg",
        "price": 150,
        "emoji": "🫘"
    },
    {
        "name": "Moong Dal",
        "category": "Dal & Pulses",
        "unit": "1 kg",
        "price": 130,
        "emoji": "🫘"
    },
    {
        "name": "Chana Dal",
        "category": "Dal & Pulses",
        "unit": "1 kg",
        "price": 95,
        "emoji": "🫘"
    },
    {
        "name": "Masoor Dal",
        "category": "Dal & Pulses",
        "unit": "1 kg",
        "price": 110,
        "emoji": "🫘"
    },
    {
        "name": "Green Gram",
        "category": "Dal & Pulses",
        "unit": "500 g",
        "price": 75,
        "emoji": "🫘"
    },
    {
        "name": "Black Chana",
        "category": "Dal & Pulses",
        "unit": "500 g",
        "price": 55,
        "emoji": "🫘"
    },
    {
        "name": "White Peas",
        "category": "Dal & Pulses",
        "unit": "500 g",
        "price": 60,
        "emoji": "🫘"
    },
    {
        "name": "Rajma",
        "category": "Dal & Pulses",
        "unit": "500 g",
        "price": 75,
        "emoji": "🫘"
    },

    # ---------------- OIL & MASALA ----------------

    {
        "name": "Sunflower Oil",
        "category": "Oil & Masala",
        "unit": "1 litre",
        "price": 145,
        "emoji": "🫙"
    },
    {
        "name": "Groundnut Oil",
        "category": "Oil & Masala",
        "unit": "1 litre",
        "price": 180,
        "emoji": "🫙"
    },
    {
        "name": "Gingelly Oil",
        "category": "Oil & Masala",
        "unit": "1 litre",
        "price": 210,
        "emoji": "🫙"
    },
    {
        "name": "Coconut Oil",
        "category": "Oil & Masala",
        "unit": "500 ml",
        "price": 110,
        "emoji": "🥥"
    },
    {
        "name": "Turmeric Powder",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 30,
        "emoji": "🟡"
    },
    {
        "name": "Chilli Powder",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 35,
        "emoji": "🌶️"
    },
    {
        "name": "Coriander Powder",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 30,
        "emoji": "🌿"
    },
    {
        "name": "Cumin",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 45,
        "emoji": "🌿"
    },
    {
        "name": "Mustard Seeds",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 20,
        "emoji": "🌱"
    },
    {
        "name": "Pepper",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 70,
        "emoji": "⚫"
    },
    {
        "name": "Cardamom",
        "category": "Oil & Masala",
        "unit": "50 g",
        "price": 130,
        "emoji": "🌿"
    },
    {
        "name": "Cinnamon",
        "category": "Oil & Masala",
        "unit": "50 g",
        "price": 45,
        "emoji": "🪵"
    },
    {
        "name": "Garam Masala",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 55,
        "emoji": "🧂"
    },
    {
        "name": "Sambar Powder",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 40,
        "emoji": "🧂"
    },
    {
        "name": "Rasam Powder",
        "category": "Oil & Masala",
        "unit": "100 g",
        "price": 40,
        "emoji": "🧂"
    },

    # ---------------- SNACKS ----------------

    {
        "name": "Marie Biscuits",
        "category": "Snacks",
        "unit": "Pack",
        "price": 30,
        "emoji": "🍪"
    },
    {
        "name": "Good Day",
        "category": "Snacks",
        "unit": "Pack",
        "price": 35,
        "emoji": "🍪"
    },
    {
        "name": "Milk Bikis",
        "category": "Snacks",
        "unit": "Pack",
        "price": 25,
        "emoji": "🍪"
    },
    {
        "name": "Cream Biscuits",
        "category": "Snacks",
        "unit": "Pack",
        "price": 30,
        "emoji": "🍪"
    },
    {
        "name": "Lays",
        "category": "Snacks",
        "unit": "Pack",
        "price": 20,
        "emoji": "🥔"
    },
    {
        "name": "Kurkure",
        "category": "Snacks",
        "unit": "Pack",
        "price": 20,
        "emoji": "🥨"
    },
    {
        "name": "Mixture",
        "category": "Snacks",
        "unit": "250 g",
        "price": 60,
        "emoji": "🥜"
    },
    {
        "name": "Murukku",
        "category": "Snacks",
        "unit": "250 g",
        "price": 70,
        "emoji": "🥨"
    },
    {
        "name": "Popcorn",
        "category": "Snacks",
        "unit": "Pack",
        "price": 40,
        "emoji": "🍿"
    },
    {
        "name": "Nuts",
        "category": "Snacks",
        "unit": "250 g",
        "price": 180,
        "emoji": "🥜"
    },

    # ---------------- DAIRY ----------------

    {
        "name": "Fresh Milk",
        "category": "Dairy & Beverages",
        "unit": "1 litre",
        "price": 60,
        "emoji": "🥛"
    },
    {
        "name": "Curd",
        "category": "Dairy & Beverages",
        "unit": "500 g",
        "price": 40,
        "emoji": "🥛"
    },
    {
        "name": "Butter",
        "category": "Dairy & Beverages",
        "unit": "100 g",
        "price": 60,
        "emoji": "🧈"
    },
    {
        "name": "Paneer",
        "category": "Dairy & Beverages",
        "unit": "200 g",
        "price": 90,
        "emoji": "🧀"
    },
    {
        "name": "Horlicks",
        "category": "Dairy & Beverages",
        "unit": "500 g",
        "price": 220,
        "emoji": "🥤"
    },
    {
        "name": "Boost",
        "category": "Dairy & Beverages",
        "unit": "500 g",
        "price": 230,
        "emoji": "🥤"
    },
    {
        "name": "Health Drink",
        "category": "Dairy & Beverages",
        "unit": "500 g",
        "price": 220,
        "emoji": "🥤"
    },
    {
        "name": "Soft Drink",
        "category": "Dairy & Beverages",
        "unit": "1.25 litre",
        "price": 60,
        "emoji": "🥤"
    },

    # ---------------- CLEANING ----------------

    {
        "name": "Surf Excel",
        "category": "Cleaning",
        "unit": "1 kg",
        "price": 130,
        "emoji": "🧺"
    },
    {
        "name": "Rin",
        "category": "Cleaning",
        "unit": "1 kg",
        "price": 100,
        "emoji": "🧼"
    },
    {
        "name": "Vim Dishwash",
        "category": "Cleaning",
        "unit": "500 ml",
        "price": 80,
        "emoji": "🧽"
    },
    {
        "name": "Harpic",
        "category": "Cleaning",
        "unit": "500 ml",
        "price": 110,
        "emoji": "🧴"
    },
    {
        "name": "Floor Cleaner",
        "category": "Cleaning",
        "unit": "1 litre",
        "price": 120,
        "emoji": "🧹"
    },
    {
        "name": "Toilet Cleaner",
        "category": "Cleaning",
        "unit": "500 ml",
        "price": 100,
        "emoji": "🧴"
    },
    {
        "name": "Dishwash Bar",
        "category": "Cleaning",
        "unit": "1 pc",
        "price": 25,
        "emoji": "🧼"
    },
    {
        "name": "Scrub Pad",
        "category": "Cleaning",
        "unit": "1 pack",
        "price": 30,
        "emoji": "🧽"
    },
    {
        "name": "Garbage Bags",
        "category": "Cleaning",
        "unit": "1 pack",
        "price": 60,
        "emoji": "🗑️"
    },
    {
        "name": "Mosquito Coil",
        "category": "Cleaning",
        "unit": "1 pack",
        "price": 45,
        "emoji": "🦟"
    },

    # ---------------- PERSONAL CARE ----------------

    {
        "name": "Colgate",
        "category": "Personal Care",
        "unit": "100 g",
        "price": 65,
        "emoji": "🪥"
    },
    {
        "name": "Toothbrush",
        "category": "Personal Care",
        "unit": "1 pc",
        "price": 40,
        "emoji": "🪥"
    },
    {
        "name": "Lux Soap",
        "category": "Personal Care",
        "unit": "1 pc",
        "price": 40,
        "emoji": "🧼"
    },
    {
        "name": "Lifebuoy Soap",
        "category": "Personal Care",
        "unit": "1 pc",
        "price": 35,
        "emoji": "🧼"
    },
    {
        "name": "Dettol",
        "category": "Personal Care",
        "unit": "100 ml",
        "price": 55,
        "emoji": "🧴"
    },
    {
        "name": "Shampoo",
        "category": "Personal Care",
        "unit": "180 ml",
        "price": 120,
        "emoji": "🧴"
    },
    {
        "name": "Hair Oil",
        "category": "Personal Care",
        "unit": "100 ml",
        "price": 80,
        "emoji": "🧴"
    },
    {
        "name": "Face Wash",
        "category": "Personal Care",
        "unit": "100 ml",
        "price": 140,
        "emoji": "🧴"
    },
    {
        "name": "Hand Wash",
        "category": "Personal Care",
        "unit": "250 ml",
        "price": 90,
        "emoji": "🧴"
    },
    {
        "name": "Body Lotion",
        "category": "Personal Care",
        "unit": "200 ml",
        "price": 150,
        "emoji": "🧴"
    },

    # ---------------- STATIONERY ----------------

    {
        "name": "Pencil",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 10,
        "emoji": "✏️"
    },
    {
        "name": "Blue Pen",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 10,
        "emoji": "🖊️"
    },
    {
        "name": "Black Pen",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 10,
        "emoji": "🖊️"
    },
    {
        "name": "Red Pen",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 10,
        "emoji": "🖊️"
    },
    {
        "name": "Notebook",
        "category": "Stationery",
        "unit": "1 book",
        "price": 40,
        "emoji": "📓"
    },
    {
        "name": "Long Notebook",
        "category": "Stationery",
        "unit": "1 book",
        "price": 60,
        "emoji": "📒"
    },
    {
        "name": "Record Note",
        "category": "Stationery",
        "unit": "1 book",
        "price": 80,
        "emoji": "📔"
    },
    {
        "name": "Geometry Box",
        "category": "Stationery",
        "unit": "1 box",
        "price": 120,
        "emoji": "📐"
    },
    {
        "name": "Scale 30 cm",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 15,
        "emoji": "📏"
    },
    {
        "name": "Scissors",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 30,
        "emoji": "✂️"
    },
    {
        "name": "Eraser",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 5,
        "emoji": "◻️"
    },
    {
        "name": "Sharpener",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 5,
        "emoji": "🔪"
    },
    {
        "name": "Colour Pencils",
        "category": "Stationery",
        "unit": "12 colours",
        "price": 60,
        "emoji": "🖍️"
    },
    {
        "name": "Sketch Pens",
        "category": "Stationery",
        "unit": "12 colours",
        "price": 50,
        "emoji": "🖌️"
    },
    {
        "name": "Crayons",
        "category": "Stationery",
        "unit": "12 colours",
        "price": 50,
        "emoji": "🖍️"
    },
    {
        "name": "Water Colours",
        "category": "Stationery",
        "unit": "1 set",
        "price": 60,
        "emoji": "🎨"
    },
    {
        "name": "Glue Stick",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 20,
        "emoji": "🧴"
    },
    {
        "name": "Fevicol",
        "category": "Stationery",
        "unit": "50 g",
        "price": 30,
        "emoji": "🧴"
    },
    {
        "name": "A4 Paper",
        "category": "Stationery",
        "unit": "100 sheets",
        "price": 80,
        "emoji": "📄"
    },
    {
        "name": "File Folder",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 30,
        "emoji": "📁"
    },
    {
        "name": "Document File",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 40,
        "emoji": "📂"
    },
    {
        "name": "Sticky Notes",
        "category": "Stationery",
        "unit": "1 pad",
        "price": 30,
        "emoji": "🗒️"
    },
    {
        "name": "Paper Clips",
        "category": "Stationery",
        "unit": "1 box",
        "price": 20,
        "emoji": "📎"
    },
    {
        "name": "Binder Clips",
        "category": "Stationery",
        "unit": "1 box",
        "price": 30,
        "emoji": "📎"
    },
    {
        "name": "Writing Pad",
        "category": "Stationery",
        "unit": "1 pad",
        "price": 40,
        "emoji": "📝"
    },
    {
        "name": "Whiteboard Marker",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 25,
        "emoji": "🖊️"
    },
    {
        "name": "Highlighter",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 25,
        "emoji": "🖍️"
    },
    {
        "name": "Gel Pen",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 15,
        "emoji": "🖊️"
    },
    {
        "name": "Ball Pen Pack",
        "category": "Stationery",
        "unit": "5 pcs",
        "price": 50,
        "emoji": "🖊️"
    },
    {
        "name": "Pencil Box",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 80,
        "emoji": "📦"
    },
    {
        "name": "Pencil Pouch",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 100,
        "emoji": "👝"
    },
    {
        "name": "Drawing Book",
        "category": "Stationery",
        "unit": "1 book",
        "price": 50,
        "emoji": "🎨"
    },
    {
        "name": "Colouring Book",
        "category": "Stationery",
        "unit": "1 book",
        "price": 60,
        "emoji": "🎨"
    },
    {
        "name": "Chart Paper",
        "category": "Stationery",
        "unit": "1 sheet",
        "price": 10,
        "emoji": "📄"
    },
    {
        "name": "Craft Paper",
        "category": "Stationery",
        "unit": "1 pack",
        "price": 50,
        "emoji": "📄"
    },
    {
        "name": "Tape",
        "category": "Stationery",
        "unit": "1 roll",
        "price": 20,
        "emoji": "📏"
    },
    {
        "name": "Double-Sided Tape",
        "category": "Stationery",
        "unit": "1 roll",
        "price": 40,
        "emoji": "📏"
    },
    {
        "name": "Stapler",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 60,
        "emoji": "📎"
    },
    {
        "name": "Stapler Pins",
        "category": "Stationery",
        "unit": "1 box",
        "price": 20,
        "emoji": "📌"
    },
    {
        "name": "Calculator",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 150,
        "emoji": "🧮"
    },
    {
        "name": "Clipboard",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 50,
        "emoji": "📋"
    },
    {
        "name": "Notebook Set",
        "category": "Stationery",
        "unit": "3 books",
        "price": 100,
        "emoji": "📚"
    },
    {
        "name": "Spiral Notebook",
        "category": "Stationery",
        "unit": "1 book",
        "price": 70,
        "emoji": "📓"
    },
    {
        "name": "Project File",
        "category": "Stationery",
        "unit": "1 pc",
        "price": 40,
        "emoji": "📁"
    },
    {
        "name": "Brown Cover",
        "category": "Stationery",
        "unit": "1 pack",
        "price": 30,
        "emoji": "📄"
    },
    {
        "name": "Label Stickers",
        "category": "Stationery",
        "unit": "1 sheet",
        "price": 20,
        "emoji": "🏷️"
    }
]

# =========================================================
# SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}

# =========================================================
# FUNCTIONS
# =========================================================

def get_product(name):
    for product in PRODUCTS:
        if product["name"] == name:
            return product
    return None


def add_to_cart(name):
    st.session_state.cart[name] = (
        st.session_state.cart.get(name, 0) + 1
    )


def remove_one(name):
    if name in st.session_state.cart:
        st.session_state.cart[name] -= 1

        if st.session_state.cart[name] <= 0:
            del st.session_state.cart[name]


def cart_total():
    total = 0

    for name, qty in st.session_state.cart.items():
        product = get_product(name)

        if product:
            total += product["price"] * qty

    return total


def cart_count():
    return sum(st.session_state.cart.values())


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🛒 BALAJI MALIGAI")

    st.markdown("---")

    st.write("📞 **Phone**")
    st.write(PHONE)

    st.markdown("---")

    st.write("📍 **Address**")
    st.write(ADDRESS)

    st.markdown("---")

    st.write("🛒 **Cart Items**")
    st.metric("Items", cart_count())

    st.write("💰 **Cart Total**")
    st.metric("Total", f"₹{cart_total()}")

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🛒 BALAJI MALIGAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Groceries • Household • Personal Care • Stationery'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">
        <h1>Everything You Need, In One Place 🛍️</h1>
        <p>
            Quality groceries, household essentials and
            stationery at affordable prices.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SEARCH
# =========================================================

st.markdown(
    '<div class="section-title">🛍️ Shop Products</div>',
    unsafe_allow_html=True
)

search = st.text_input(
    "🔎 Search Product",
    placeholder="Search rice, pen, soap, biscuits..."
)

categories = ["All"] + sorted(
    list(set(p["category"] for p in PRODUCTS))
)

selected_category = st.selectbox(
    "📂 Category",
    categories
)

# =========================================================
# FILTER
# =========================================================

filtered_products = []

for product in PRODUCTS:

    search_match = (
        search.lower()
        in product["name"].lower()
    )

    category_match = (
        selected_category == "All"
        or product["category"] == selected_category
    )

    if search_match and category_match:
        filtered_products.append(product)

# =========================================================
# PRODUCTS
# =========================================================

if not filtered_products:

    st.warning("😕 Product not found.")

else:

    columns = st.columns(4)

    for index, product in enumerate(filtered_products):

        with columns[index % 4]:

            # IMPORTANT:
            # This is the only HTML product card.
            # unsafe_allow_html=True makes it render,
            # not display as code.

            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-emoji">
                        {product["emoji"]}
                    </div>

                    <div class="product-name">
                        {product["name"]}
                    </div>

                    <div class="product-unit">
                        {product["unit"]}
                    </div>

                    <div class="product-price">
                        ₹{product["price"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            name = product["name"]

            if st.button(
                "🛒 Add to Cart",
                key=f"add_{name}",
                use_container_width=True
            ):
                add_to_cart(name)
                st.rerun()

            qty = st.session_state.cart.get(name, 0)

            if qty > 0:

                c1, c2, c3 = st.columns(3)

                with c1:

                    if st.button(
                        "➖",
                        key=f"minus_{name}"
                    ):
                        remove_one(name)
                        st.rerun()

                with c2:

                    st.markdown(
                        f"<div style='text-align:center;"
                        f"font-weight:bold;"
                        f"padding-top:8px;'>"
                        f"{qty}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

                with c3:

                    if st.button(
                        "➕",
                        key=f"plus_{name}"
                    ):
                        add_to_cart(name)
                        st.rerun()

# =========================================================
# CART
# =========================================================

st.markdown(
    '<div class="section-title">🛒 Your Cart</div>',
    unsafe_allow_html=True
)

if not st.session_state.cart:

    st.info(
        "Your cart is empty. Add products to continue."
    )

else:

    for name, qty in list(
        st.session_state.cart.items()
    ):

        product = get_product(name)

        if not product:
            continue

        item_total = product["price"] * qty

        c1, c2, c3, c4 = st.columns(
            [4, 1, 2, 2]
        )

        with c1:
            st.write(
                f"{product['emoji']} **{name}**"
            )

        with c2:
            st.write(f"x {qty}")

        with c3:
            st.write(f"₹{item_total}")

        with c4:

            if st.button(
                "❌ Remove",
                key=f"cart_remove_{name}"
            ):
                del st.session_state.cart[name]
                st.rerun()

    st.markdown("---")

    st.subheader(
        f"💰 Total: ₹{cart_total()}"
    )

# =========================================================
# CHECKOUT
# =========================================================

st.markdown(
    '<div class="section-title">📦 Checkout</div>',
    unsafe_allow_html=True
)

if st.session_state.cart:

    customer_name = st.text_input(
        "👤 Customer Name"
    )

    customer_phone = st.text_input(
        "📱 Phone Number"
    )

    customer_address = st.text_area(
        "🏠 Delivery Address"
    )

    notes = st.text_area(
        "📝 Order Notes"
    )

    # =====================================================
    # PAYMENT
    # =====================================================

    st.markdown(
        '<div class="section-title">💳 Scan & Pay</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Scan this QR using PhonePe / Google Pay / Paytm "
        "or another UPI app."
    )

    qr_file = Path("payment_qr.jpg")

    if qr_file.exists():

        st.image(
            str(qr_file),
            caption="BALAJI MALIGAI - Scan & Pay",
            width=320
        )

    else:

        st.error(
            "payment_qr.jpg file not found."
        )

        st.write(
            "Put payment_qr.jpg in the same folder "
            "as app.py."
        )

    st.write(
        f"💳 **UPI ID:** `{UPI_ID}`"
    )

    st.caption(
        "After payment, send the payment screenshot "
        "along with your order on WhatsApp."
    )

    # =====================================================
    # WHATSAPP MESSAGE
    # =====================================================

    message = []

    message.append(
        "🛒 BALAJI MALIGAI ORDER"
    )

    message.append("")

    message.append(
        f"👤 Name: {customer_name}"
    )

    message.append(
        f"📱 Phone: {customer_phone}"
    )

    message.append(
        f"🏠 Address: {customer_address}"
    )

    message.append("")

    message.append(
        "📦 ORDER ITEMS"
    )

    for name, qty in st.session_state.cart.items():

        product = get_product(name)

        if product:

            amount = product["price"] * qty

            message.append(
                f"{product['emoji']} "
                f"{name} x {qty} = ₹{amount}"
            )

    message.append("")

    message.append(
        f"💰 TOTAL: ₹{cart_total()}"
    )

    message.append("")

    message.append(
        "💳 Payment: UPI"
    )

    message.append(
        f"UPI ID: {UPI_ID}"
    )

    if notes:

        message.append("")

        message.append(
            f"📝 Notes: {notes}"
        )

    whatsapp_message = "\n".join(message)

    whatsapp_url = (
        f"https://wa.me/{WHATSAPP}"
        f"?text={quote(whatsapp_message)}"
    )

    st.markdown(
        f"""
        <a href="{whatsapp_url}" target="_blank"
           style="text-decoration:none;">

            <div style="
                background:#25D366;
                color:white;
                padding:15px;
                text-align:center;
                border-radius:12px;
                font-size:18px;
                font-weight:bold;
                margin-top:15px;
            ">
                📲 SEND ORDER ON WHATSAPP
            </div>

        </a>
        """,
        unsafe_allow_html=True
    )

else:

    st.info(
        "🛒 Add products to your cart first."
    )

# =========================================================
# FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">✨ Why Shop With Us?</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(
        """
        <div class="info-box">
            <h3>🛍️ Easy Shopping</h3>
            <p>
                Search products and add them
                to your cart easily.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        """
        <div class="info-box">
            <h3>💳 UPI Payment</h3>
            <p>
                Scan the QR code and pay
                using your UPI app.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        """
        <div class="info-box">
            <h3>📲 WhatsApp Order</h3>
            <p>
                Send your complete order
                directly through WhatsApp.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:

    st.markdown(
        """
        <div class="info-box">
            <h3>🏠 Home Delivery</h3>
            <p>
                Enter your delivery address
                during checkout.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CONTACT
# =========================================================

st.markdown(
    '<div class="section-title">📞 Contact Us</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
        <div class="info-box">

            <h3>🏪 {SHOP_NAME}</h3>

            <p>📞 <b>{PHONE}</b></p>

            <p>💳 <b>{UPI_ID}</b></p>

            <p>📍 {ADDRESS}</p>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.link_button(
        "📍 Open Google Maps",
        MAP_LINK,
        use_container_width=True
    )

    st.link_button(
        "📲 WhatsApp",
        f"https://wa.me/{WHATSAPP}",
        use_container_width=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    f"""
    <div class="footer">

        <h2>🛒 {SHOP_NAME}</h2>

        <p>
            Groceries • Household • Personal Care • Stationery
        </p>

        <p>
            📞 {PHONE} &nbsp; | &nbsp;
            💳 {UPI_ID}
        </p>

        <p>
            © 2026 {SHOP_NAME}
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
