import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("static/fatal-police-shootings-data.csv")

# Define the gender types and counts
genders_labels = {
    'male': 'Male',
    'female': 'Female'
}

genders = ['male', 'female']

gender_counts = {}

for gender in genders:
    count = df["gender"].str.count(gender).sum()
    gender_counts[f"{gender}"] = count
gender_counts_df = pd.DataFrame(list(gender_counts.items()),
                                columns=["Gender", "Count"])
gender_counts_df["Gender"] = gender_counts_df["Gender"].map(genders_labels)
gender_figure = px.bar(gender_counts_df, x="Gender", y="Count")
gender_figure.update_xaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))
gender_figure.update_yaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))

# Define the race types and counts
race_labels = {
    'W': 'White',
    'B': 'Black',
    'A': 'Asian heritage',
    'N': 'Native American',
    'H': 'Hispanic',
    'O': 'Other'
}

races = ['W', 'B', 'H', 'A', 'N', 'O']

races_counts = {}

for race in races:
    count = df["race"].str.count(race).sum()
    races_counts[f"{race}"] = count
races_counts_df = pd.DataFrame(list(races_counts.items()),
                               columns=["Race", "Count"])
races_counts_df["Race"] = races_counts_df["Race"].map(race_labels)

races_figure = px.bar(races_counts_df, x="Race", y="Count")
races_figure.update_xaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))
races_figure.update_yaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))

# Defining states/counts
states = ['WA', 'OR', 'KS', 'CA', 'CO', 'OK', 'AZ', 'IA', 'PA', 'TX', 'OH',
          'LA', 'MT', 'UT',
          'AR', 'IL', 'NV', 'NM', 'MN', 'MO', 'VA', 'NJ', 'IN', 'KY', 'MA',
          'NH', 'FL', 'ID',
          'MD', 'NE', 'MI', 'GA', 'TN', 'NC', 'AK', 'NY', 'ME', 'AL', 'MS',
          'WI', 'SC', 'DE',
          'DC', 'WV', 'HI', 'WY', 'ND', 'CT', 'SD', 'VT', 'RI']

state_counts = {}

for state in states:
    count = df['state'].str.count(state).sum()
    state_counts[f"{state}"] = count
state_counts_df = pd.DataFrame(list(state_counts.items()),
                               columns=["State", 'Count'])
state_counts_df = state_counts_df.sort_values(by="Count", ascending=False)

state_figure = px.bar(state_counts_df, x='State', y='Count')
state_figure.update_xaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))
state_figure.update_yaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))

# Mental Illness
mental = [False, True]
mental_count = {}

for m in mental:
    count = (df['was_mental_illness_related'] == m).sum()
    label = "Affected by Mental Illness" if m else "Not Affected by Mental Illness"
    mental_count[label] = count
mental_count_df = pd.DataFrame(list(mental_count.items()),
                               columns=["Mental illness", 'Count'])

mental_figure = px.bar(mental_count_df, x='Mental illness', y='Count')
mental_figure.update_xaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))
mental_figure.update_yaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))

# Define the threat types and counts
threats = ["shoot", "threat", "point", "attack", "move", "undetermined",
           "flee", "accident"]

threat_counts = {}

for threat in threats:
    count = df["threat_type"].str.count(threat).sum()
    threat_counts[f"{threat}"] = count

threat_counts_df = pd.DataFrame(list(threat_counts.items()),
                                columns=["Threat Type", "Count"])
threat_counts_df["Threat Type"] = threat_counts_df[
    "Threat Type"].str.capitalize()

threat_figure = px.bar(threat_counts_df, x="Threat Type", y="Count")
threat_figure.update_xaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))
threat_figure.update_yaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))

# Define the armed types and counts
armed_with_labels = {
    'gun': 'Gun',
    'unarmed': 'Unarmed',
    'replica': 'Replica',
    'other': 'Other',
    'knife': 'Knife',
    'vehicle': 'Vehicle',
    'undetermined': 'Undetermined',
    'unknown': 'Unknown',
    'blunt_object': 'Blunt Object',
    'gun;knife': 'Gun and Knife',
    'vehicle;gun': 'Vehicle and Gun',
    'gun;vehicle': 'Gun and Vehicle',
}

armed_with = ['gun', 'knife', 'unarmed', 'vehicle', 'undetermined', 'replica',
              'blunt_object', 'unknown', 'other', 'gun;vehicle',
              'gun;knife', 'vehicle;gun']

armed_with_counts = {}

for arm in armed_with:
    count = df["armed_with"].str.count(arm).sum()
    armed_with_counts[f"{arm}"] = count
armed_with_counts_df = pd.DataFrame(list(armed_with_counts.items()),
                                    columns=["Armed With", "Count"])
armed_with_counts_df["Armed With"] = armed_with_counts_df["Armed With"].map(
    armed_with_labels)

armed_with_figure = px.bar(armed_with_counts_df, x="Armed With", y="Count")
armed_with_figure.update_xaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))
armed_with_figure.update_yaxes(tickfont=dict(size=14, color='black'), title_font=dict(size=20, color='black'))

st.set_page_config(initial_sidebar_state='expanded', layout="wide")

st.title("A breakdown of police-involved fatalities in the United States since 2015")

st.markdown('<hr style="border: 2px solid #ff5733;">', unsafe_allow_html=True)

st.subheader("Gender:")
st.text("Distribution of genders that the fatalities affected.")
st.plotly_chart(gender_figure)
st.markdown('<hr style="border: 0.5px solid #000000;">', unsafe_allow_html=True)

st.subheader("Race:")
st.text("Distribution of races that the fatalities affected.")
st.plotly_chart(races_figure)
st.markdown('<hr style="border: 0.5px solid #000000;">', unsafe_allow_html=True)

st.subheader("State:")
st.text("Distribution of states where fatalities occurred.")
st.plotly_chart(state_figure)
st.markdown('<hr style="border: 0.5px solid #000000;">', unsafe_allow_html=True)

st.subheader("Mental Illness:")
st.text("Distribution of victims that were affected with mental illness.")
st.plotly_chart(mental_figure)
st.markdown('<hr style="border: 0.5px solid #000000;">', unsafe_allow_html=True)

st.subheader("Threat Type:")
st.text("Actions the victim took leading up to the fatality.")
st.plotly_chart(threat_figure)
st.markdown('<hr style="border: 0.5px solid #000000;">', unsafe_allow_html=True)

st.subheader("Armament Types:")
st.text(
    "What, if anything, was the victim armed with leading up to the fatality.")
st.plotly_chart(armed_with_figure)
st.markdown('<hr style="border: 0.5px solid #000000;">', unsafe_allow_html=True)

st.divider()
st.text("Disclaimer: Some minor outliers have been omitted from the graphs.")
st.text("For the complete and comprehensive list, please refer to The Data "
        "tables.")
st.divider()
