import streamlit as st
import pandas as pd

# הגדרות תצוגה בסיסיות
st.set_page_config(page_title="תכנון החתונה", page_icon="💍", layout="wide")

st.title("💍 תכנון החתונה של אושר ושלי")
st.markdown("ברוכים הבאים למערכת תכנון החתונה! כאן תוכלו לנהל את כל המשימות, המוזמנים, והתקציב במקום אחד.")

# אתחול נתונים התחלתיים בזיכרון (Session State) כדי שהעריכה לא תימחק במעבר בין עמודים
if 'guests' not in st.session_state:
    st.session_state.guests = pd.DataFrame({
        "שם מלא": ["ישראל ישראלי", "משה כהן"],
        "צד": ["אושר", "שלי"],
        "סטטוס הגעה": ["טרם אישרו", "אישרו"],
        "כמות אורחים": [2, 1]
    })

if 'budget' not in st.session_state:
    st.session_state.budget = pd.DataFrame({
        "קטגוריה": ["אולם", "קייטרינג", "צלם", "דיג'יי", "בגדים"],
        "עלות משוערת (₪)": [50000, 30000, 10000, 7000, 5000],
        "עלות בפועל (₪)": [0, 0, 0, 0, 0]
    })

if 'venues' not in st.session_state:
    st.session_state.venues = pd.DataFrame({
        "שם האולם": ["אולם חלומות", "גן הפקאן"],
        "מיקום": ["מרכז", "שרון"],
        "מחיר למנה": [350, 400],
        "הערות": ["אהבנו את החופה", "יקר קצת אבל יפה"]
    })

# תפריט ניווט צדדי
st.sidebar.title("ניווט 📌")
page = st.sidebar.radio("בחר עמוד:", ["✅ צ׳ק ליסט", "👥 רשימת מוזמנים", "💰 ניהול תקציב", "🏰 אולמות אירועים"])

# עמוד 1: צ'ק ליסט
if page == "✅ צ׳ק ליסט":
    st.header("צ׳ק ליסט משימות")
    st.markdown("סמנו את המשימות שכבר סיימתם:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("סגירת תאריך ואולם")
        st.checkbox("בחירת צלם סטילס ווידאו")
        st.checkbox("בחירת דיג'יי")
    with col2:
        st.checkbox("סגירת חברת קייטרינג / תפריט")
        st.checkbox("בחירת בגדים וטבעות")
        st.checkbox("שליחת הזמנות לאורחים (Save the Date)")

# עמוד 2: רשימת מוזמנים
elif page == "👥 רשימת מוזמנים":
    st.header("רשימת מוזמנים")
    st.markdown("כאן תוכלו לערוך, להוסיף ולמחוק מוזמנים. פשוט לחצו פעמיים על תא כדי לערוך אותו, או על שורת ה-Plus למטה כדי להוסיף שורה חדשה.")
    
    # טבלה אינטראקטיבית שמעדכנת את הזיכרון
    edited_guests = st.data_editor(st.session_state.guests, num_rows="dynamic", use_container_width=True)
    st.session_state.guests = edited_guests
    
    total_guests = edited_guests["כמות אורחים"].sum()
    st.info(f"סה״כ מוזמנים ברשימה (כולל בני זוג): **{total_guests}**")

# עמוד 3: תקציב
elif page == "💰 ניהול תקציב":
    st.header("ניהול תקציב")
    st.markdown("טבלת הוצאות משוערות מול בפועל.")
    
    edited_budget = st.data_editor(st.session_state.budget, num_rows="dynamic", use_container_width=True)
    st.session_state.budget = edited_budget
    
    total_estimated = edited_budget["עלות משוערת (₪)"].sum()
    total_actual = edited_budget["עלות בפועל (₪)"].sum()
    
    col1, col2 = st.columns(2)
    col1.metric("סה״כ תקציב משוער", f"₪{total_estimated:,}")
    col2.metric("סה״כ הוצאות בפועל", f"₪{total_actual:,}")

# עמוד 4: אולמות
elif page == "🏰 אולמות אירועים":
    st.header("השוואת אולמות אירועים")
    st.markdown("תרכזו כאן את כל האולמות שהייתם בהם כדי לקבל החלטה נוחה:")
    
    edited_venues = st.data_editor(st.session_state.venues, num_rows="dynamic", use_container_width=True)
    st.session_state.venues = edited_venues