import streamlit as st
import pandas as pd

# Function to handle file uploads and uses file names for column
def upload_and_merge():
    st.title("Merge CSV Files with File Names")

    # File uploader for multiple files
    uploaded_files = st.file_uploader(
        "Upload CSV files", type=["csv"], accept_multiple_files=True
    )

    if uploaded_files:
        all_dataframes = []  # List to store dataframes

        # Process each uploaded file
        for uploaded_file in uploaded_files:
            # Use the file name (without extension) as the column value
            file_name = uploaded_file.name.rsplit('.', 1)[0]  # Removes .csv extension
            
            # Read the uploaded CSV file
            df = pd.read_csv(uploaded_file)

            # Add the FileName column using the file name
            df["FileName"] = file_name

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
