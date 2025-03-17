import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# Configure Google API Key securely
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("⚠ Google API Key is missing. Set it as an environment variable.")
    st.stop()
genai.configure(api_key=api_key)

# Function to call Google Gemini models with error handling
def get_gemini_response(query, model_name):
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(query)
        return response.text if hasattr(response, "text") else "⚠ No valid response received."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Initialize model scores
if "model_scores" not in st.session_state:
    st.session_state.model_scores = {"Gemini 1.5 Pro": 1, "Gemini 2.0-pro-exp": 1, "Gemini 1.5-flash-latest": 1}

# Function to determine model order based on scores
def get_model_order():
    return sorted(st.session_state.model_scores, key=st.session_state.model_scores.get, reverse=True)

# Streamlit UI
st.set_page_config(page_title="AI Article Generator")
st.header("📝 AI Article Generator (Compare Responses)")

query = st.text_area("Enter your article topic:")

# Ensure a valid input
if query and st.button("Generate"):
    query = query.strip()
    if not query:
        st.warning("⚠ Please enter an article topic before generating.")
        st.stop()

    model_order = get_model_order()

    responses = {
        "Gemini 1.5 Pro": get_gemini_response(query, "gemini-1.5-pro"),
        "Gemini 2.0-pro-exp": get_gemini_response(query, "gemini-2.0-pro-exp"),
        "Gemini 1.5-flash-latest": get_gemini_response(query, "gemini-1.5-flash-latest"),
    }

    # Store responses in session state
    st.session_state.ordered_responses = {model: responses[model] for model in model_order}
    st.session_state.selected_model = None  # Reset selection for new query

# Display responses if available
if "ordered_responses" in st.session_state and not st.session_state.get("selected_model"):
    for model, response in st.session_state.ordered_responses.items():
        if st.button(f"Select {model} Response", key=f"select_{model}"):
            st.session_state.selected_model = model
            st.session_state.model_scores[model] += 1  # Increase model preference score
            st.rerun()  # Ensures UI updates correctly

# Show only the selected response
if st.session_state.get("selected_model"):
    selected_model = st.session_state.selected_model
    st.subheader(f"✅ Selected Model: {selected_model}")
    st.write(st.session_state.ordered_responses.get(selected_model, "⚠ No response available."))
