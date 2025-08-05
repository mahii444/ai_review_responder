# File: app.py

import streamlit as st
from core_logic import generate_response, configure_api

# Page settings
st.set_page_config(page_title="AI Review Responder", page_icon="✍️", layout="centered")

# Configure Gemini API securely
try:
    configure_api()
except Exception:
    st.error("🚨 Gemini API Key not found in Streamlit secrets. Please add it before proceeding.")
    st.stop()

# UI title and description
st.title("✍️ AI Review Responder for Local Businesses")
st.markdown("Generate professional, personalized replies to your customer reviews—instantly.")

# Sidebar for business profile
with st.sidebar:
    st.header("Your Business Information")
    st.markdown("Fill this once; it will customize all replies.")
    business_name = st.text_input("Business Name", "e.g., Paradise Biryani")
    business_type = st.text_input("Business Type", "e.g., a famous Hyderabadi restaurant")
    special_offer = st.text_area("Current Special or Offer", "e.g., Tuesday Biryani Bonanza")
    contact_info = st.text_input("Customer Contact for Issues", "e.g., manager@paradise.com")
    tone = st.selectbox("Reply Tone", ("Friendly", "Professional", "Warm", "Formal"), index=0)

# Main input for customer review
st.subheader("Paste Customer Review Below")
review_text = st.text_area("Customer Review", height=150)

# Generate reply button and output
if st.button("Generate Reply", type="primary"):
    if not all([business_name, business_type, review_text]):
        st.warning("Please fill in your Business Name, Type, and paste the Review text.")
    else:
        with st.spinner("🧠 AI is crafting your reply..."):
            reply = generate_response(business_name, business_type, tone, special_offer, contact_info, review_text)
        st.subheader("✅ Suggested Reply")
        st.markdown(f"> {reply}")

# Footer
st.markdown("---")
st.markdown("Built by a solo founder with Python & AI.")
