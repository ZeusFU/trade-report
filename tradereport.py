import streamlit as st
import pandas as pd

# Function to handle file uploads and prompts for Account names
def upload_and_merge():
    st.title("Merge CSV Files with Account Names")

    # File uploader for multiple files
    uploaded_files = st.file_uploader(
        "Upload CSV files", type=["csv"], accept_multiple_files=True
    )

    if uploaded_files:
        all_dataframes = []  # List to store dataframes

        # Process each uploaded file
        for uploaded_file in uploaded_files:
            # Prompt user for Account name
            account_name = st.text_input(f"What account is this? (File: {uploaded_file.name})")

            # Proceed if an account name is provided
            if account_name:
                # Read the uploaded CSV file
                df = pd.read_csv(uploaded_file)

                # Add the Account column
                df["Account"] = account_name

                # Append to the list of dataframes
                all_dataframes.append(df)

        # Merge all dataframes if any were uploaded
        if all_dataframes:
            merged_df = pd.concat(all_dataframes, ignore_index=True)

            # Display the merged dataframe
            st.write("Merged Data:")
            st.dataframe(merged_df)

            # Provide download link for the merged CSV
            csv = merged_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Merged CSV",
                data=csv,
                file_name="merged_data.csv",
                mime="text/csv",
            )

# Run the app
if __name__ == "__main__":
    upload_and_merge()
