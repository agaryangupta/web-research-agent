import streamlit as st

# 🎨 Page Config
st.set_page_config(
    page_title="Web Research Agent",
    page_icon="🌐",
    layout="centered"
)

# 🎨 Custom CSS
st.markdown("""
    <style>
        .main {
            max-width: 800px;
            margin: auto;
        }
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: gray;
            margin-bottom: 30px;
        }
        .stTextInput > div > div > input {
            border-radius: 10px;
            padding: 12px;
            font-size: 16px;
        }
        .stButton button {
            width: 100%;
            border-radius: 10px;
            padding: 12px;
            font-size: 16px;
            font-weight: 600;
        }
        .card {
            padding: 20px;
            border-radius: 12px;
            background-color: #f8f9fa;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 🌐 Header
st.markdown('<div class="title">🌐 Web Research Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered quick research using Gemini + Wikipedia</div>', unsafe_allow_html=True)

# 🔍 Input
query = st.text_input("🔎 Enter a topic to research")

# 🚀 Button
if st.button("🚀 Start Research"):
    if query:
        with st.spinner("Fetching and analyzing data... ⏳"):

            full_text = get_wikipedia_content(query)

            if not full_text:
                st.error("⚠️ No data found. Try a different topic.")
            else:
                summary = summarize(full_text)

                # 📌 Summary Card
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("📌 Summary")
                st.write(summary)
                st.markdown('</div>', unsafe_allow_html=True)

                # 🔗 Source Card
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("🔗 Source")
                st.markdown(
                    f"[Open Wikipedia Article](https://en.wikipedia.org/wiki/{query.replace(' ', '_')})"
                )
                st.markdown('</div>', unsafe_allow_html=True)