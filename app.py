import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Anand Ice Cream Menu", page_icon="🍨", layout="centered")

# --- Logo ---
logo_url = "https://drive.google.com/uc?export=view&id=1dPnFK8yHuGPdDGH2S2VdeEqxNwFnUGjK"
st.image(logo_url, width=150)
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Anand Ice Cream Menu</h1>", unsafe_allow_html=True)

# --- Load Data ---
categories_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRQJ5L6O5vVyXrWx7iVf_dfM7dWV-qx02tN7D4VFZGoZq6iPOXj1RVI9JlhV9VEKnDwoqwhQdde2gCB/pub?gid=0&single=true&output=csv"
items_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRQJ5L6O5vVyXrWx7iVf_dfM7dWV-qx02tN7D4VFZGoZq6iPOXj1RVI9JlhV9VEKnDwoqwhQdde2gCB/pub?gid=1538241295&single=true&output=csv"

categories_df = pd.read_csv(categories_url)
items_df = pd.read_csv(items_url)

# --- Micro Animation CSS ---
st.markdown("""
    <style>
    .category-card {
        transition: transform 0.3s ease;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .category-card:hover {
        transform: scale(1.02);
        background-color: #fff8f0;
    }
    .item {
        padding: 5px 0;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Display Categories ---
for _, cat in categories_df.iterrows():
    st.markdown(f"<div class='category-card'>", unsafe_allow_html=True)
    st.image(cat['ImageURL'], width=300)
    st.markdown(f"<h3 style='color:#ff4b4b;'>{cat['Name']}</h3>", unsafe_allow_html=True)

    # Filter items under this category
    items = items_df[items_df['CategoryID'] == cat['ID']]
    for _, item in items.iterrows():
        st.markdown(f"<div class='item'>🍧 <strong>{item['Name']}</strong> — ₹{item['Price']}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
