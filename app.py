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
# HOME PAGE
# =========================

components.html("""

<div class="ivr-navbar">

    <div class="nav-logo">
        IVR PDF Tools
    </div>

    <div class="nav-links">

        <a href="https://ivr-watermark-tool.streamlit.app" target="_top">
            تعليم الملفات
        </a>

        <a href="https://ivr-merge-tool.streamlit.app" target="_top">
            دمج الملفات
        </a>

        <a href="https://ivr-imagetopdf-tool.streamlit.app" target="_top">
            الصور إلى PDF
        </a>

    </div>

</div>

<div class="hero">

    <h1>
        أدوات PDF خاصة بأعضاء اللجنة العلمية
    </h1>

    <p>
        منصة لمعالجة ملفات PDF بسهولة
    </p>

</div>

<div class="tools-grid">

    <!-- WATERMARK -->

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
        href="https://ivr-watermark-tool.streamlit.app"
        target="_top">

            فتح الأداة

        </a>

    </div>

    <!-- MERGE -->

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
        href="https://ivr-merge-tool.streamlit.app"
        target="_top">

            فتح الأداة

        </a>

    </div>

    <!-- IMAGE TO PDF -->

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
        href="https://ivr-imagetopdf-tool.streamlit.app"
        target="_top">

            فتح الأداة

        </a>

    </div>

</div>

<div class="footer">

    IVR Engineering Society © 2026

</div>

""", height=900)