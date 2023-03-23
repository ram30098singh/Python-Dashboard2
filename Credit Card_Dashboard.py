#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


# In[46]:


st.set_page_config(page_title="Dashboard",
                  page_icon="bar_chart:",
                  layout="wide")


# In[47]:


data=pd.read_csv("C:/Users/Dell/Desktop/Dataset/RAC_Datset.csv")
data.shape


# In[48]:


import random
random.seed(35043)
df = data.sample(n=1000, random_state=35043)
df.head()


# In[49]:


df.shape


# In[50]:


df.isnull().sum()


# In[51]:


st.sidebar.header('Please Filter Here:')

Customer_Status = st.sidebar.multiselect(
    "Select the Customer Status:",
    options=df["Customer_Status"].unique(),
    default=df["Customer_Status"].unique())

Gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique())

Marital_Status = st.sidebar.multiselect(
    "Select the Marital Status:",
    options=df["Marital_Status"].unique(),
    default=df["Marital_Status"].unique())

Card_Category = st.sidebar.multiselect(
    "Select the Card Category:",
    options=df["Card_Category"].unique(),
    default=df["Card_Category"].unique())

Income_Category = st.sidebar.multiselect(
    "Select the Income Category:",
    options=df["Income_Category"].unique(),
    default=df["Income_Category"].unique())

Education_Level = st.sidebar.multiselect(
    "Select the Education Level:",
    options=df["Education_Level"].unique(),
    default=df["Education_Level"].unique())

df_selection = df.query(
    "Customer_Status ==@Customer_Status & Gender ==@Gender & Marital_Status ==@Marital_Status & Card_Category ==@Card_Category & Income_Category ==@Income_Category & Education_Level ==@Education_Level") 
st.dataframe(df_selection)


# In[52]:


st.title('Dashboard')
st.markdown('##')
Total_Yearly_Transaction_Amount= int(df_selection['Yearly_Transaction_Amount'].sum())
Total_Credit_Limit= int(df_selection['Credit_Limit'].sum())


# In[53]:


left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader('Total Credit Limit')
    st.subheader(f' {Total_Credit_Limit:,}')

with right_column:
    st.subheader('Total Yearly Transaction Amount')
    st.subheader(f' {Total_Yearly_Transaction_Amount:,}')
st.markdown("---")


# In[54]:


v1 = df_selection.groupby(by=['Customer_Status']).sum()[['Credit_Limit']].sort_values(by=['Credit_Limit'])
fig1 = px.bar(
    v1,
    x='Credit_Limit', y = v1.index,
    orientation='h', title="<b> Total Credit Limit of Customer </b>",
    color_discrete_sequence=["#0083B8"]* len(v1),
    template="plotly_white",)

v2 = df_selection.groupby(by=['Customer_Status']).sum()[['Yearly_Transaction_Amount']].sort_values(by=['Yearly_Transaction_Amount'])
fig2 = px.bar(
    v2,
    x='Yearly_Transaction_Amount', y = v2.index,
    orientation='h', title="<b> Total Credit Limit of Customer </b>",
    color_discrete_sequence=["#9903B8"]* len(v2),
    template="plotly_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)


# In[55]:


Pie_chart1= px.pie(df_selection, title='Card used on months', values='Months_on_Use', names='Card_Category')
Pie_chart2= px.pie(df_selection, title='Card Credit Limit', values='Credit_Limit', names='Card_Category')
left_column, right_column = st.columns(2)
left_column.plotly_chart(Pie_chart1, use_container_width=True)
right_column.plotly_chart(Pie_chart2, use_container_width=True)


# In[56]:


bar_chart1=px.bar(df_selection, x="Customer_Status", y="Total_Transactions", color="Card_Category", title="Total transaction by customer with different cards")
bar_chart2=px.bar(df_selection, x="Income_Category", y="Total_Transactions", color="Card_Category", title="Total transaction by Income category with different cards")
left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart1, use_container_width=True)
right_column.plotly_chart(bar_chart2, use_container_width=True)


# In[57]:


v3 = df_selection.groupby(by=['Marital_Status']).sum()[['Total_Transactions']].sort_values(by=['Total_Transactions'])
fig3 = px.bar(
    v3,
    x='Total_Transactions', y = v3.index,
    orientation='h', title="<b> Total Transactions by Marital Status </b>",
    color_discrete_sequence=["#2993B8"]* len(v3),
    template="plotly_white",)

v4 = df_selection.groupby(by=['Education_Level']).sum()[['Total_Transactions']].sort_values(by=['Total_Transactions'])
fig4 = px.bar(
    v4,
    x='Total_Transactions', y = v4.index,
    orientation='h', title="<b> Total Transactions by Education Level </b>",
    color_discrete_sequence=["#6683B8"]* len(v4),
    template="plotly_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig3, use_container_width=True)
right_column.plotly_chart(fig4, use_container_width=True)


# In[58]:


bar_chart3=px.bar(df_selection, x="Education_Level", y="Yearly_Average_Balance", color="Card_Category", title="Yearly Average Balance with Card & Education category")
bar_chart4=px.bar(df_selection, x="Income_Category", y="Yearly_Transaction_Amount", color="Marital_Status", title="Yearly Transaction Amount with Income & Marital category")
left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart3, use_container_width=True)
right_column.plotly_chart(bar_chart4, use_container_width=True)


# In[62]:


st.title('Statistical Analysis')
st.markdown('##')


# In[59]:


b1 = px.box(df_selection, x="Customer_Status", y="Yearly_Transaction_Amount")
b2 = px.box(df_selection, x="Card_Category", y="Total_Transactions")
left_column, right_column = st.columns(2)
left_column.plotly_chart(b1, use_container_width=True)
right_column.plotly_chart(b2, use_container_width=True)


# In[60]:


hide_st_style = """
            <style>
            #mainMenu {Visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


# In[ ]:




