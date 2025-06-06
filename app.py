import streamlit as st
import random

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

# STEP 1 – Choose Analysis Depth
if language == "العربية":
    st.subheader("الخطوة 1: مستوى التحليل")
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
    st.subheader("Step 1: Choose Analysis Depth")
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

# STEP 2 – Interview Context
if language == "العربية":
    st.subheader("الخطوة 2: نوع المقابلة")
    st.markdown("اختر نوع المقابلة التي خضتها:")
    st.selectbox("نوع المقابلة:", [
        "1. تقنية", "2. سلوكية", "3. مبيعات", "4. رعاية صحية", "5. أكاديمية / بحث", "6. خدمة عملاء", "7. أخرى"
    ])
    st.radio("مستوى الوظيفة:", ["1. مبتدئ", "2. متوسط", "3. خبير", "4. إدارة/قيادة"])
    st.radio("صيغة المقابلة:", ["1. حضور شخصي", "2. فيديو", "3. هاتف"])
    st.text_area("معلومات إضافية (عدد المقابلين، الجولة، هل ذكرت الخطوات التالية؟)")
else:
    st.subheader("Step 2: Interview Context")
    st.markdown("Tell us a bit about your interview:")
    st.selectbox("What kind of interview was it?", [
        "1. Technical", "2. Behavioral", "3. Sales", "4. Healthcare", "5. Academic / Research", "6. Customer Service", "7. Other"
    ])
    st.radio("Job level:", ["1. Entry", "2. Mid-level", "3. Senior", "4. Executive/Management"])
    st.radio("Interview format:", ["1. In-person", "2. Video", "3. Phone"])
    st.text_area("Optional extras: (interviewers, round, response time, next steps mentioned?)")

st.button("Next Step")
