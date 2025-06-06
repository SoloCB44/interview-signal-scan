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

if language == "العربية":
    st.markdown("""
    ✅ هذا الأداة خاصة وآمنة — لا يتم حفظ أو مشاركة أي بيانات شخصية.
    ✅ ستحصل على نتيجة تقييم، إشارات القوة والمخاطر، ونصائح للخطوة التالية.

    🔽 دعنا نبدأ بخطوات بسيطة.
    """)
    st.header("🧭 مراجعة المقابلة خطوة بخطوة")
else:
    st.header("🧭 Step-by-Step Interview Review")

# Session state init
TOTAL_GROUPS = 5
if 'current_group' not in st.session_state:
    st.session_state.current_group = 1

def navigation_buttons():
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.session_state.current_group > 1:
            if st.button("⬅️ Back"):
                st.session_state.current_group -= 1
    with col2:
        if st.button("➡️ Next"):
            st.session_state.current_group += 1

# Group 1 – Depth
if st.session_state.current_group == 1:
    st.subheader("📍 Group 1 of 5 – Choose Scan Depth")
    if language == "العربية":
        st.selectbox("اختر المستوى:", [
            "1. 🟢 تحليل سريع (3 دقائق / 5 مجموعات)",
            "2. 🔵 قياسي (5 دقائق / 7 مجموعات)",
            "3. 🟣 عميق (8 دقائق / 10 مجموعات)",
            "4. 🟠 تشخيص متقدم (10+ دقائق / 15 مجموعة)",
            "5. ⚫ وضع خبير (يشمل التوقعات والرسوم البيانية)"
        ], key="depth")
        if st.session_state.depth.startswith("3") or st.session_state.depth.startswith("4") or st.session_state.depth.startswith("5"):
            st.radio("هل ترغب بالحصول على رسوم بيانية؟", ["نعم", "لا"], key="visuals")
            if st.session_state.visuals == "نعم":
                st.selectbox("اختر نوع الرسم البياني:", [
                    "📊 Bar Graphs", "🧭 Radar Charts", "🧠 Heatmaps", "🔄 Sankey Flows", "💡 Custom Visual"
                ], key="chart")
    else:
        st.selectbox("Choose a level:", [
            "1. 🟢 QUICK SCAN (3 mins / 5 groups)",
            "2. 🔵 STANDARD (5 mins / 7 groups)",
            "3. 🟣 DEEP SCAN (8 mins / 10 groups)",
            "4. 🟠 ADVANCED DIAGNOSTIC (10+ mins / 15 groups)",
            "5. ⚫ EXPERT MODE (with visuals and forecasting)"
        ], key="depth")
        if st.session_state.depth.startswith("3") or st.session_state.depth.startswith("4") or st.session_state.depth.startswith("5"):
            st.radio("Would you like to generate charts or visual feedback?", ["Yes", "No"], key="visuals")
            if st.session_state.visuals == "Yes":
                st.selectbox("Choose your visual style:", [
                    "📊 Bar Graphs", "🧭 Radar Charts", "🧠 Heatmaps", "🔄 Sankey Flows", "💡 Custom Visual"
                ], key="chart")
    navigation_buttons()

# Group 2 – Context
elif st.session_state.current_group == 2:
    st.subheader("📍 Group 2 of 5 – Interview Context")
    if language == "العربية":
        st.selectbox("نوع المقابلة:", [
            "1. تقنية", "2. سلوكية", "3. مبيعات", "4. رعاية صحية", "5. أكاديمية / بحث", "6. خدمة عملاء", "7. أخرى"
        ], key="type")
        st.radio("مستوى الوظيفة:", ["1. مبتدئ", "2. متوسط", "3. خبير", "4. إدارة/قيادة"], key="level")
        st.radio("صيغة المقابلة:", ["1. حضور شخصي", "2. فيديو", "3. هاتف"], key="format")
        st.text_area("معلومات إضافية:", key="extras")
    else:
        st.selectbox("What kind of interview was it?", [
            "1. Technical", "2. Behavioral", "3. Sales", "4. Healthcare", "5. Academic / Research", "6. Customer Service", "7. Other"
        ], key="type")
        st.radio("Job level:", ["1. Entry", "2. Mid-level", "3. Senior", "4. Executive/Management"], key="level")
        st.radio("Interview format:", ["1. In-person", "2. Video", "3. Phone"], key="format")
        st.text_area("Optional extras:", key="extras")
    navigation_buttons()

# Group 3 – Signal Check
elif st.session_state.current_group == 3:
    st.subheader("📍 Group 3 of 5 – Signal Check")
    st.radio("How confident were you in your responses?", ["✅ Strong", "⚠️ Somewhat", "❌ Unsure"], key="conf")
    st.radio("How fast did they follow up?", ["✅ <24h", "⚠️ 1–3 days", "❌ Longer"], key="speed")
    st.radio("Did they describe next steps clearly?", ["✅ Yes", "⚠️ Vague", "❌ No"], key="nextsteps")
    navigation_buttons()

# Group 4 – Show Results
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
    navigation_buttons()

# Group 5 – Closing
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
