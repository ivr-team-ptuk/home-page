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
# HIDE STREAMLIT DEFAULT UI
# =========================

st.markdown("""
<style>

#MainMenu,
header,
footer{
    visibility:hidden;
}

.block-container{
    padding:0;
}

iframe{
    border:none !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD CSS FILE
# =========================

with open("style.css", encoding="utf-8") as f:
    css = f.read()

# =========================
# HTML CONTENT
# =========================

html_content = f"""

<style>
{css}
</style>

<script>

function toggleNavbar() {{

    const navbar =
        document.getElementById("navbarWrapper");

    navbar.classList.toggle("collapsed");
}}

</script>

<div class="page-wrapper">

    <!-- NAVBAR -->

    <div class="ivr-navbar-wrapper" id="navbarWrapper">


            <!-- TOGGLE BUTTON -->

            <button class="nav-toggle" onclick="toggleNavbar()">
                ☰
            </button>

        <div class="ivr-navbar">

            <div class="nav-logo">
                IVR PDF Tools
            </div>

            <div class="nav-links">


                <a href="https://ivr-watermark-tool.streamlit.app" target="_self">
                    تعليم الملفات
                </a>

                <a href="https://ivr-merge-tool.streamlit.app" target="_self">
                    دمج الملفات
                </a>

                <a href="https://ivr-imagetopdf-tool.streamlit.app" target="_self">
                    الصور إلى PDF
                </a>

                <a href="" target="_self"></a>

            </div>

        </div>

    </div>

    <!-- HERO -->

    <div class="hero">

        <h1>
            أدوات PDF خاصة بأعضاء اللجنة العلمية
        </h1>

        <p>
            منصة لمعالجة ملفات PDF بسهولة
        </p>

    </div>

    <!-- TOOLS -->

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
            target="_self">

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
            target="_self">

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
            target="_self">

                فتح الأداة

            </a>

        </div>

    </div>

    <!-- FOOTER -->

    <div class="footer">
        IVR Engineering Society © 2026
    </div>

</div>

<script>

function toggleNavbar() {{

    const navbar =
        document.getElementById("navbarWrapper");

    navbar.classList.toggle("collapsed");
}}

</script>

"""

# =========================
# RENDER HTML
# =========================

components.html( html_content, height=950, scrolling=True )

