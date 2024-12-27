import json
import requests
import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize

# Function to fetch a JSON file from GitHub
def fetch_json_from_github(url):
    response = requests.get(url)
    #st.write("Status", response.status_code)
    #st.write(response.text)
    response.raise_for_status()  # Check for HTTP request errors
    return response.text  # Return parsed JSON

# Streamlit application
def main():
    st.title("Poet Information from GitHub")
    df = pd.DataFrame({})
    # Input for the GitHub URL
    #url = st.text_input("Enter the GitHub raw JSON URL", "")
    url = 'https://raw.githubusercontent.com/papavask/Dataframe01/main/page07.txt'
    if url:
        try:
            # Fetch the JSON data from the provided URL
            data = fetch_json_from_github(url)
        except Exception as e:
            st.error(f"Error: {e}")

        try:
            # Display data
            #st.write(data)
            #jstr = json.loads(data)
            astr = data.splitlines()
            for poet in astr:
                #st.write("List>>>>",poet)  # Display each poet's information
                jstr = json.loads(poet)
                #st.write("Json>>>>", jstr)
                dt = pd.json_normalize(jstr)
                #st.write("Norm >>>>>",dt)
                #df.append(dt, ignore_index=True)  
                if df.empty:
                    df = dt
                else:       
                    df = pd.concat([df, dt], ignore_index=True)
        except Exception as e:
            st.error(f"Error: {e}")

    st.dataframe(df)
if __name__ == "__main__":
    main()