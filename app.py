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

<style>

body{

    margin:0;

    padding:0 20px;

    background:transparent;

    font-family:'Almarai',sans-serif;

    direction:rtl;

    color:white;
}

/* =========================
NAVBAR
========================= */

.ivr-navbar {

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:18px 24px;

    margin-bottom:40px;

    border-radius:20px;

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);

    backdrop-filter:blur(12px);
}

.nav-logo {

    font-size:22px;

    font-weight:800;

    color:white;
}

.nav-links {

    display:flex;

    gap:12px;

    flex-wrap:wrap;
}

.nav-links a {

    text-decoration:none;

    color:white;

    padding:10px 18px;

    border-radius:12px;

    transition:0.2s;
}

.nav-links a:hover {

    background:rgba(255,255,255,0.08);

    color:#FF5B04;
}

/* =========================
HERO
========================= */

.hero {

    text-align:center;

    padding:40px 20px 60px 20px;
}

.hero h1 {

    font-size:54px;

    margin-bottom:18px;
}

.hero p {

    font-size:22px;

    color:rgba(255,255,255,0.75);
}

/* =========================
TOOLS GRID
========================= */

.tools-grid {

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

    gap:24px;
}

/* =========================
CARDS
========================= */

.tool-card {

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:28px;

    padding:32px;

    text-align:center;

    backdrop-filter:blur(14px);

    transition:0.25s;
}

.tool-card:hover {

    transform:translateY(-6px);

    border-color:#FF5B04;
}

.tool-icon {

    font-size:52px;

    margin-bottom:16px;
}

.tool-card h3 {

    margin-bottom:14px;
}

.tool-card p {

    color:rgba(255,255,255,0.75);

    line-height:1.8;

    margin-bottom:24px;
}

.tool-btn {

    display:inline-block;

    padding:12px 24px;

    background:#FF5B04;

    color:white;

    border-radius:14px;

    text-decoration:none;

    font-weight:bold;

    transition:0.2s;
}

.tool-btn:hover {

    background:#e65100;
}

/* =========================
FOOTER
========================= */

.footer {

    text-align:center;

    padding:50px 0 10px 0;

    color:rgba(255,255,255,0.5);
}

/* =========================
MOBILE
========================= */

@media (max-width:900px){

    .ivr-navbar{

        flex-direction:column;

        gap:16px;
    }

    .hero h1{

        font-size:36px;
    }

    .hero p{

        font-size:18px;
    }
}

</style>

""", height=900)