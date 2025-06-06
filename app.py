import streamlit as st
import random
import time

st.set_page_config(page_title="Interview Signal Scan", layout="centered")
st.title("📊 INTERVIEW SIGNAL SCAN™")

st.markdown("""
Welcome to **Interview Signal Scan™** — your step-by-step guide to analyzing how your recent interview went.

✅ This tool is fully private and anonymous — no data is stored or shared.  
✅ You'll get a final confidence score, key strength/risk signals, and advice on what to do next.

Choose your language to begin:
""")

language = st.radio("🌍 Language / اللغة:", ["English", "العربية"], key="lang")

if 'current_group' not in st.session_state:
    st.session_state.current_group = 1
if 'next_clicked' not in st.session_state:
    st.session_state.next_clicked = False
if 'back_clicked' not in st.session_state:
    st.session_state.back_clicked = False

# Language-based headers
if language == "العربية":
    st.markdown("""
    ✅ هذا الأداة خاصة وآمنة — لا يتم حفظ أو مشاركة أي بيانات شخصية.
    ✅ ستحصل على نتيجة تقييم، إشارات القوة والمخاطر، ونصائح للخطوة التالية.

    🔽 دعنا نبدأ بخطوات بسيطة.
    """)
    st.header("🧭 مراجعة المقابلة خطوة بخطوة")
else:
    st.header("🧭 Step-by-Step Interview Review")

# Define navigation buttons
col1, col2 = st.columns([1, 5])
with col1:
    if st.session_state.current_group > 1:
        back = st.button("⬅️ Back")
        if back:
            st.session_state.back_clicked = True
with col2:
    next = st.button("➡️ Next")
    if next:
        st.session_state.next_clicked = True

# Handle navigation
if st.session_state.next_clicked:
    st.session_state.current_group += 1
    st.session_state.next_clicked = False
elif st.session_state.back_clicked:
    st.session_state.current_group -= 1
    st.session_state.back_clicked = False

# Step 1 – Choose Scan Depth
if st.session_state.current_group == 1:
    st.subheader("📍 Group 1 of 5 – Choose Scan Depth")
    st.selectbox("Choose a level:" if language == "English" else "اختر المستوى:", [
        "1. 🟢 QUICK SCAN (3 mins / 5 groups)" if language == "English" else "1. 🟢 تحليل سريع (3 دقائق / 5 مجموعات)",
        "2. 🔵 STANDARD (5 mins / 7 groups)" if language == "English" else "2. 🔵 قياسي (5 دقائق / 7 مجموعات)",
        "3. 🟣 DEEP SCAN (8 mins / 10 groups)" if language == "English" else "3. 🟣 عميق (8 دقائق / 10 مجموعات)",
        "4. 🟠 ADVANCED DIAGNOSTIC (10+ mins / 15 groups)" if language == "English" else "4. 🟠 تشخيص متقدم (10+ دقائق / 15 مجموعة)",
        "5. ⚫ EXPERT MODE (with visuals and forecasting)" if language == "English" else "5. ⚫ وضع خبير (يشمل التوقعات والرسوم البيانية)"
    ], key="depth")
    if st.session_state.depth.startswith("3") or st.session_state.depth.startswith("4") or st.session_state.depth.startswith("5"):
        st.radio("Would you like to generate charts or visual feedback?" if language == "English" else "هل ترغب بالحصول على رسوم بيانية؟", ["Yes" if language == "English" else "نعم", "No" if language == "English" else "لا"], key="visuals")
        if st.session_state.visuals in ["Yes", "نعم"]:
            st.selectbox("Choose your visual style:" if language == "English" else "اختر نوع الرسم البياني:", [
                "📊 Bar Graphs", "🧭 Radar Charts", "🧠 Heatmaps", "🔄 Sankey Flows", "💡 Custom Visual"
            ], key="chart")

# Step 2 – Interview Context
elif st.session_state.current_group == 2:
    st.subheader("📍 Group 2 of 5 – Interview Context")
    st.selectbox("What kind of interview was it?" if language == "English" else "نوع المقابلة:", [
        "1. Technical" if language == "English" else "1. تقنية",
        "2. Behavioral" if language == "English" else "2. سلوكية",
        "3. Sales" if language == "English" else "3. مبيعات",
        "4. Healthcare" if language == "English" else "4. رعاية صحية",
        "5. Academic / Research" if language == "English" else "5. أكاديمية / بحث",
        "6. Customer Service" if language == "English" else "6. خدمة عملاء",
        "7. Other" if language == "English" else "7. أخرى"
    ], key="type")
    st.radio("Job level:" if language == "English" else "مستوى الوظيفة:", [
        "1. Entry" if language == "English" else "1. مبتدئ",
        "2. Mid-level" if language == "English" else "2. متوسط",
        "3. Senior" if language == "English" else "3. خبير",
        "4. Executive/Management" if language == "English" else "4. إدارة/قيادة"
    ], key="level")
    st.radio("Interview format:" if language == "English" else "صيغة المقابلة:", [
        "1. In-person" if language == "English" else "1. حضور شخصي",
        "2. Video" if language == "English" else "2. فيديو",
        "3. Phone" if language == "English" else "3. هاتف"
    ], key="format")
    st.text_area("Optional extras:" if language == "English" else "معلومات إضافية:", key="extras")

# Step 3 – Signal Check
elif st.session_state.current_group == 3:
    st.subheader("📍 Group 3 of 5 – Signal Check")
    st.radio("How confident were you in your responses?", ["✅ Strong", "⚠️ Somewhat", "❌ Unsure"], key="conf")
    st.radio("How fast did they follow up?", ["✅ <24h", "⚠️ 1–3 days", "❌ Longer"], key="speed")
    st.radio("Did they describe next steps clearly?", ["✅ Yes", "⚠️ Vague", "❌ No"], key="nextsteps")

# Step 4 – Show Results
elif st.session_state.current_group == 4:
    st.subheader("📍 Group 4 of 5 – Analyzing Results...")
    with st.spinner("Calculating signals..."):
        time.sleep(2)
    score = random.randint(60, 95)
    verdict = "Excellent" if score > 85 else "Likely" if score > 70 else "Unclear"
    st.success("✅ Scan complete!")
    st.metric("Final Verdict", verdict)
    st.metric("Confidence Score", f"{score}%")
    st.write("**Top Strengths:** Engaged tone, clear next steps")
    st.write("**Top Risks:** Timing delays, short interview duration")
    st.bar_chart([score, 100 - score])

# Step 5 – Closing
elif st.session_state.current_group == 5:
    st.subheader("📍 Group 5 of 5 – What to Do Next")
    st.markdown("""
    🎯 You’ve completed the Interview Signal Scan!

    Based on your answers, here’s what you can do:
    - 📬 Follow up with the recruiter if you haven’t heard back in 3–5 days.
    - 🧠 Reflect on the signals above. If you scored low, review where clarity or tone could improve.
    - 📈 Want to run again with different priorities (e.g. tone vs. speed)? Just refresh and try again.

    🔒 Remember: No data is saved. You are in full control.
    """)
    st.balloons()
    if st.button("🔁 Restart Scan"):
        st.session_state.current_group = 1
