import streamlit as st

st.set_page_config(page_title="Purplle Store Intelligence")

st.title("🛍️ Purplle Store Intelligence Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Visitors", 132)

with col2:
    st.metric("Queue Length", 4)

with col3:
    st.metric("Billing Area", 2)

st.success("Store running normally")

st.subheader("Insights")

st.write("• Peak visitors detected at 6 PM")
st.write("• Queue length remained below threshold")
st.write("• No anomaly detected")