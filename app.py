import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="IVR Merge Tool",
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

st.markdown("""
<div class="ivr-navbar">
    <a href="https://ivr-home-page.streamlit.app" target="_blank">Home</a>
    <a href="https://ivr-merge-tool.streamlit.app" target="_blank">Merge PDF</a>
    <a href="https://ivr-watermark-tool.streamlit.app" target="_blank">Watermark PDF</a>
    <a href="https://ivr-imagetopdf-tool.streamlit.app" target="_blank">Image to PDF</a>
</div>
""", unsafe_allow_html=True)

# =========================
# TOOLS
# =========================

st.markdown(
    """
    <div class="hero">
        <h1>أدوات اللجنة العلمية - IVR</h1>
        <p>
            أدوات للتعامل مع ملفات PDF والصور
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

col1, col2, col3 = st.columns(3)

# =========================
# MERGE
# =========================

with col1:

    st.markdown(
        """
        <div class="tool-card">
            <div class="tool-icon">📄</div>
            <h3>دمج PDF</h3>
            <p>
                دمج ملفات PDF
                وترتيبها وإضافة
                علامات مرجعية
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "الذهاب لدمج الملفات",
        "https://ivr-merge-tool.streamlit.app",
        use_container_width=True
    )

# =========================
# WATERMARK
# =========================

with col2:

    st.markdown(
        """
        <div class="tool-card">
            <div class="tool-icon">🖋️</div>
            <h3>تعليم PDF</h3>
            <p>
                إضافة علامات مائية على ملفات PDF
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "الذهاب لتعليم الملفات",
        "https://ivr-watermark-tool.streamlit.app",
        use_container_width=True
    )

# =========================
# IMAGE TO PDF
# =========================

with col3:

    st.markdown(
        """
        <div class="tool-card">
            <div class="tool-icon">🖼️</div>
            <h3>صور إلى PDF</h3>
            <p>
                تحويل الصور إلى
                ملف PDF مرتب
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "تحويل الصور إلى ملفات",
        "https://ivr-imagetopdf-tool.streamlit.app",
        use_container_width=True
    )

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

    IVR Engineering Society © 2026

</div>
""", unsafe_allow_html=True)