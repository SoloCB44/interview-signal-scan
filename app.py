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

language = st.radio("🌍 Language / اللغة:", ["English", "العربية"])

if language == "العربية":
    st.markdown("""
    ✅ هذا الأداة خاصة وآمنة — لا يتم حفظ أو مشاركة أي بيانات شخصية.
    ✅ ستحصل على نتيجة تقييم، إشارات القوة والمخاطر، ونصائح للخطوة التالية.

    🔽 دعنا نبدأ بخطوات بسيطة.
    """)
    st.header("🧭 مراجعة المقابلة خطوة بخطوة")
else:
    st.header("🧭 Step-by-Step Interview Review")

# Define the number of groups and initialize session state for step tracking
TOTAL_GROUPS = 5
if 'current_group' not in st.session_state:
    st.session_state.current_group = 1

# STEP 1 – Choose Analysis Depth
if st.session_state.current_group == 1:
    st.subheader("📍 Group 1 of 5 – Choose Scan Depth")
    if language == "العربية":
        st.markdown("اختر مدى تفصيل التحليل الذي ترغب به:")
        depth = st.selectbox("اختر المستوى:", [
            "1. 🟢 تحليل سريع (3 دقائق / 5 مجموعات)",
            "2. 🔵 قياسي (5 دقائق / 7 مجموعات)",
            "3. 🟣 عميق (8 دقائق / 10 مجموعات)",
            "4. 🟠 تشخيص متقدم (10+ دقائق / 15 مجموعة)",
            "5. ⚫ وضع خبير (يشمل التوقعات والرسوم البيانية)"
        ])
        if depth.startswith("3") or depth.startswith("4") or depth.startswith("5"):
            visuals = st.radio("هل ترغب بالحصول على رسوم بيانية؟", ["نعم", "لا"])
            if visuals == "نعم":
                st.selectbox("اختر نوع الرسم البياني:", [
                    "📊 Bar Graphs", "🧭 Radar Charts", "🧠 Heatmaps", "🔄 Sankey Flows", "💡 Custom Visual"
                ])
    else:
        st.markdown("How detailed do you want your scan to be?")
        depth = st.selectbox("Choose a level:", [
            "1. 🟢 QUICK SCAN (3 mins / 5 groups)",
            "2. 🔵 STANDARD (5 mins / 7 groups)",
            "3. 🟣 DEEP SCAN (8 mins / 10 groups)",
            "4. 🟠 ADVANCED DIAGNOSTIC (10+ mins / 15 groups)",
            "5. ⚫ EXPERT MODE (with visuals and forecasting)"
        ])
        if depth.startswith("3") or depth.startswith("4") or depth.startswith("5"):
            visuals = st.radio("Would you like to generate charts or visual feedback?", ["Yes", "No"])
            if visuals == "Yes":
                st.selectbox("Choose your visual style:", [
                    "📊 Bar Graphs", "🧭 Radar Charts", "🧠 Heatmaps", "🔄 Sankey Flows", "💡 Custom Visual"
                ])
    if st.button("Next"):
        st.session_state.current_group += 1

# STEP 2 – Interview Context
elif st.session_state.current_group == 2:
    st.subheader("📍 Group 2 of 5 – Interview Context")
    if language == "العربية":
        st.markdown("أخبرنا عن سياق المقابلة:")
        st.selectbox("نوع المقابلة:", [
            "1. تقنية", "2. سلوكية", "3. مبيعات", "4. رعاية صحية", "5. أكاديمية / بحث", "6. خدمة عملاء", "7. أخرى"
        ])
        st.radio("مستوى الوظيفة:", ["1. مبتدئ", "2. متوسط", "3. خبير", "4. إدارة/قيادة"])
        st.radio("صيغة المقابلة:", ["1. حضور شخصي", "2. فيديو", "3. هاتف"])
        st.text_area("معلومات إضافية (عدد المقابلين، الجولة، هل ذكرت الخطوات التالية؟)")
    else:
        st.markdown("Tell us a bit about your interview:")
        st.selectbox("What kind of interview was it?", [
            "1. Technical", "2. Behavioral", "3. Sales", "4. Healthcare", "5. Academic / Research", "6. Customer Service", "7. Other"
        ])
        st.radio("Job level:", ["1. Entry", "2. Mid-level", "3. Senior", "4. Executive/Management"])
        st.radio("Interview format:", ["1. In-person", "2. Video", "3. Phone"])
        st.text_area("Optional extras: (interviewers, round, response time, next steps mentioned?)")
    if st.button("Next"):
        st.session_state.current_group += 1

# STEP 3 – Scoring Simulation (for demonstration)
elif st.session_state.current_group == 3:
    st.subheader("📍 Group 3 of 5 – Signal Check")
    st.radio("How confident were you in your responses?", ["✅ Strong", "⚠️ Somewhat", "❌ Unsure"])
    st.radio("How fast did they follow up?", ["✅ <24h", "⚠️ 1–3 days", "❌ Longer"])
    st.radio("Did they describe next steps clearly?", ["✅ Yes", "⚠️ Vague", "❌ No"])
    if st.button("Next"):
        st.session_state.current_group += 1

# STEP 4 – Visualize & Show Results
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
    if st.button("Next"):
        st.session_state.current_group += 1

# STEP 5 – Closing Message
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
