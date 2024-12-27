import json
import requests
import streamlit as st
import pandas as pd

# Function to fetch a JSON file from GitHub
def fetch_json_from_github(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors
    return response.text  # Return parsed JSON

# Streamlit application
def main():
    st.title("Speculations...")
    df = pd.DataFrame({})
    url = 'https://raw.githubusercontent.com/papavask/Dataframe01/main/page07.txt'
    if url:
        try:
            # Fetch the JSON data from the provided URL
            data = fetch_json_from_github(url)
                    try:
                        astr = data.splitlines()
                        for spec in astr:
                            jstr = json.loads(spec)
                            dt = pd.json_normalize(jstr) 
                            if df.empty:
                                df = dt
                            else:       
                                df = pd.concat([df, dt], ignore_index=True)
                    except Exception as e:
                        st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")

    st.dataframe(df)
if __name__ == "__main__":
    main()
