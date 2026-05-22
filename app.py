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
    <a href="https://ivr-home-page.streamlit.app" target="_blank">Home</a>
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

with col1:

    st.markdown("""
    <div class="tool-card">

        <div class="tool-icon">📄</div>

        <h3>دمج ملفات PDF</h3>

        <p>
            دمج عدة ملفات PDF
            مع ترتيبها وإضافة
            علامات مرجعية.
        </p>

        <a class="tool-btn"
        href="https://ivr-merge-tool.streamlit.app"
        target="_blank">

        فتح الأداة

        </a>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="tool-card">

        <div class="tool-icon">🖋️</div>

        <h3>تعليم ملفات PDF</h3>

        <p>
            إضافة علامة مائية
            احترافية على ملفات PDF
            بعدة أوضاع.
        </p>

        <a class="tool-btn"
        href="https://ivr-watermark-tool.streamlit.app"
        target="_blank">

        فتح الأداة

        </a>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="tool-card">

        <div class="tool-icon">🖼️</div>

        <h3>تحويل الصور إلى PDF</h3>

        <p>
            تحويل الصور إلى
            ملف PDF واحد
            مع ترتيب الصفحات.
        </p>

        <a class="tool-btn"
        href="https://ivr-imagetopdf-tool.streamlit.app"
        target="_blank">

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