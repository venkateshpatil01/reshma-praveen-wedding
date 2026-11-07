
import streamlit as st
from datetime import date
from pathlib import Path
import base64
import textwrap

# PAGE SETTINGS
st.set_page_config(
    page_title="Reshma weds Praveen",
    page_icon="💍",
    layout="centered"
)

# WEDDING DETAILS
BRIDE = "Reshma"
GROOM = "Praveen"
CITY = "Kalburgi"

HALDI_DATE = date(2026, 12, 12)
WEDDING_DATE = date(2026, 12, 13)

VENUE = "VR Swamy Kalyan Mantapa"
VENUE_ADDRESS = (
    "Ring Rd, Yamlimunuligaon, Taj Sultanpur, "
    "Kalaburagi (Kalburgi), Karnataka 585104"
)

# FIND TIRUPATI IMAGE
BASE_DIR = Path(__file__).resolve().parent

image_candidates = [
    BASE_DIR / "tirupati.png",
    BASE_DIR / "tirupati.png.png",
    BASE_DIR / "Tirupati Temple Deity Icon.png"
]

IMAGE_PATH = next(
    (p for p in image_candidates if p.exists()),
    None
)

tirupati_base64 = ""

if IMAGE_PATH:
    tirupati_base64 = base64.b64encode(
        IMAGE_PATH.read_bytes()
    ).decode("utf-8")


# CSS DESIGN
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Great+Vibes&family=Montserrat:wght@300;400;500&display=swap');

:root {
    --wine: #64172f;
    --deep: #300916;
    --gold: #d4b16d;
    --cream: #fff8ee;
}

.stApp {
    background: radial-gradient(
        circle at top,
        #fffaf3,
        #f0e4d9 72%,
        #ead9ce
    );
    color: #4b2832;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 560px;
    padding: 16px 12px 38px;
}

.invite {
    background: var(--cream);
    border: 1px solid #d8bd88;
    box-shadow: 0 18px 48px #35091824;
    text-align: center;
    overflow: hidden;
}

.cover {
    min-height: 630px;
    padding: 36px 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    position: relative;
    color: var(--cream);

    background:
        radial-gradient(
            ellipse at 50% 18%,
            #eccd8f47,
            transparent 38%
        ),
        linear-gradient(
            160deg,
            #2d071433,
            #280511e0
        ),
        linear-gradient(
            135deg,
            #bd895f,
            #e8c28d 35%,
            #77364a 70%,
            #300916
        );

    animation: reveal 1.3s ease both;
}

.cover:before {
    content: "";
    position: absolute;
    inset: 13px;
    border: 1px solid #e2c280;
    pointer-events: none;
}

.eyebrow {
    font: 9px Montserrat, sans-serif;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #f0dcae;
}

.cover-art {
    width: 90px;
    height: 90px;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.cover-art img {
    width: 90px;
    height: 90px;
    object-fit: contain;
    filter:
        brightness(0.55)
        contrast(1.8)
        drop-shadow(0 3px 6px #0008);
    opacity: 1;
}

.script {
    font: clamp(55px, 13vw, 82px)
        'Great Vibes', cursive;
    color: #f4d99d;
    line-height: 1.02;
    text-shadow: 0 3px 18px #23050f88;
}

.weds {
    font: 16px 'Cormorant Garamond', serif;
    letter-spacing: 6px;
    color: #fff3dc;
    margin: 8px 0;
}

.cover-date {
    font: 21px 'Cormorant Garamond', serif;
    letter-spacing: 3px;
    color: #fff0d4;
    margin-top: 22px;
}

.cover-city {
    font: 9px Montserrat, sans-serif;
    letter-spacing: 4px;
    color: #ead5a8;
    margin-top: 8px;
}

.page {
    background: var(--cream);
    border-left: 1px solid #dfc99f;
    border-right: 1px solid #dfc99f;
    padding: 46px 26px;
    text-align: center;
    min-height: 330px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    animation: fadein 1s ease both;
}

.page-title {
    font: 36px 'Cormorant Garamond', serif;
    color: var(--wine);
    font-weight: 400;
    margin: 8px 0;
}

.copy {
    font: 18px 'Cormorant Garamond', serif;
    line-height: 1.65;
    color: #684d53;
}

.flourish {
    color: #b28b4d;
    letter-spacing: 8px;
    margin: 14px 0;
}

.event-title {
    font: 31px 'Cormorant Garamond', serif;
    color: var(--wine);
}

.event-date {
    font: 10px Montserrat, sans-serif;
    letter-spacing: 2px;
    color: #94777a;
    margin: 8px 0 12px;
}

.date-number {
    font: 58px 'Cormorant Garamond', serif;
    color: var(--wine);
    line-height: 1;
}

.count {
    font: 34px 'Cormorant Garamond', serif;
    color: var(--wine);
}

.stButton > button,
.stLinkButton > a {
    background: var(--wine) !important;
    color: var(--cream) !important;
    border: 1px solid var(--gold) !important;
    border-radius: 0 !important;
    font: 10px Montserrat, sans-serif !important;
    letter-spacing: 2px !important;
    padding: 12px 15px !important;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    background: #7b2943 !important;
}

.footer {
    text-align: center;
    padding: 22px 8px;
    font: 9px Montserrat, sans-serif;
    letter-spacing: 3px;
    color: #9d817c;
}

@keyframes reveal {
    from {
        opacity: 0;
        transform: translateY(25px) scale(.97);
        clip-path: inset(8% 0);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
        clip-path: inset(0);
    }
}

@keyframes fadein {
    from {
        opacity: 0;
        transform: translateY(14px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media(max-width:520px) {
    .cover {
        min-height: 590px;
        padding: 32px 20px;
    }

    .page {
        padding: 40px 20px;
        min-height: 310px;
    }
}

</style>
""", unsafe_allow_html=True)


# SESSION STATE
if "opened" not in st.session_state:
    st.session_state.opened = False


# COVER FUNCTION
def cover():

    if tirupati_base64:
        image_html = (
            '<img src="data:image/png;base64,'
            + tirupati_base64
            + '" alt="Tirupati Balaji" />'
        )
    else:
        image_html = ""

    html = (
        '<div class="invite">'
        '<div class="cover">'
        '<div class="eyebrow">'
        'Together with their families'
        '</div>'
        '<div class="cover-art">'
        + image_html +
        '</div>'
        '<div>'
        '<div class="script">' + BRIDE + '</div>'
        '<div class="weds">WEDS</div>'
        '<div class="script">' + GROOM + '</div>'
        '<div class="flourish">✧ ❀ ✧</div>'
        '<div class="cover-date">13 · 12 · 2026</div>'
        '<div class="cover-city">' + CITY.upper() + '</div>'
        '</div>'
        '</div>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


# INNER PAGE FUNCTION
def page(html):

    html = textwrap.dedent(html).strip()

    complete_html = (
        '<div class="invite">'
        '<div class="page">'
        + html +
        '</div></div>'
    )

    st.markdown(
        complete_html,
        unsafe_allow_html=True
    )


# OPENING COVER
if not st.session_state.opened:

    cover()

    if not tirupati_base64:
        st.error(
            "Tirupati image not found. "
            "Please keep tirupati.png in the app.py folder."
        )

    if st.button(
        "✧  OPEN INVITATION  ✧",
        use_container_width=True
    ):
        st.session_state.opened = True
        st.rerun()

    st.markdown(
        '<div class="footer">'
        'A CELEBRATION OF LOVE · 2026'
        '</div>',
        unsafe_allow_html=True
    )

    st.stop()


# INVITATION INTRODUCTION
cover()

page("""
<div class="eyebrow" style="color:#987a69">
With the blessings of our families
</div>

<div class="flourish">✧ ❀ ✧</div>

<div class="page-title">
You are cordially invited
</div>

<div class="copy">
With hearts full of joy, we invite you to share in the happiness of a beautiful new beginning as
</div>

<div class="script" style="color:#64172f;font-size:48px">
Reshma weds Praveen
</div>

<div class="copy">
Your presence and blessings will make our celebration truly special.
Come, be part of the love, laughter and memories we will cherish forever.
</div>

<div class="flourish">✧ ❀ ✧</div>

<div class="eyebrow" style="color:#987a69">
With love from both families
</div>
""")


# COUNTDOWN
remaining = (WEDDING_DATE - date.today()).days

if remaining > 0:

    countdown = (
        f'<div class="count">{remaining}</div>'
        '<div class="eyebrow" style="color:#987a69">'
        'DAYS UNTIL THE WEDDING'
        '</div>'
    )

elif remaining == 0:

    countdown = (
        '<div class="copy">'
        'Today is the day! Let the celebrations begin.'
        '</div>'
    )

else:

    countdown = (
        '<div class="copy">'
        'A beautiful day remembered with love.'
        '</div>'
    )


page(f"""
<div class="eyebrow" style="color:#987a69">
Save the date
</div>

<div class="flourish">✧ ❀ ✧</div>

<div class="page-title">
A date to remember
</div>

<div class="date-number">13</div>

<div class="event-date">
DECEMBER · 2026
</div>

{countdown}

<div class="flourish">✧ ❀ ✧</div>

<div class="copy">
A new chapter. A lifetime of togetherness.
</div>
""")


# CELEBRATION DETAILS
page("""
<div class="eyebrow" style="color:#987a69">
The celebrations
</div>

<div class="flourish">✧ ❀ ✧</div>

<div style="font-size:34px">🌼</div>

<div class="event-title">
Haldi Ceremony
</div>

<div class="event-date">
SATURDAY · 12 DECEMBER 2026
</div>

<div class="copy">
A joyful gathering filled with sunshine, laughter and blessings.
</div>

<div class="flourish">❧</div>

<div style="font-size:34px">💍</div>

<div class="event-title">
Wedding Ceremony
</div>

<div class="event-date">
SUNDAY · 13 DECEMBER 2026
</div>

<div class="copy">
Join us as two hearts begin their forever.
</div>

<div class="flourish">✧ ❀ ✧</div>

<div class="eyebrow" style="color:#987a69">
Wedding Venue
</div>

<div class="event-title" style="font-size:25px">
VR Swamy Kalyan Mantapa
</div>

<div class="copy" style="font-size:16px;line-height:1.5">
Ring Rd, Yamlimunuligaon, Taj Sultanpur,<br>
Kalaburagi (Kalburgi), Karnataka 585104
</div>

<div class="flourish">✧ ❀ ✧</div>

""")

# BLESSINGS PAGE
page("""
<div class="eyebrow" style="color:#987a69">
A note from the heart
</div>

<div class="flourish">✧ ❀ ✧</div>

<div class="page-title">
Your blessings mean everything
</div>

<div class="copy">
As we begin this beautiful journey together, we would be honoured to have you with us.
May your blessings add warmth to our celebration and become a treasured part of the memories we create.
</div>

<div class="script" style="color:#64172f;font-size:48px">
Reshma & Praveen
</div>

<div class="flourish">✧ ❀ ✧</div>

<div class="eyebrow" style="color:#987a69">
With love · 2026
</div>
""")


# BACK TO COVER
if st.button(
    "BACK TO THE COVER",
    use_container_width=True
):
    st.session_state.opened = False
    st.rerun()


# FOOTER
st.markdown(
    '<div class="footer">'
    'RESHMA WEDS PRAVEEN · WITH LOVE & BLESSINGS'
    '</div>',
    unsafe_allow_html=True
)
