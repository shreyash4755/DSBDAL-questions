import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Swine Flu Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df.rename(columns={
        "Country": "Country/Region",
        "Cumulative no. of cases": "Confirmed",
        "Cumulative no. of deaths": "Deaths"
    }, inplace=True)
    return df

df = load_data()

# Sidebar
st.sidebar.title("Swine Flu Dashboard")
selected_country = st.sidebar.selectbox("Select a Country", sorted(df["Country/Region"].unique()))
start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

# Filter and group
country_df = df[df["Country/Region"] == selected_country]
country_df = country_df.groupby("Date")[["Confirmed", "Deaths"]].sum()
country_df = country_df[(country_df.index >= pd.to_datetime(start_date)) & (country_df.index <= pd.to_datetime(end_date))]

# Title
st.title(f"Swine Flu Trends in {selected_country}")

# Trend
st.subheader("Trend of Confirmed and Deaths")
st.line_chart(country_df)

# Daily new cases
st.subheader("Daily New Confirmed Cases")
country_df["Daily Confirmed"] = country_df["Confirmed"].diff().fillna(0)
st.bar_chart(country_df["Daily Confirmed"])

# Latest stats
latest = country_df.iloc[-1]
confirmed, deaths = latest["Confirmed"], latest["Deaths"]
mortality_rate = (deaths / confirmed) * 100 if confirmed else 0

st.subheader("Latest Statistics")
st.metric("Total Confirmed", int(confirmed))
st.metric("Total Deaths", int(deaths))
st.metric("Mortality Rate (%)", f"{mortality_rate:.2f}")

# Global Summary
st.title("🌐 Global Swine Flu Summary")
latest_date = df["Date"].max()
latest_df = df[df["Date"] == latest_date]
global_summary = latest_df.groupby("Country/Region")[["Confirmed", "Deaths"]].sum()

col1, col2 = st.columns(2)
col1.metric("🌍 Total Confirmed", int(global_summary["Confirmed"].sum()))
col2.metric("⚰️ Total Deaths", int(global_summary["Deaths"].sum()))

# Top 10 countries
st.subheader("📊 Top 10 Countries by Confirmed Cases")
top10 = global_summary.sort_values("Confirmed", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 5))
top10[["Confirmed", "Deaths"]].plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.title("Top 10 Countries - Confirmed & Deaths")
st.pyplot(fig)

# Mortality rate over time
st.subheader("📉 Mortality Rate Over Time")
country_df["Mortality Rate (%)"] = (country_df["Deaths"] / country_df["Confirmed"]).replace([float("inf"), -float("inf")], 0).fillna(0) * 100
st.line_chart(country_df[["Mortality Rate (%)"]])

# Pie chart
st.subheader(f"🥧 Case Distribution in {selected_country}")
active = confirmed - deaths
labels = ["Active", "Deaths"]
sizes = [active, deaths]
fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Case Distribution")
st.pyplot(fig2)

# Comparison
st.subheader("🆚 Compare Two Countries")
colA, colB = st.columns(2)
with colA:
    country1 = st.selectbox("First Country", df["Country/Region"].unique(), index=0)
with colB:
    country2 = st.selectbox("Second Country", [c for c in df["Country/Region"].unique() if c != country1], index=0)

def get_country_data(country):
    return df[df["Country/Region"] == country].groupby("Date")[["Confirmed"]].sum()

c1_df = get_country_data(country1)
c2_df = get_country_data(country2)

st.line_chart(pd.DataFrame({
    f"{country1} Confirmed": c1_df["Confirmed"],
    f"{country2} Confirmed": c2_df["Confirmed"]
}))

# Map
st.subheader("🌍 Global Confirmed Swine Flu Cases Map")
fig = px.choropleth(latest_df, locations="Country/Region",
                    locationmode="country names",
                    color="Confirmed",
                    color_continuous_scale="Oranges",
                    title="Global Swine Flu Cases")
st.plotly_chart(fig)
