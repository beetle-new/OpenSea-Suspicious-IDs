import streamlit as st
import requests
import pandas as pd
import os

api_key = os.environ.get("api_key")

st.title("Flagged OS Tokens")
st.markdown("Created with <3 by [@1kbeetlejuice](https://twitter.com/1kbeetlejuice).")

# Get user input for filter
filter_input = st.text_input("Enter a filter for the collection:", "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d")

# Define the URLs
bored_ape_url = f"https://api.reservoir.tools/tokens/ids/v1?collection={filter_input}&flagStatus=1&limit=1000"

# Define headers
headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

# Make the GET requests
suspicious_response = requests.get(bored_ape_url, headers=headers)

# Convert the responses to JSON
data = suspicious_response.json()

# Create dataframe for Bored Ape
bored_ape_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

# Concatenate the two dataframes
df = pd.concat([bored_ape_df], axis=1)

# Count the total number of rows
total_rows = df.shape[0]
collection_url = f"https://api.reservoir.tools/collections/v5?id={filter_input}&includeTopBid=true&includeAttributes=false&includeOwnerCount=true&useNonFlaggedFloorAsk=true"

headers = {
    "accept": "432bae1c-ea9b-5c76-9b6f-8a159cd78e3a",
    "x-api-key": "demo-api-key"
}

response = requests.get(collection_url, headers=headers)

data = response.json()

collections = data['collections']

name = [collection['name'] for collection in collections]
col1, col2 = st.columns(2)

with col1:
    st.metric("Collection Name: ", name[0])

with col2:
    st.metric("Total Suspicious Tokens: ", total_rows)

col1, col2, col3 = st.columns(3)

with col2:
    st.dataframe(bored_ape_df)





####################################################################################################################################

st.title("Total Marked Suspicious Tokens for Blue-Chip Collections")



################################################# BAYC #########################################################
col1, col2, col3 = st.columns(3)

bored_ape_url = "https://api.reservoir.tools/tokens/ids/v1?collection=0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d&flagStatus=1&limit=1000"

headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

suspicious_response = requests.get(bored_ape_url, headers=headers)

data = suspicious_response.json()

bored_ape_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

total_rows = bored_ape_df.shape[0]

with col1:  
    st.metric("Bored Ape Yacht Club: ", total_rows)


############################################################ MAYC ########################################################################

mayc_url = "https://api.reservoir.tools/tokens/ids/v1?collection=0x60e4d786628fea6478f785a6d7e704777c86a7c6&flagStatus=1&limit=1000"

headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

suspicious_response = requests.get(mayc_url, headers=headers)

data = suspicious_response.json()

mayc_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

total_rows = mayc_df.shape[0]

with col2:
    st.metric("Mutant Ape Yacht Club: ", total_rows)

############################################################ AZUKI ########################################################################

azuki_url = "https://api.reservoir.tools/tokens/ids/v1?collection=0xed5af388653567af2f388e6224dc7c4b3241c544&flagStatus=1&limit=1000"

headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

suspicious_response = requests.get(azuki_url, headers=headers)

data = suspicious_response.json()

azuki_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

total_rows = azuki_df.shape[0]

with col3:
    st.metric("Azuki: ", total_rows)

############################################################ Pudgy Penguins ########################################################################
col1, col2, col3 = st.columns(3)


pudgy_url = "https://api.reservoir.tools/tokens/ids/v1?collection=0xbd3531da5cf5857e7cfaa92426877b022e612cf8&flagStatus=1&limit=1000"

headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

suspicious_response = requests.get(pudgy_url, headers=headers)

data = suspicious_response.json()

pudgy_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

total_rows = pudgy_df.shape[0]

with col1:
    st.metric("Pudgy Penguins: ", total_rows)

############################################################ Doodles ########################################################################


doodles_url = "https://api.reservoir.tools/tokens/ids/v1?collection=0x8a90cab2b38dba80c64b7734e58ee1db38b8992e&flagStatus=1&limit=1000"

headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

suspicious_response = requests.get(doodles_url, headers=headers)

data = suspicious_response.json()

doodles_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

total_rows = doodles_df.shape[0]

with col2:
    st.metric("Doodles: ", total_rows)

############################################################ CloneX ########################################################################


clone_url = "https://api.reservoir.tools/tokens/ids/v1?collection=0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b&flagStatus=1&limit=1000"

headers = {
    "accept": api_key,
    "x-api-key": "demo-api-key"
}

suspicious_response = requests.get(clone_url, headers=headers)

data = suspicious_response.json()

clone_df = pd.DataFrame(data['tokens'], columns=['Token IDs'])

total_rows = clone_df.shape[0]

with col3:
    st.metric("CloneX: ", total_rows)
