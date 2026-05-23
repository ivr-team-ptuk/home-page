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
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding: 0; }
iframe { border: none !important; }
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

<div class="page-wrapper">

    <!-- NAVBAR -->
    <nav class="ivr-navbar-wrapper" id="navbarWrapper">

        <button
            class="nav-toggle"
            onclick="toggleNavbar()"
            aria-label="تبديل القائمة"
            aria-expanded="true"
            aria-controls="navbarWrapper"
        >☰</button>

        <div class="ivr-navbar">

            <a href="https://ivr-home-page.streamlit.app" class="nav-logo">
                <img
                    src="https://raw.githubusercontent.com/ivr-team-ptuk/home-page/main/Black_Square-01.svg"
                    class="nav-logo-img"
                    alt="IVR Logo"
                >
            </a>

            <div class="nav-links">
                <a href="https://ivr-watermark-tool.streamlit.app" target="_blank">تعليم الملفات</a>
                <a href="https://ivr-merge-tool.streamlit.app" target="_blank">دمج الملفات</a>
                <a href="https://ivr-imagetopdf-tool.streamlit.app" target="_blank">الصور إلى PDF</a>
            </div>

        </div>

    </nav>

    <!-- HERO -->
    <section class="hero">
        <h1>أدوات PDF خاصة بأعضاء اللجنة العلمية</h1>
        <p>منصة لمعالجة ملفات PDF بسهولة</p>
    </section>

    <!-- TOOLS -->
    <div class="tools-grid">

        <div class="tool-card">
            <div class="tool-icon">🖊️</div>
            <h3>تعليم الملفات</h3>
            <p>إضافة علامات مائية احترافية على ملفات PDF</p>
            <a class="tool-btn" href="https://ivr-watermark-tool.streamlit.app" target="_blank">فتح الأداة</a>
        </div>

        <div class="tool-card">
            <div class="tool-icon">📚</div>
            <h3>دمج الملفات</h3>
            <p>دمج عدة ملفات PDF داخل ملف واحد</p>
            <a class="tool-btn" href="https://ivr-merge-tool.streamlit.app" target="_blank">فتح الأداة</a>
        </div>

        <div class="tool-card">
            <div class="tool-icon">🖼️</div>
            <h3>الصور إلى PDF</h3>
            <p>تحويل الصور إلى ملفات PDF بجودة عالية</p>
            <a class="tool-btn" href="https://ivr-imagetopdf-tool.streamlit.app" target="_blank">فتح الأداة</a>
        </div>

    </div>

    <!-- FOOTER -->
    <footer class="footer">
        IVR Engineering Society &copy; 2026
    </footer>

</div>

<script>
    // =========================
    // NAVBAR TOGGLE
    // =========================

    function toggleNavbar() {{
        const wrapper = document.getElementById("navbarWrapper");
        const btn     = wrapper.querySelector(".nav-toggle");
        const isNowCollapsed = wrapper.classList.toggle("collapsed");

        btn.setAttribute("aria-expanded", isNowCollapsed ? "false" : "true");
    }}

    // =========================
    // AUTO-RESIZE IFRAME
    // (notifies Streamlit of true content height)
    // =========================

    function sendHeight() {{
        const height = document.querySelector(".page-wrapper").scrollHeight;
        window.parent.postMessage(
            {{ type: "streamlit:setFrameHeight", height: height }},
            "*"
        );
    }}

    document.addEventListener("DOMContentLoaded", sendHeight);
    window.addEventListener("resize", sendHeight);
</script>
"""

# =========================
# RENDER HTML
# =========================

components.html(html_content, height=1000, scrolling=True)
