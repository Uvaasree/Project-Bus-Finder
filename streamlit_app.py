import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    # changing datatype of 'Price' and 'Ratings' columns
    df['Price_clean'] = df['Price'].astype(float)
    df['Ratings_clean'] = pd.to_numeric(df['Ratings'], errors='coerce')
    
    # Clean the 'Seats_Available' column (extracting the number of seats)
    df['Seats_clean'] = df['Seats_Available'].str.extract('(\d+)').astype(int)
    return df

df = load_data('combined.csv')

# Title of the app
st.title('Bus Availability Finder')

# Sidebar filters
st.sidebar.header('Filter Options')

# Filter by route
route_options = ['All Routes'] + sorted(df['Route_name'].unique().tolist())
route = st.sidebar.selectbox('Select Route', route_options)

# Filter by price range
price_min, price_max = st.sidebar.slider(
    'Select Price Range (INR)',
    min_value=int(df['Price_clean'].min()),
    max_value=int(df['Price_clean'].max()),
    value=(int(df['Price_clean'].min()), int(df['Price_clean'].max()))
)

# Filter by minimum rating
ratings_min = st.sidebar.slider(
    'Select Minimum Rating',
    min_value=float(df['Ratings_clean'].min()),
    max_value=float(df['Ratings_clean'].max()),
    value=float(df['Ratings_clean'].min())
)

# Filter by available seats
seats_min = st.sidebar.slider(
    'Select Minimum Available Seats',
    min_value=int(df['Seats_clean'].min()),
    max_value=int(df['Seats_clean'].max()),
    value=int(df['Seats_clean'].min())
)

# Apply filters
filtered_df = df.copy()

if route != 'All Routes':
    filtered_df = filtered_df[filtered_df['Route_name'] == route]

filtered_df = filtered_df[
    (filtered_df['Price_clean'] >= price_min) &
    (filtered_df['Price_clean'] <= price_max) &
    (filtered_df['Ratings_clean'] >= ratings_min) &
    (filtered_df['Seats_clean'] >= seats_min)
]

# Prepare filtered data with selected columns
filtered_df = filtered_df[['Bus_name', 'Bus_type', 'Start_time', 'End_time', 'Total_duration', 'Price_clean', 'Seats_clean', 'Ratings_clean', 'Route_link']].rename(columns={'Price_clean':'Price','Seats_clean':'Seats_available','Ratings_clean':'Ratings'})

# Display results
st.write(f'### {len(filtered_df)} bus(es) found')

# Create hyperlinks for Route_link column
def make_clickable(link):
    return f'<a href="{link}" target="_blank">View Route</a>'

filtered_df['Route_link'] = filtered_df['Route_link'].apply(make_clickable)

# Display filtered dataframe with clickable links
st.markdown(filtered_df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Additional information
st.sidebar.info("🔍 Use the filters to narrow down your search and find the best bus for your route!")
st.sidebar.markdown("[Explore more on our website](#)", unsafe_allow_html=True)
