# File: core_logic.py

import streamlit as st
import google.generativeai as genai

def configure_api():
    """Configures the Gemini API using Streamlit secrets (for secure key management)."""
    genai.configure(api_key=st.secrets["AIzaSyCCPb5zuTlPnONSe4gDj-5a4nnBoLIqvto"])

def get_master_prompt(business_name, business_type, tone, special_offer, contact_info, review_text):
    """Crafts the detailed, high-quality prompt for GPT model to generate reply."""
    prompt = f"""
    You are a highly skilled customer service manager for '{business_name}', a beloved {business_type} in Hyderabad.
    Your tone must be consistently {tone}.
    Your main goal is to make every customer feel heard and valued, encouraging them to return.

    **Instructions:**
    1.  Acknowledge the specific key points (positive or negative) from the customer's review. Be specific.
    2.  If the review is positive, express genuine gratitude. Subtly include the special offer: '{special_offer}'.
    3.  If the review is negative, be empathetic and apologize for their specific poor experience. Do not make excuses.
        Invite them to connect offline by contacting us at {contact_info}.
    4.  Keep the response concise, personal, professional — 2 to 4 sentences only.
    5.  Do NOT invent facts or make promises the business can't keep.

    **Customer Review:**
    ---
    {review_text}
    ---

    **Your Response:**
    """
    return prompt

def generate_response(business_name, business_type, tone, special_offer, contact_info, review_text):
    """Calls Gemini LLM and returns the generated reply text."""
    try:
        model = genai.GenerativeModel('models/gemini-2.5-pro')
        prompt = get_master_prompt(business_name, business_type, tone, special_offer, contact_info, review_text)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"API Error: {e}")
        return "Error: Unable to generate response. Please check your API key and internet connection."


