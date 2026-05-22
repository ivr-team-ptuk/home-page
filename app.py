import streamlit as st
import streamlit.components.v1 as components

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="IVR Tools",
    page_icon="Black_Square-01.svg",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

with open("style.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# NAVBAR
# =========================

import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="IVR PDF Tools",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

def load_css():

    with open("style.css", "r", encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# =========================
# NAVBAR
# =========================

st.markdown("""

<div class="ivr-navbar">

    <div class="nav-logo">
        IVR PDF Tools
    </div>

    <div class="nav-links">

        <a href="ivr-watermark-tool.streamlit.app">
            تعليم الملفات
        </a>

        <a href="ivr-merge-tool.streamlit.app">
            دمج الملفات
        </a>

        <a href="ivr-imagetopdf-tool.streamlit.app">
            الصور إلى PDF
        </a>

    </div>

</div>

""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

components.html("""

<div class="hero">

    <h1>
        أدوات PDF خاصة بأعضاء اللجنة العلمية
    </h1>

    <p>
        منصة لمعالجة ملفات PDF بسهولة
    </p>

</div>

""", unsafe_allow_html=True)

# =========================
# TOOL CARDS
# =========================

col1, col2, col3 = st.columns(3)

# =========================
# WATERMARK
# =========================

with col1:

    st.markdown("""

    <div class="tool-card">

        <div class="tool-icon">
            🖊️
        </div>

        <h3>
            تعليم الملفات
        </h3>

        <p>
            إضافة علامات مائية احترافية
            على ملفات PDF
        </p>

        <a class="tool-btn"
        href="https://ivr-watermark-tool.streamlit.app">

            فتح الأداة

        </a>

    </div>

    """, unsafe_allow_html=True)

# =========================
# MERGE
# =========================

with col2:

    st.markdown("""

    <div class="tool-card">

        <div class="tool-icon">
            📚
        </div>

        <h3>
            دمج الملفات
        </h3>

        <p>
            دمج عدة ملفات PDF
            داخل ملف واحد
        </p>

        <a class="tool-btn"
        href="https://ivr-merge-tool.streamlit.app">

            فتح الأداة

        </a>

    </div>

    """, unsafe_allow_html=True)

# =========================
# IMAGES
# =========================

with col3:

    st.markdown("""

    <div class="tool-card">

        <div class="tool-icon">
            🖼️
        </div>

        <h3>
            الصور إلى PDF
        </h3>

        <p>
            تحويل الصور إلى ملفات PDF
            بجودة عالية
        </p>

        <a class="tool-btn"
        href="https://ivr-imagetopdf-tool.streamlit.app">

            فتح الأداة

        </a>

    </div>

    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""

<div class="footer">

    IVR Engineering Society © 2026

</div>

""", height=90)