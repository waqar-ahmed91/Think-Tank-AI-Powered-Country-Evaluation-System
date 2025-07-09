import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crew import run_thinktank_pipeline

st.set_page_config(
    page_title="Think Tank — Country Intelligence",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Think Tank — Country Evaluation System")
st.markdown("""
Analyze and synthesize multi-domain insights (economic, political, climate, risk, etc.)
to generate a national strategic report.
""")

# Sidebar Inputs
with st.sidebar:
    st.header("⚙️ Settings")
    country = st.text_input("Enter a country name:", value="Pakistan")

    st.markdown("### 📂 Domains to Include")
    domains = {
        "Economic": st.checkbox("Economic", value=True),
        "Education": st.checkbox("Education", value=True),
        "Political": st.checkbox("Political", value=True),
        "Culture": st.checkbox("Culture", value=True),
        "Technology": st.checkbox("Technology", value=True),
        "Health": st.checkbox("Health", value=True),
        "Environment": st.checkbox("Environment", value=True),
        "Energy": st.checkbox("Energy", value=True),
        "Foreign Policy": st.checkbox("Foreign Policy", value=True),
        "Demographics": st.checkbox("Demographics", value=True),
        "Risk": st.checkbox("Risk", value=True),
    }

    run_btn = st.button("🚀 Run Analysis")

# Main Panel
if run_btn:
    st.info(f"🔍 Generating strategic report for **{country}**...")
    with st.spinner("Running agents and synthesizing insights..."):
        run_thinktank_pipeline(country)

    st.success("✅ Report generated!")

    md_path = f"{country.lower()}_thinktank_report.md"
    pdf_path = f"{country.lower()}_thinktank_report.pdf"

    # Display download buttons
    if os.path.exists(md_path) and os.path.exists(pdf_path):
        with open(md_path, "r", encoding="utf-8") as f:
            st.markdown("### 📄 Markdown Report")
            st.code(f.read(), language='markdown')

        st.download_button("⬇️ Download Markdown", data=open(md_path, "rb"), file_name=md_path)
        st.download_button("⬇️ Download PDF", data=open(pdf_path, "rb"), file_name=pdf_path)
