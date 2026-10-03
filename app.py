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
MAP_URL = "https://maps.app.goo.gl/voLpdqGVrMMMGKXf8"

# =========================================================
# PRODUCTS
# =========================================================
PRODUCTS = [

    # ---------------- STAPLES ----------------
    {
        "name": "Sona Masoori Rice",
        "category": "Staples",
        "price": 300,
        "unit": "5 kg",
        "emoji": "🍚"
    },
    {
        "name": "Idli Rice",
        "category": "Staples",
        "price": 280,
        "unit": "5 kg",
        "emoji": "🍚"
    },
    {
        "name": "Raw Rice",
        "category": "Staples",
        "price": 290,
        "unit": "5 kg",
        "emoji": "🍚"
    },
    {
        "name": "Basmati Rice",
        "category": "Staples",
        "price": 140,
        "unit": "1 kg",
        "emoji": "🍚"
    },
    {
        "name": "Wheat",
        "category": "Staples",
        "price": 55,
        "unit": "1 kg",
        "emoji": "🌾"
    },
    {
        "name": "Rava",
        "category": "Staples",
        "price": 35,
        "unit": "500 g",
        "emoji": "🌾"
    },
    {
        "name": "Maida",
        "category": "Staples",
        "price": 30,
        "unit": "500 g",
        "emoji": "🌾"
    },
    {
        "name": "Besan Flour",
        "category": "Staples",
        "price": 55,
        "unit": "500 g",
        "emoji": "🌾"
    },
    {
        "name": "Poha",
        "category": "Staples",
        "price": 45,
        "unit": "500 g",
        "emoji": "🥣"
    },
    {
        "name": "Vermicelli",
        "category": "Staples",
        "price": 50,
        "unit": "500 g",
        "emoji": "🍜"
    },

    # ---------------- DAL & PULSES ----------------
    {
        "name": "Urad Dal",
        "category": "Dal & Pulses",
        "price": 150,
        "unit": "1 kg",
        "emoji": "🫘"
    },
    {
        "name": "Moong Dal",
        "category": "Dal & Pulses",
        "price": 130,
        "unit": "1 kg",
        "emoji": "🫘"
    },
    {
        "name": "Chana Dal",
        "category": "Dal & Pulses",
        "price": 95,
        "unit": "1 kg",
        "emoji": "🫘"
    },
    {
        "name": "Masoor Dal",
        "category": "Dal & Pulses",
        "price": 110,
        "unit": "1 kg",
        "emoji": "🫘"
    },
    {
        "name": "Green Gram",
        "category": "Dal & Pulses",
        "price": 75,
        "unit": "500 g",
        "emoji": "🫘"
    },
    {
        "name": "Black Chana",
        "category": "Dal & Pulses",
        "price": 55,
        "unit": "500 g",
        "emoji": "🫘"
    },
    {
        "name": "White Peas",
        "category": "Dal & Pulses",
        "price": 60,
        "unit": "500 g",
        "emoji": "🫘"
    },
    {
        "name": "Rajma",
        "category": "Dal & Pulses",
        "price": 75,
        "unit": "500 g",
        "emoji": "🫘"
    },

    # ---------------- OIL & MASALA ----------------
    {
        "name": "Sunflower Oil",
        "category": "Oil & Masala",
        "price": 145,
        "unit": "1 litre",
        "emoji": "🫙"
    },
    {
        "name": "Groundnut Oil",
        "category": "Oil & Masala",
        "price": 180,
        "unit": "1 litre",
        "emoji": "🫙"
    },
    {
        "name": "Gingelly Oil",
        "category": "Oil & Masala",
        "price": 210,
        "unit": "1 litre",
        "emoji": "🫙"
    },
    {
        "name": "Coconut Oil",
        "category": "Oil & Masala",
        "price": 110,
        "unit": "500 ml",
        "emoji": "🥥"
    },
    {
        "name": "Turmeric Powder",
        "category": "Oil & Masala",
        "price": 30,
        "unit": "100 g",
        "emoji": "🟡"
    },
    {
        "name": "Chilli Powder",
        "category": "Oil & Masala",
        "price": 35,
        "unit": "100 g",
        "emoji": "🌶️"
    },
    {
        "name": "Coriander Powder",
        "category": "Oil & Masala",
        "price": 30,
        "unit": "100 g",
        "emoji": "🌿"
    },
    {
        "name": "Cumin",
        "category": "Oil & Masala",
        "price": 45,
        "unit": "100 g",
        "emoji": "🌿"
    },
    {
        "name": "Mustard Seeds",
        "category": "Oil & Masala",
        "price": 20,
        "unit": "100 g",
        "emoji": "🌱"
    },
    {
        "name": "Pepper",
        "category": "Oil & Masala",
        "price": 70,
        "unit": "100 g",
        "emoji": "⚫"
    },
    {
        "name": "Cardamom",
        "category": "Oil & Masala",
        "price": 130,
        "unit": "50 g",
        "emoji": "🌿"
    },
    {
        "name": "Cinnamon",
        "category": "Oil & Masala",
        "price": 45,
        "unit": "50 g",
        "emoji": "🪵"
    },
    {
        "name": "Garam Masala",
        "category": "Oil & Masala",
        "price": 55,
        "unit": "100 g",
        "emoji": "🧂"
    },
    {
        "name": "Sambar Powder",
        "category": "Oil & Masala",
        "price": 40,
        "unit": "100 g",
        "emoji": "🧂"
    },
    {
        "name": "Rasam Powder",
        "category": "Oil & Masala",
        "price": 40,
        "unit": "100 g",
        "emoji": "🧂"
    },

    # ---------------- SNACKS ----------------
    {
        "name": "Marie Biscuits",
        "category": "Snacks",
        "price": 30,
        "unit": "Pack",
        "emoji": "🍪"
    },
    {
        "name": "Good Day",
        "category": "Snacks",
        "price": 35,
        "unit": "Pack",
        "emoji": "🍪"
    },
    {
        "name": "Milk Bikis",
        "category": "Snacks",
        "price": 25,
        "unit": "Pack",
        "emoji": "🍪"
    },
    {
        "name": "Cream Biscuits",
        "category": "Snacks",
        "price": 30,
        "unit": "Pack",
        "emoji": "🍪"
    },
    {
        "name": "Lays",
        "category": "Snacks",
        "price": 20,
        "unit": "Pack",
        "emoji": "🥔"
    },
    {
        "name": "Kurkure",
        "category": "Snacks",
        "price": 20,
        "unit": "Pack",
        "emoji": "🥨"
    },
    {
        "name": "Mixture",
        "category": "Snacks",
        "price": 60,
        "unit": "250 g",
        "emoji": "🥜"
    },
    {
        "name": "Murukku",
        "category": "Snacks",
        "price": 70,
        "unit": "250 g",
        "emoji": "🥨"
    },
    {
        "name": "Popcorn",
        "category": "Snacks",
        "price": 40,
        "unit": "Pack",
        "emoji": "🍿"
    },
    {
        "name": "Nuts",
        "category": "Snacks",
        "price": 180,
        "unit": "250 g",
        "emoji": "🥜"
    },

    # ---------------- DAIRY & BEVERAGES ----------------
    {
        "name": "Fresh Milk",
        "category": "Dairy & Beverages",
        "price": 30,
        "unit": "500 ml",
        "emoji": "🥛"
    },
    {
        "name": "Curd",
        "category": "Dairy & Beverages",
        "price": 35,
        "unit": "500 g",
        "emoji": "🥛"
    },
    {
        "name": "Butter",
        "category": "Dairy & Beverages",
        "price": 60,
        "unit": "100 g",
        "emoji": "🧈"
    },
    {
        "name": "Paneer",
        "category": "Dairy & Beverages",
        "price": 90,
        "unit": "200 g",
        "emoji": "🧀"
    },
    {
        "name": "Horlicks",
        "category": "Dairy & Beverages",
        "price": 220,
        "unit": "500 g",
        "emoji": "🥤"
    },
    {
        "name": "Boost",
        "category": "Dairy & Beverages",
        "price": 230,
        "unit": "500 g",
        "emoji": "🥤"
    },
    {
        "name": "Health Drink",
        "category": "Dairy & Beverages",
        "price": 220,
        "unit": "500 g",
        "emoji": "🥤"
    },
    {
        "name": "Soft Drink",
        "category": "Dairy & Beverages",
        "price": 60,
        "unit": "1.25 litre",
        "emoji": "🥤"
    },

    # ---------------- CLEANING ----------------
    {
        "name": "Surf Excel",
        "category": "Cleaning",
        "price": 130,
        "unit": "1 kg",
        "emoji": "🧺"
    },
    {
        "name": "Rin",
        "category": "Cleaning",
        "price": 100,
        "unit": "1 kg",
        "emoji": "🧼"
    },
    {
        "name": "Vim Dishwash",
        "category": "Cleaning",
        "price": 80,
        "unit": "500 ml",
        "emoji": "🧽"
    },
    {
        "name": "Harpic",
        "category": "Cleaning",
        "price": 110,
        "unit": "500 ml",
        "emoji": "🧴"
    },
    {
        "name": "Floor Cleaner",
        "category": "Cleaning",
        "price": 120,
        "unit": "1 litre",
        "emoji": "🧹"
    },
    {
        "name": "Toilet Cleaner",
        "category": "Cleaning",
        "price": 100,
        "unit": "500 ml",
        "emoji": "🧴"
    },
    {
        "name": "Dishwash Bar",
        "category": "Cleaning",
        "price": 25,
        "unit": "1 pc",
        "emoji": "🧼"
    },
    {
        "name": "Scrub Pad",
        "category": "Cleaning",
        "price": 30,
        "unit": "1 pack",
        "emoji": "🧽"
    },
    {
        "name": "Garbage Bags",
        "category": "Cleaning",
        "price": 60,
        "unit": "1 pack",
        "emoji": "🗑️"
    },
    {
        "name": "Mosquito Coil",
        "category": "Cleaning",
        "price": 45,
        "unit": "1 pack",
        "emoji": "🦟"
    },

    # ---------------- PERSONAL CARE ----------------
    {
        "name": "Colgate",
        "category": "Personal Care",
        "price": 65,
        "unit": "100 g",
        "emoji": "🪥"
    },
    {
        "name": "Toothbrush",
        "category": "Personal Care",
        "price": 40,
        "unit": "1 pc",
        "emoji": "🪥"
    },
    {
        "name": "Lux Soap",
        "category": "Personal Care",
        "price": 40,
        "unit": "1 pc",
        "emoji": "🧼"
    },
    {
        "name": "Lifebuoy Soap",
        "category": "Personal Care",
        "price": 35,
        "unit": "1 pc",
        "emoji": "🧼"
    },
    {
        "name": "Dettol",
        "category": "Personal Care",
        "price": 55,
        "unit": "100 ml",
        "emoji": "🧴"
    },
    {
        "name": "Shampoo",
        "category": "Personal Care",
        "price": 120,
        "unit": "180 ml",
        "emoji": "🧴"
    },
    {
        "name": "Hair Oil",
        "category": "Personal Care",
        "price": 80,
        "unit": "100 ml",
        "emoji": "🧴"
    },
    {
        "name": "Face Wash",
        "category": "Personal Care",
        "price": 140,
        "unit": "100 ml",
        "emoji": "🧴"
    },
    {
        "name": "Hand Wash",
        "category": "Personal Care",
        "price": 90,
        "unit": "250 ml",
        "emoji": "🧴"
    },
    {
        "name": "Body Lotion",
        "category": "Personal Care",
        "price": 150,
        "unit": "200 ml",
        "emoji": "🧴"
    },

    # ---------------- STATIONERY ----------------
    {
        "name": "Pencil",
        "category": "Stationery",
        "price": 10,
        "unit": "1 pc",
        "emoji": "✏️"
    },
    {
        "name": "Blue Pen",
        "category": "Stationery",
        "price": 10,
        "unit": "1 pc",
        "emoji": "🖊️"
    },
    {
        "name": "Black Pen",
        "category": "Stationery",
        "price": 10,
        "unit": "1 pc",
        "emoji": "🖊️"
    },
    {
        "name": "Red Pen",
        "category": "Stationery",
        "price": 10,
        "unit": "1 pc",
        "emoji": "🖊️"
    },
    {
        "name": "Notebook",
        "category": "Stationery",
        "price": 40,
        "unit": "1 book",
        "emoji": "📓"
    },
    {
        "name": "Long Notebook",
        "category": "Stationery",
        "price": 60,
        "unit": "1 book",
        "emoji": "📒"
    },
    {
        "name": "Record Note",
        "category": "Stationery",
        "price": 80,
        "unit": "1 book",
        "emoji": "📔"
    },
    {
        "name": "Geometry Box",
        "category": "Stationery",
        "price": 120,
        "unit": "1 box",
        "emoji": "📐"
    },
    {
        "name": "Scale 30 cm",
        "category": "Stationery",
        "price": 15,
        "unit": "1 pc",
        "emoji": "📏"
    },
    {
        "name": "Scissors",
        "category": "Stationery",
        "price": 30,
        "unit": "1 pc",
        "emoji": "✂️"
    },
    {
        "name": "Eraser",
        "category": "Stationery",
        "price": 5,
        "unit": "1 pc",
        "emoji": "◻️"
    },
    {
        "name": "Sharpener",
        "category": "Stationery",
        "price": 5,
        "unit": "1 pc",
        "emoji": "🔪"
    },
    {
        "name": "Colour Pencils",
        "category": "Stationery",
        "price": 60,
        "unit": "12 colours",
        "emoji": "🖍️"
    },
    {
        "name": "Sketch Pens",
        "category": "Stationery",
        "price": 50,
        "unit": "12 colours",
        "emoji": "🖌️"
    },
    {
        "name": "Crayons",
        "category": "Stationery",
        "price": 50,
        "unit": "12 colours",
        "emoji": "🖍️"
    },
    {
        "name": "Water Colours",
        "category": "Stationery",
        "price": 60,
        "unit": "1 set",
        "emoji": "🎨"
    },
    {
        "name": "Glue Stick",
        "category": "Stationery",
        "price": 20,
        "unit": "1 pc",
        "emoji": "🧴"
    },
    {
        "name": "Fevicol",
        "category": "Stationery",
        "price": 30,
        "unit": "50 g",
        "emoji": "🧴"
    },
    {
        "name": "A4 Paper",
        "category": "Stationery",
        "price": 80,
        "unit": "100 sheets",
        "emoji": "📄"
    },
    {
        "name": "File Folder",
        "category": "Stationery",
        "price": 30,
        "unit": "1 pc",
        "emoji": "📁"
    },
    {
        "name": "Document File",
        "category": "Stationery",
        "price": 40,
        "unit": "1 pc",
        "emoji": "📂"
    },
    {
        "name": "Sticky Notes",
        "category": "Stationery",
        "price": 30,
        "unit": "1 pad",
        "emoji": "🗒️"
    },
    {
        "name": "Paper Clips",
        "category": "Stationery",
        "price": 20,
        "unit": "1 box",
        "emoji": "📎"
    },
    {
        "name": "Binder Clips",
        "category": "Stationery",
        "price": 30,
        "unit": "1 box",
        "emoji": "📎"
    },
    {
        "name": "Exam Pad / Writing Pad",
        "category": "Stationery",
        "price": 40,
        "unit": "1 pad",
        "emoji": "📝"
    },
    {
        "name": "Whiteboard Marker",
        "category": "Stationery",
        "price": 25,
        "unit": "1 pc",
        "emoji": "🖊️"
    },
    {
        "name": "Highlighter",
        "category": "Stationery",
        "price": 25,
        "unit": "1 pc",
        "emoji": "🖍️"
    },
    {
        "name": "Gel Pen",
        "category": "Stationery",
        "price": 15,
        "unit": "1 pc",
        "emoji": "🖊️"
    },
    {
        "name": "Ball Pen Pack",
        "category": "Stationery",
        "price": 50,
        "unit": "5 pcs",
        "emoji": "🖊️"
    },
    {
        "name": "Pencil Box",
        "category": "Stationery",
        "price": 80,
        "unit": "1 pc",
        "emoji": "📦"
    },
    {
        "name": "Pencil Pouch",
        "category": "Stationery",
        "price": 100,
        "unit": "1 pc",
        "emoji": "👝"
    },
    {
        "name": "Drawing Book",
        "category": "Stationery",
        "price": 50,
        "unit": "1 book",
        "emoji": "🎨"
    },
    {
        "name": "Colouring Book",
        "category": "Stationery",
        "price": 60,
        "unit": "1 book",
        "emoji": "🎨"
    },
    {
        "name": "Chart Paper",
        "category": "Stationery",
        "price": 10,
        "unit": "1 sheet",
        "emoji": "📄"
    },
    {
        "name": "Craft Paper",
        "category": "Stationery",
        "price": 50,
        "unit": "1 pack",
        "emoji": "📄"
    },
    {
        "name": "Tape",
        "category": "Stationery",
        "price": 20,
        "unit": "1 roll",
        "emoji": "📏"
    },
    {
        "name": "Double-Sided Tape",
        "category": "Stationery",
        "price": 40,
        "unit": "1 roll",
        "emoji": "📏"
    },
    {
        "name": "Stapler",
        "category": "Stationery",
        "price": 60,
        "unit": "1 pc",
        "emoji": "📎"
    },
    {
        "name": "Stapler Pins",
        "category": "Stationery",
        "price": 20,
        "unit": "1 box",
        "emoji": "📌"
    },
    {
        "name": "Calculator",
        "category": "Stationery",
        "price": 150,
        "unit": "1 pc",
        "emoji": "🧮"
    },
    {
        "name": "Clipboard",
        "category": "Stationery",
        "price": 50,
        "unit": "1 pc",
        "emoji": "📋"
    },
    {
        "name": "Notebook Set",
        "category": "Stationery",
        "price": 100,
        "unit": "3 books",
        "emoji": "📚"
    },
    {
        "name": "Spiral Notebook",
        "category": "Stationery",
        "price": 70,
        "unit": "1 book",
        "emoji": "📓"
    },
    {
        "name": "Project File",
        "category": "Stationery",
        "price": 40,
        "unit": "1 pc",
        "emoji": "📁"
    },
    {
        "name": "Brown Cover",
        "category": "Stationery",
        "price": 30,
        "unit": "1 pack",
        "emoji": "📄"
    },
    {
        "name": "Label Stickers",
        "category": "Stationery",
        "price": 20,
        "unit": "1 sheet",
        "emoji": "🏷️"
    },
]

# =========================================================
# SESSION STATE
# =========================================================
if "cart" not in st.session_state:
    st.session_state.cart = {}

# =========================================================
# FUNCTIONS
# =========================================================
def add_to_cart(product_name):
    st.session_state.cart[product_name] = (
        st.session_state.cart.get(product_name, 0) + 1
    )


def remove_from_cart(product_name):
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name] -= 1

        if st.session_state.cart[product_name] <= 0:
            del st.session_state.cart[product_name]


def get_product(product_name):
    for product in PRODUCTS:
        if product["name"] == product_name:
            return product
    return None


def cart_total():
    total = 0

    for name, quantity in st.session_state.cart.items():
        product = get_product(name)

        if product:
            total += product["price"] * quantity

    return total


def cart_count():
    return sum(st.session_state.cart.values())


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.title("🛒 BALAJI MALIGAI")

    st.write("Fresh groceries & stationery")

    page = st.radio(
        "Menu",
        [
            "🏠 Home",
            "🛍️ Shop",
            "🛒 Cart",
            "📦 Checkout",
            "📞 Contact"
        ]
    )

    st.divider()

    st.metric(
        "Cart Items",
        cart_count()
    )

    st.write("📞", PHONE)
    st.write("💳", UPI_ID)


# =========================================================
# HOME
# =========================================================
if page == "🏠 Home":

    st.title("🛒 BALAJI MALIGAI")

    st.subheader(
        "Your Local Grocery & Stationery Store"
    )

    st.write(
        "Quality groceries, household essentials, "
        "personal care products and stationery items "
        "available at affordable prices."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Products",
            len(PRODUCTS)
        )

    with col2:
        st.metric(
            "Categories",
            len(set(p["category"] for p in PRODUCTS))
        )

    with col3:
        st.metric(
            "Cart Items",
            cart_count()
        )

    with col4:
        st.metric(
            "UPI Payment",
            "Available"
        )

    st.divider()

    st.subheader("✨ Shop Categories")

    categories = sorted(
        set(p["category"] for p in PRODUCTS)
    )

    category_columns = st.columns(4)

    for index, category in enumerate(categories):

        with category_columns[index % 4]:

            count = sum(
                1
                for product in PRODUCTS
                if product["category"] == category
            )

            st.info(
                f"### {category}\n\n"
                f"{count} products"
            )

    st.divider()

    st.subheader("📍 Store Location")

    st.write(ADDRESS)

    st.link_button(
        "🗺️ Open Google Maps",
        MAP_URL
    )


# =========================================================
# SHOP
# =========================================================
elif page == "🛍️ Shop":

    st.title("🛍️ Shop Products")

    search = st.text_input(
        "🔎 Search products",
        placeholder="Search rice, pen, soap..."
    )

    categories = ["All Categories"] + sorted(
        set(p["category"] for p in PRODUCTS)
    )

    selected_category = st.selectbox(
        "📂 Category",
        categories
    )

    filtered_products = PRODUCTS.copy()

    if selected_category != "All Categories":
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == selected_category
        ]

    if search.strip():

        search_text = search.strip().lower()

        filtered_products = [
            product
            for product in filtered_products
            if search_text in product["name"].lower()
        ]

    st.write(
        f"Showing {len(filtered_products)} products"
    )

    st.divider()

    for start in range(0, len(filtered_products), 4):

        row_products = filtered_products[start:start + 4]

        columns = st.columns(4)

        for column, product in zip(columns, row_products):

            with column:

                st.info(
                    f"{product['emoji']}  **{product['category']}**"
                )

                st.subheader(
                    product["name"]
                )

                st.caption(
                    product["unit"]
                )

                st.success(
                    f"₹{product['price']}"
                )

                current_quantity = st.session_state.cart.get(
                    product["name"],
                    0
                )

                st.write(
                    f"Cart: {current_quantity}"
                )

                add_col, qty_col, remove_col = st.columns(3)

                with add_col:
                    if st.button(
                        "➕",
                        key=f"add_{product['name']}"
                    ):
                        add_to_cart(product["name"])
                        st.rerun()

                with qty_col:
                    st.write(
                        str(current_quantity)
                    )

                with remove_col:
                    if st.button(
                        "➖",
                        key=f"remove_{product['name']}"
                    ):
                        remove_from_cart(product["name"])
                        st.rerun()

                st.divider()


# =========================================================
# CART
# =========================================================
elif page == "🛒 Cart":

    st.title("🛒 Your Cart")

    if not st.session_state.cart:

        st.info(
            "Your cart is empty. Go to Shop and add products."
        )

    else:

        for name, quantity in list(
            st.session_state.cart.items()
        ):

            product = get_product(name)

            if not product:
                continue

            item_total = product["price"] * quantity

            col1, col2, col3, col4, col5 = st.columns(
                [3, 1, 1, 1, 1]
            )

            with col1:
                st.write(
                    f"{product['emoji']} **{name}**"
                )

            with col2:
                st.write(
                    product["unit"]
                )

            with col3:
                st.write(
                    f"₹{product['price']}"
                )

            with col4:
                st.write(
                    f"Qty: {quantity}"
                )

            with col5:
                st.write(
                    f"₹{item_total}"
                )

        st.divider()

        st.subheader(
            f"Total: ₹{cart_total()}"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "🗑️ Clear Cart",
                use_container_width=True
            ):
                st.session_state.cart = {}
                st.rerun()

        with col2:
            st.write(
                "Go to Checkout from the sidebar."
            )


# =========================================================
# CHECKOUT
# =========================================================
elif page == "📦 Checkout":

    st.title("📦 Checkout")

    if not st.session_state.cart:

        st.warning(
            "Your cart is empty."
        )

    else:

        st.subheader("🛒 Order Summary")

        for name, quantity in st.session_state.cart.items():

            product = get_product(name)

            if product:

                total = product["price"] * quantity

                st.write(
                    f"{product['emoji']} "
                    f"{name} × {quantity} = ₹{total}"
                )

        st.divider()

        st.subheader(
            f"💰 Total Amount: ₹{cart_total()}"
        )

        st.divider()

        st.subheader("👤 Customer Details")

        customer_name = st.text_input(
            "Customer Name"
        )

        customer_phone = st.text_input(
            "Phone Number"
        )

        delivery_address = st.text_area(
            "Delivery Address"
        )

        order_notes = st.text_area(
            "Order Notes",
            placeholder="Any special instructions?"
        )

        payment_method = st.radio(
            "💳 Payment Method",
            [
                "Cash on Delivery",
                "UPI Payment"
            ]
        )

        if payment_method == "UPI Payment":

            st.info(
                f"UPI ID: {UPI_ID}"
            )

            st.write(
                "Open your UPI app and pay using the above UPI ID."
            )

            qr_files = [
                "payment_qr.png",
                "payment_qr.jpg",
                "phonepe_qr.png",
                "phonepe_qr.jpg"
            ]

            qr_found = False

            for qr_file in qr_files:

                qr_path = Path(qr_file)

                if qr_path.exists():

                    st.image(
                        str(qr_path),
                        caption="Scan to Pay",
                        width=250
                    )

                    qr_found = True
                    break

            if not qr_found:

                st.warning(
                    "QR image not found. "
                    "Add payment_qr.png inside the same folder as app.py."
                )

        st.divider()

        if st.button(
            "📲 Place Order on WhatsApp",
            use_container_width=True
        ):

            if not customer_name:
                st.error(
                    "Please enter your name."
                )

            elif not customer_phone:
                st.error(
                    "Please enter your phone number."
                )

            elif not delivery_address:
                st.error(
                    "Please enter delivery address."
                )

            else:

                lines = [
                    "🛒 BALAJI MALIGAI ORDER",
                    "",
                    f"Customer: {customer_name}",
                    f"Phone: {customer_phone}",
                    f"Address: {delivery_address}",
                    "",
                    "ORDER ITEMS:"
                ]

                for name, quantity in st.session_state.cart.items():

                    product = get_product(name)

                    if product:

                        item_total = (
                            product["price"] * quantity
                        )

                        lines.append(
                            f"{name} × {quantity} = ₹{item_total}"
                        )

                lines.extend(
                    [
                        "",
                        f"TOTAL: ₹{cart_total()}",
                        f"Payment: {payment_method}",
                        f"Notes: {order_notes}"
                    ]
                )

                message = quote(
                    "\n".join(lines)
                )

                whatsapp_url = (
                    f"https://wa.me/{WHATSAPP}"
                    f"?text={message}"
                )

                st.success(
                    "Order details are ready."
                )

                st.link_button(
                    "💬 Open WhatsApp & Send Order",
                    whatsapp_url
                )


# =========================================================
# CONTACT
# =========================================================
elif page == "📞 Contact":

    st.title("📞 Contact BALAJI MALIGAI")

    st.subheader(
        "We are happy to help you!"
    )

    st.write(
        f"📞 **Phone:** {PHONE}"
    )

    st.write(
        f"💬 **WhatsApp:** {PHONE}"
    )

    st.write(
        f"💳 **UPI ID:** {UPI_ID}"
    )

    st.write(
        f"📍 **Address:** {ADDRESS}"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "💬 WhatsApp",
            f"https://wa.me/{WHATSAPP}"
        )

    with col2:

        st.link_button(
            "🗺️ Google Maps",
            MAP_URL
        )

    st.divider()

    st.subheader("🏪 BALAJI MALIGAI")

    st.write(
        "Groceries • Household Essentials • "
        "Personal Care • Stationery"
    )

    st.write(
        "Thank you for shopping with us ❤️"
    )
