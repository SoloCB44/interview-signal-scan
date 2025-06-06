import streamlit as st
import random

st.set_page_config(page_title="Interview Signal Scan", layout="centered")
st.title("📊 INTERVIEW SIGNAL SCAN™")
st.caption("Private, smart post-interview analyzer")

# Step 0: Mode Selection
st.header("👋 How would you like to begin your interview scan?")
st.markdown("""
Choose the experience that works best for you:

### 🗨️ Chat Mode – Natural & Friendly
- Feels like talking to a smart assistant
- You type your answers freely (or copy/paste them)
- Great if you're more comfortable expressing details in your own words
- Takes a bit longer but feels personal

### 🧩 Guided Mode – Fast & Structured
- Step-by-step with dropdowns, buttons, and sliders
- Easy to complete in 3–5 minutes
- Perfect if you want speed, clarity, or don’t like typing
- Best for focused users or mobile use
""")

mode = st.radio("Choose your mode:", ["🗨️ Chat Mode", "🧩 Guided Mode"])

if mode == "🗨️ Chat Mode":
    st.success("You selected Chat Mode. Let's start the conversation.")
    if 'chat_step' not in st.session_state:
        st.session_state.chat_step = 0

    chat_questions = [
        "🎯 STEP 1: How detailed do you want your scan to be? (Type 1–5)",
        "STEP 2: What kind of interview was this? (1–7)",
        "STEP 2: What is the job level? (1–4)",
        "STEP 2: What was the interview format? (1–3)",
        "STEP 2: Optional extras (number of interviewers, round, follow-up, etc.)",
        "🧩 STEP 3: Ready to begin the scoring scan? (yes/no)"
    ]

    with st.form("chat_form"):
        user_input = st.text_input("Your reply:")
        submitted = st.form_submit_button("Submit")

    if submitted and user_input:
        if user_input.lower() not in ["1", "2", "3", "4", "5", "6", "7", "yes", "no"] and st.session_state.chat_step < 5:
            st.warning("⚠️ I can only help you with your interview. Please stay on track.")
        else:
            st.session_state.chat_step += 1

    if st.session_state.chat_step < len(chat_questions):
        st.write(chat_questions[st.session_state.chat_step])
    else:
        st.success("✅ Scan complete! Here's your result:")
        st.metric("Final Score", "Likely")
        st.metric("Confidence", "82%")
        st.write("📉 Top Risks: Late scheduling, unclear next steps")
        st.write("💡 Strength Signals: Timely response, good tone fit")
        st.write("🛠️ What to Do Next: Wait 3–5 days, follow up if no reply")
        st.bar_chart([70, 85, 90, 60])

elif mode == "🧩 Guided Mode":
    st.success("You selected Guided Mode. Let's walk through this together.")

    if 'step' not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        st.subheader("🎯 Step 1: Choose Analysis Depth")
        depth = st.selectbox("How detailed do you want your scan to be?", [
            "1. 🟢 QUICK SCAN (3 mins / 5 groups)",
            "2. 🔵 STANDARD (5 mins / 7 groups)",
            "3. 🟣 DEEP SCAN (7–8 mins / 10 groups)",
            "4. 🟠 ADVANCED DIAGNOSTIC (10+ mins / 15 groups)",
            "5. ⚫ EXPERT MODE (15–20 mins with extra insights)"
        ])
        if depth.startswith("3") or depth.startswith("4") or depth.startswith("5"):
            visuals = st.radio("Would you like to generate charts or visual feedback?", ["Yes", "No"])
            if visuals == "Yes":
                st.selectbox("Choose your visual style:", [
                    "📊 Bar Graphs (Simple)",
                    "🧭 Radar Charts (Behavioral Fit)",
                    "🧠 Heatmaps (Signal Strength)",
                    "🔄 Sankey Flows (Follow-up Likelihood)",
                    "💡 Choose your own visual"
                ])
        if st.button("Next"):
            st.session_state.step += 1

    elif st.session_state.step == 2:
        st.subheader("🧩 Step 2: Set Interview Context")
        st.selectbox("What kind of interview was this?", [
            "1. Technical", "2. Behavioral", "3. Sales", "4. Healthcare",
            "5. Academic / Research", "6. Customer Service", "7. Other"
        ])
        st.radio("What is the job level?", [
            "1. Entry", "2. Mid-level", "3. Senior", "4. Executive/Management"
        ])
        st.radio("What was the interview format?", [
            "1. In-person", "2. Video", "3. Phone"
        ])
        st.text_area("Optional: How many interviewers? Round? Timeline?")
        if st.button("Start Scan"):
            st.session_state.step += 1

    elif st.session_state.step == 3:
        st.subheader("⏱️ Step 3: Scoring Questions")
        group = st.slider("📍 Group 1 of 5 – Est. time left: 3 min", 1, 5, 1)
        st.radio("How confident were you in your answers?", ["1. Very", "2. Somewhat", "3. Not much", "4. Unsure"])
        st.radio("Did the interview feel conversational?", ["1. Yes", "2. A bit", "3. No", "4. Not sure"])
        st.radio("How quickly did they respond after earlier rounds?", ["1. <24h", "2. 1–2 days", "3. 3–5 days", "4. Longer"])
        if st.button("Finish Scan"):
            st.session_state.step += 1

    elif st.session_state.step == 4:
        st.success("✅ Scan complete! Here's your result:")
        st.metric("Final Score", random.choice(["Excellent", "Likely", "Unclear", "Unlikely"]))
        st.metric("Confidence", f"{random.randint(70, 95)}%")
        st.write("📉 Top Risks: Response delay, vague direction")
        st.write("💡 Strength Signals: Fast scheduling, engaged tone")
        st.write("🛠️ What to Do Next: Follow up or prepare next steps")
        st.bar_chart([60, 75, 90, 55])
