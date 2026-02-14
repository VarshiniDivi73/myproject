import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Heyy Love 💖", page_icon="💘")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center; color: #ff4b6e;'>Heyy Love 💕</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Will you be my <span style='color:red;'>Valentine?</span> 💖</h2>", unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    # YES BUTTON
    with col1:
        if st.button("Yes 💘"):
            st.session_state.page = "love"
            st.rerun()

    # NO BUTTON (Moves randomly)
    with col2:
        x = random.randint(0, 300)
        y = random.randint(0, 300)

        no_button_html = f"""
        <div style="
            position: relative;
            left: {x}px;
            top: {y}px;">
            <button style="
                background-color: grey;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                border: none;">
                No 😢
            </button>
        </div>
        """

        st.markdown(no_button_html, unsafe_allow_html=True)

# ---------------- LOVE PAGE ----------------
elif st.session_state.page == "love":
    st.markdown("<h1 style='text-align: center; color: #ff4b6e;'>💖 Thank You My Love 💖</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size:20px;'>
    thank you my love you are amazing and most perfect man I have ever seen.<br><br>
    its been a blessing to have a man like you in my life.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("<h2 style='text-align: center; color: red;'>I LOVE YOU TEJA ❤️</h2>", unsafe_allow_html=True)

    st.write("")

    st.markdown("<p style='text-align: center; font-style: italic;'>-by yours varsha 💌</p>", unsafe_allow_html=True)
