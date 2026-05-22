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

with open("style.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# NAVBAR
# =========================

st.markdown("""
<div class="ivr-navbar">

    <div class="nav-links">

        <a href="https://home-url.streamlit.app"
        target="_self">
        الرئيسية
        </a>

        <a href="https://merge-url.streamlit.app"
        target="_self">
        دمج PDF
        </a>

        <a href="https://watermark-url.streamlit.app"
        target="_self">
        تعليم الملفات
        </a>

        <a href="https://images-url.streamlit.app"
        target="_self">
        صور إلى PDF
        </a>

    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">

    <h1>
        IVR Scientific Tools
    </h1>

    <p>
        أدوات احترافية للتعامل مع ملفات PDF
        بسرعة وتصميم عصري.
    </p>

</div>
""", unsafe_allow_html=True)

# =========================
# TOOLS
# =========================

col1, col2, col3 = st.columns(3)

# =========================
# MERGE
# =========================

with col1:

    st.markdown("""
    <div class="tool-card">

        <div class="tool-icon">
            📄
        </div>

        <h3>
            دمج ملفات PDF
        </h3>

        <p>
            دمج عدة ملفات PDF
            مع ترتيبها وإضافة
            علامات مرجعية.
        </p>

        <a class="tool-btn"
        href="https://merge-url.streamlit.app"
        target="_self">

            فتح الأداة

        </a>

    </div>
    """, unsafe_allow_html=True)

# =========================
# WATERMARK
# =========================

with col2:

    st.markdown("""
    <div class="tool-card">

        <div class="tool-icon">
            🛡️
        </div>

        <h3>
            تعليم الملفات
        </h3>

        <p>
            إضافة شعارات وعلامات
            مائية على ملفات PDF
            بشكل احترافي.
        </p>

        <a class="tool-btn"
        href="https://watermark-url.streamlit.app"
        target="_self">

            فتح الأداة

        </a>

    </div>
    """, unsafe_allow_html=True)

# =========================
# IMAGES TO PDF
# =========================

with col3:

    st.markdown("""
    <div class="tool-card">

        <div class="tool-icon">
            🖼️
        </div>

        <h3>
            صور إلى PDF
        </h3>

        <p>
            تحويل الصور إلى PDF
            مع ترتيب الصفحات
            وإضافة علامات مرجعية.
        </p>

        <a class="tool-btn"
        href="https://images-url.streamlit.app"
        target="_self">

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