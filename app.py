import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="Haryf Games - Hangman", page_icon="🕹️")

# هيدر التطبيق
st.title("🕹️ ساحة ألعاب الحريف")
st.markdown("---")

# قائمة الكلمات (تقدر تزود كلمات براحتك)
words = ["PYTHON", "STREAMLIT", "ANDROID", "GITHUB", "PROGRAMMING", "INTELLIGENCE"]

# تهيئة اللعبة
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.attempts = 6

st.subheader("لعبة تخمين الكلمة (Hangman)")
st.write(f"المحاولات المتبقية: **{st.session_state.attempts}** ❤️")

# عرض الكلمة المخفية
display_word = "".join([letter if letter in st.session_state.guessed_letters else " _ " for letter in st.session_state.word])
st.header(display_word)

# إدخال الحروف
input_letter = st.text_input("اكتب حرفاً واحدًا:", max_chars=1).upper()

if st.button("تخمين"):
    if input_letter in st.session_state.guessed_letters:
        st.warning("جربت الحرف ده قبل كدة!")
    elif input_letter in st.session_state.word:
        st.session_state.guessed_letters.append(input_letter)
        st.success("صح! حرف موجود.")
    else:
        st.session_state.attempts -= 1
        st.error("خطأ! الحرف مش موجود.")
    
    # التحقق من الفوز أو الخسارة
    if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
        st.balloons()
        st.success(f"مبروك يا مبرمج! الكلمة هي: {st.session_state.word}")
        if st.button("العب تاني"):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()
            
    if st.session_state.attempts <= 0:
        st.error(f"للأسف خسرت! الكلمة كانت: {st.session_state.word}")
        if st.button("محاولة جديدة"):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()

st.sidebar.info("صنع بواسطة: أحمد الحريف 🚀")
      
