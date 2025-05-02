import streamlit as st

# 🔹 Set up the Streamlit app title and description
st.title("⚖️ BMI Calculator - Know Your Health Status!")
st.write("### 🎨 Designed for an interactive experience with real-time calculations!")
st.write("---")

def calculate_bmi(height, weight):
    bmi = round(weight / ((height / 100) ** 2), 1)
    if bmi < 28.5:
        return f"📊 Your BMI is {bmi}: **Underweight** \n\n🍎 You need to gain some weight! "
    elif 28.5 <= bmi < 45:
        return f"📊 Your BMI is {bmi}: **Healthy** \n\n💪 Great job! Keep it up! "
    elif 45 <= bmi < 60:
        return f"📊 Your BMI is {bmi}: **Overweight** \n\n⚖️ Consider a balanced diet! "
    else:
        return f"📊 Your BMI is {bmi}: **Obese** \n\n💪 Time to hit the gym! "

# 🔹 Collect user input with better formatting
st.write("## 🎯 Enter Your Details Below")
st.write("---")
height = st.number_input("📏 Enter height in cm:", min_value=50.0, max_value=300.0, step=0.1)
weight = st.number_input("⚖️ Enter weight in kg:", min_value=10.0, max_value=500.0, step=0.1)

if st.button("🧮 Calculate BMI"):
    if height > 0 and weight > 0:
        result = calculate_bmi(height, weight)
        st.success(result)
        st.balloons()
    else:
        st.error("❌ Please enter valid height and weight values.")

st.write("---")
st.write("### 💡 Tip: A healthy lifestyle starts with knowing your numbers!")