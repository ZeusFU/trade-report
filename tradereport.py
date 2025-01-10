import os
import pandas as pd
import streamlit as st

# Title
st.title("CSV Merger Web App")

# File uploader
uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True, type=['csv'])

if uploaded_files:
    merged_data = []

    for file in uploaded_files:
        data = pd.read_csv(file)
        data['Account'] = os.path.splitext(file.name)[0]
        merged_data.append(data)

    # Combine all dataframes
    final_df = pd.concat(merged_data, ignore_index=True)
    
    # Download button
    st.write("Merged Data Preview:")
    st.dataframe(final_df)
    
    csv = final_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download Merged CSV",
                       data=csv,
                       file_name='merged_output.csv',
                       mime='text/csv')
