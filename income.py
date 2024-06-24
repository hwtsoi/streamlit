import streamlit as st

# Title and description
st.title("Income Categorization")
st.write("Enter your income to see the category.")

# Input for income
income = st.number_input("What is your income?", min_value=0)

# Convert to integer (optional, happens automatically with number_input)
# income = int(income)  # Uncomment if needed with different input type

# Income categorization with logic
if income > 8000:
    category = "High income"
elif income > 4000:
    category = "Medium high income"
elif income > 2000:
    category = "Medium income"
elif income > 1000:
    category = "Medium low income"
else:
    category = "Low income"

# Display the income category
st.write(f"Your income category is: {category}")

