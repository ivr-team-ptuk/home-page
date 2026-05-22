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
    <a href="https://ivr-home.streamlit.app" target="_blank">Home</a>
    <a href="https://ivr-merge-tool.streamlit.app" target="_blank">Merge PDF</a>
    <a href="https://ivr-watermark-tool.streamlit.app" target="_blank">Watermark PDF</a>
    <a href="https://ivr-imagetopdf-tool.streamlit.app" target="_blank">Image to PDF</a>
</div>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

st.markdown("""

<div class="hero">

    <h1>
        أدوات PDF احترافية
    </h1>

    <p>
        منصة متكاملة لمعالجة ملفات PDF بسهولة وسرعة
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

    IVR Scientific © 2026

</div>

""", unsafe_allow_html=True)