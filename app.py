import streamlit as st
import re
import random
import string

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    
    if strength == 1:
        remarks = "Very Weak"
    elif strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 4:
        remarks = "Strong"
    
    return strength, remarks

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔑", layout="centered")
    st.title("🔐 Password Strength Checker")
    
    password = st.text_input("Enter your password", type="password")
    
    if password:
        strength, remarks = check_password_strength(password)
        st.write(f"🛡️ Strength: **{remarks}**")
        st.progress(strength / 4)
    
    if st.button("🔄 Generate Strong Password"):
        new_password = generate_password()
        st.success(f"✨ Suggested Password: `{new_password}`")
    
    st.markdown("💡 *Tip: Use a mix of uppercase, lowercase, numbers, and symbols for a strong password!* 🔒")

if __name__ == "__main__":
    main()
