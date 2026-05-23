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

    <!-- HERO -->
    <section class="hero">

        <img
            src="https://raw.githubusercontent.com/ivr-team-ptuk/home-page/main/Black_Square-01.svg"
            class="hero-logo"
            alt="IVR Logo"
        >

        <h1>أدوات PDF خاصة بأعضاء اللجنة العلمية</h1>
        <p>منصة لمعالجة ملفات PDF بسهولة</p>

    </section>

    <!-- TOOLS -->
    <div class="tools-grid">

        <div class="tool-card">
            <div class="tool-icon">🖊️</div>
            <h3>تعليم الملفات</h3>
            <p>إضافة علامات مائية احترافية على ملفات PDF</p>
            <a class="tool-btn" href="https://ivr-watermark-tool.streamlit.app">فتح الأداة</a>
        </div>

        <div class="tool-card">
            <div class="tool-icon">📚</div>
            <h3>دمج الملفات</h3>
            <p>دمج عدة ملفات PDF داخل ملف واحد</p>
            <a class="tool-btn" href="https://ivr-merge-tool.streamlit.app">فتح الأداة</a>
        </div>

        <div class="tool-card">
            <div class="tool-icon">🖼️</div>
            <h3>الصور إلى PDF</h3>
            <p>تحويل الصور إلى ملفات PDF بجودة عالية</p>
            <a class="tool-btn" href="https://ivr-imagetopdf-tool.streamlit.app">فتح الأداة</a>
        </div>

    </div>

    <!-- FOOTER -->
    <footer class="footer">
        IVR Engineering Society &copy; 2026
    </footer>

</div>

<script>
    function toggleNavbar() {{
        const wrapper  = document.getElementById("navbarWrapper");
        const btn      = wrapper.querySelector(".nav-toggle");
        const collapsed = wrapper.classList.toggle("collapsed");
        btn.setAttribute("aria-expanded", collapsed ? "false" : "true");
    }}
</script>
"""

# =========================
# RENDER HTML
# =========================

components.html(html_content, height=1050, scrolling=True)
