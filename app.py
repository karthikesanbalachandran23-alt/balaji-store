import streamlit as st
from urllib.parse import quote

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="BALAJI MALIGAI | Fresh Groceries",
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

MAP_URL = "https://maps.app.goo.gl/voLpdqGVrMMMGkXf8"

# =========================================================
# PRODUCTS
# =========================================================

PRODUCTS = [

    # ---------------- STAPLES ----------------

    {
        "name": "Premium Rice",
        "category": "Staples",
        "unit": "5 kg",
        "price": 320,
        "emoji": "🍚"
    },
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
        "name": "Toor Dal",
        "category": "Staples",
        "unit": "1 kg",
        "price": 145,
        "emoji": "🫘"
    },
    {
        "name": "Sugar",
        "category": "Staples",
        "unit": "1 kg",
        "price": 48,
        "emoji": "🍬"
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

    # ---------------- DAL & PULSES ----------------

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

    # ---------------- VEGETABLES ----------------

    {
        "name": "Fresh Tomato",
        "category": "Vegetables",
        "unit": "1 kg",
        "price": 55,
        "emoji": "🍅"
    },
    {
        "name": "Fresh Onion",
        "category": "Vegetables",
        "unit": "1 kg",
        "price": 60,
        "emoji": "🧅"
    },
    {
        "name": "Potato",
        "category": "Vegetables",
        "unit": "1 kg",
        "price": 50,
        "emoji": "🥔"
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

    # ---------------- DAIRY ----------------

    {
        "name": "Fresh Milk",
        "category": "Dairy",
        "unit": "1 litre",
        "price": 60,
        "emoji": "🥛"
    },
    {
        "name": "Curd",
        "category": "Dairy",
        "unit": "500 ml",
        "price": 35,
        "emoji": "🥣"
    },
    {
        "name": "Butter",
        "category": "Dairy",
        "unit": "100 g",
        "price": 60,
        "emoji": "🧈"
    },
    {
        "name": "Paneer",
        "category": "Dairy",
        "unit": "200 g",
        "price": 90,
        "emoji": "🧀"
    },

    # ---------------- SNACKS ----------------

    {
        "name": "Biscuits",
        "category": "Snacks",
        "unit": "Pack",
        "price": 30,
        "emoji": "🍪"
    },
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
        "name": "Potato Chips",
        "category": "Snacks",
        "unit": "Pack",
        "price": 40,
        "emoji": "🥔"
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
    {
        "name": "Chocolate",
        "category": "Snacks",
        "unit": "Pack",
        "price": 50,
        "emoji": "🍫"
    },

    # ---------------- BEVERAGES ----------------

    {
        "name": "Tea Powder",
        "category": "Beverages",
        "unit": "250 g",
        "price": 120,
        "emoji": "🍵"
    },
    {
        "name": "Coffee Powder",
        "category": "Beverages",
        "unit": "250 g",
        "price": 150,
        "emoji": "☕"
    },
    {
        "name": "Horlicks",
        "category": "Beverages",
        "unit": "500 g",
        "price": 220,
        "emoji": "🥤"
    },
    {
        "name": "Boost",
        "category": "Beverages",
        "unit": "500 g",
        "price": 230,
        "emoji": "🥤"
    },
    {
        "name": "Health Drink",
        "category": "Beverages",
        "unit": "500 g",
        "price": 220,
        "emoji": "🥤"
    },
    {
        "name": "Soft Drink",
        "category": "Beverages",
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

    # =====================================================
    # STATIONERY
    # =====================================================

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


def cart_count():
    return sum(st.session_state.cart.values())


def cart_total():
    total = 0

    for name, quantity in st.session_state.cart.items():
        product = get_product(name)

        if product:
            total += product["price"] * quantity

    return total


def add_to_cart(name):
    st.session_state.cart[name] = (
        st.session_state.cart.get(name, 0) + 1
    )


def decrease_cart(name):
    if name in st.session_state.cart:
        st.session_state.cart[name] -= 1

        if st.session_state.cart[name] <= 0:
            del st.session_state.cart[name]


def create_order_message(
    customer_name,
    customer_phone,
    customer_address,
    payment_method
):
    lines = [
        f"*{SHOP_NAME} - NEW ORDER*",
        "",
        "*ORDER DETAILS*"
    ]

    for name, quantity in st.session_state.cart.items():
        product = get_product(name)

        if product:
            item_total = product["price"] * quantity

            lines.append(
                f"{product['emoji']} "
                f"{product['name']} x {quantity} = ₹{item_total}"
            )

    lines.extend([
        "",
        f"*TOTAL: ₹{cart_total()}*",
        "",
        f"*PAYMENT: {payment_method}*",
        "",
        "*CUSTOMER DETAILS*",
        f"Name: {customer_name}",
        f"Phone: {customer_phone}",
        f"Address: {customer_address}",
        "",
        "Thank you for ordering from BALAJI MALIGAI!"
    ])

    return "\n".join(lines)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🛒 BALAJI MALIGAI")

    st.write("Fresh groceries at your doorstep.")

    st.divider()

    st.subheader("📌 Shop Details")

    st.write(f"📞 **{PHONE}**")

    st.write("💬 WhatsApp Available")

    st.divider()

    st.subheader("📍 Shop Address")

    st.write(ADDRESS)

    st.link_button(
        "🗺️ Open Google Maps",
        MAP_URL,
        use_container_width=True
    )

    st.divider()

    st.subheader("🛍️ Your Cart")

    st.metric("Items", cart_count())

    st.metric("Total", f"₹{cart_total()}")


# =========================================================
# MAIN HEADER
# =========================================================

st.title("🛒 BALAJI MALIGAI")

st.subheader(
    "Fresh Groceries • Quality Products • Easy Ordering"
)

st.write(
    "Your local grocery shop for everyday essentials."
)

st.divider()

# =========================================================
# HERO
# =========================================================

st.header("🛍️ Shop Fresh. Shop Easy.")

st.write(
    "Choose your favourite products, "
    "add them to your cart and order directly through WhatsApp."
)

hero1, hero2, hero3 = st.columns(3)

with hero1:
    st.info("🥦 Fresh Products")

with hero2:
    st.info("💰 Affordable Prices")

with hero3:
    st.info("📱 WhatsApp Ordering")

st.divider()

# =========================================================
# PRODUCT SECTION
# =========================================================

st.header("🛍️ Our Products")

search = st.text_input(
    "🔎 Search Products",
    placeholder="Search rice, pen, milk..."
)

categories = ["All"]

for product in PRODUCTS:
    if product["category"] not in categories:
        categories.append(product["category"])

selected_category = st.selectbox(
    "📂 Select Category",
    categories
)

# =========================================================
# FILTER
# =========================================================

filtered_products = []

for product in PRODUCTS:

    matches_search = (
        not search
        or search.lower() in product["name"].lower()
    )

    matches_category = (
        selected_category == "All"
        or product["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_products.append(product)

# =========================================================
# PRODUCT CARDS
# =========================================================

if not filtered_products:

    st.warning("No products found.")

else:

    for i in range(0, len(filtered_products), 3):

        cols = st.columns(3)

        row_products = filtered_products[i:i + 3]

        for col, product in zip(cols, row_products):

            with col:

                with st.container(border=True):

                    st.subheader(
                        f"{product['emoji']} {product['name']}"
                    )

                    st.write(product["unit"])

                    st.markdown(
                        f"### ₹{product['price']}"
                    )

                    if st.button(
                        "🛒 Add to Cart",
                        key=f"add_{product['name']}",
                        use_container_width=True
                    ):
                        add_to_cart(product["name"])
                        st.rerun()

                    quantity = st.session_state.cart.get(
                        product["name"],
                        0
                    )

                    q1, q2, q3 = st.columns(3)

                    with q1:

                        if st.button(
                            "−",
                            key=f"minus_{product['name']}",
                            use_container_width=True
                        ):
                            decrease_cart(product["name"])
                            st.rerun()

                    with q2:

                        st.markdown(
                            f"<div style='text-align:center;"
                            f"font-size:20px;"
                            f"padding-top:5px;'>"
                            f"{quantity}"
                            f"</div>",
                            unsafe_allow_html=True
                        )

                    with q3:

                        if st.button(
                            "+",
                            key=f"plus_{product['name']}",
                            use_container_width=True
                        ):
                            add_to_cart(product["name"])
                            st.rerun()


# =========================================================
# CART
# =========================================================

st.divider()

st.header("🛒 Your Cart")

if not st.session_state.cart:

    st.info("Your cart is empty.")

else:

    for name, quantity in list(
        st.session_state.cart.items()
    ):

        product = get_product(name)

        if product:

            item_total = product["price"] * quantity

            c1, c2, c3, c4 = st.columns(
                [4, 1, 1, 2]
            )

            with c1:
                st.write(
                    f"{product['emoji']} "
                    f"**{product['name']}**"
                )

            with c2:
                st.write(f"x {quantity}")

            with c3:
                st.write(f"₹{item_total}")

            with c4:

                if st.button(
                    "Remove",
                    key=f"remove_{name}"
                ):
                    del st.session_state.cart[name]
                    st.rerun()

    st.success(
        f"### Cart Total: ₹{cart_total()}"
    )

# =========================================================
# CHECKOUT
# =========================================================

if st.session_state.cart:

    st.divider()

    st.header("📦 Checkout")

    customer_name = st.text_input(
        "👤 Customer Name"
    )

    customer_phone = st.text_input(
        "📞 Phone Number"
    )

    customer_address = st.text_area(
        "📍 Delivery Address"
    )

    payment_method = st.selectbox(
        "💳 Payment Method",
        [
            "Cash on Delivery",
            "UPI"
        ]
    )

    if payment_method == "UPI":

        st.info(
            f"UPI ID: **{UPI_ID}**"
        )

        upi_link = (
            "upi://pay?"
            f"pa={quote(UPI_ID)}"
            f"&pn={quote(SHOP_NAME)}"
            f"&am={cart_total()}"
            "&cu=INR"
        )

        st.link_button(
            "💳 Pay using UPI",
            upi_link,
            use_container_width=True
        )

    order_message = create_order_message(
        customer_name,
        customer_phone,
        customer_address,
        payment_method
    )

    whatsapp_url = (
        f"https://wa.me/{WHATSAPP}"
        f"?text={quote(order_message)}"
    )

    if st.button(
        "📱 Order on WhatsApp",
        type="primary",
        use_container_width=True
    ):

        if (
            not customer_name
            or not customer_phone
            or not customer_address
        ):

            st.error(
                "Please fill all customer details."
            )

        else:

            st.markdown(
                f"[📱 Click here to send your order "
                f"on WhatsApp]({whatsapp_url})"
            )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.subheader("📍 BALAJI MALIGAI")

st.write(ADDRESS)

st.write(f"📞 Phone: {PHONE}")

st.write(
    "🛒 Thank you for shopping with BALAJI MALIGAI!"
)