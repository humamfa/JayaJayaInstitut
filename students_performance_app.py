import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Scholarship_holder, encoder_International, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Gender, encoder_Tuition_fees_up_to_date, encoder_Educational_special_needs, encoder_Displaced
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://png.pngtree.com/png-vector/20211120/ourmid/pngtree-university-logo-png-image_4037518.png", width=55)
with col2:
    st.header('Students Performance App (Prototype)')

data = pd.DataFrame()

st.subheader("Student's status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    Tuition_fees_up_to_date = st.selectbox(label='Paid tuition fees', options=['No', 'Yes'], index=0)
    if Tuition_fees_up_to_date == ['No']:
        data["Tuition_fees_up_to_date"] = [0]
    else:
        data["Tuition_fees_up_to_date"] = [1]

with col2:
    Gender = st.selectbox(label='Gender', options=['Female', 'Male'], index=0)
    if Tuition_fees_up_to_date == ['Female']:
        data["Gender"] = [0]
    else:
        data["Gender"] = [1]

with col3:
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=['No', 'Yes'], index=0)
    if Scholarship_holder == ['No']:
        data["Scholarship_holder"] = [0]
    else:
        data["Scholarship_holder"] = [1]

with col4:
    International = st.selectbox(label='International student', options=['No', 'Yes'], index=0)
    if International == ['No']:
        data["International"] = [0]
    else:
        data["International"] = [1]

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Daytime_evening_attendance = st.selectbox(label='Daytime/evening attendance', options=['No', 'Yes'], index=0)
    if International == ['No']:
        data["Daytime_evening_attendance"] = [0]
    else:
        data["Daytime_evening_attendance"] = [1]
 
with col2:
    Displaced = st.selectbox(label='Displaced student', options=['No', 'Yes'], index=0)
    if International == ['No']:
        data["Displaced"] = [0]
    else:
        data["Displaced"] = [1]
 
with col3:
    Educational_special_needs = st.selectbox(label='Educational special needs', options=['No', 'Yes'], index=0)
    if International == ['No']:
        data["Educational_special_needs"] = [0]
    else:
        data["Educational_special_needs"] = [1]

with col4:
    Debtor = st.selectbox(label='Debtor', options=['No', 'Yes'], index=0)
    if International == ['No']:
        data["Debtor"] = [0]
    else:
        data["Debtor"] = [1]

st.subheader("Student's enrollment")

col1, col2, col3, col4 = st.columns(4)

with col1:       
    Application_order = int(st.number_input(label='Application order', value=0))
    data["Application_order"] = Application_order
 
with col2:       
    Admission_grade = float(st.number_input(label='Admission grade', value=111))
    data["Admission_grade"] = Admission_grade

with col3:       
    Age_at_enrollment = int(st.number_input(label='Age at enrollment', value=23))
    data["Age_at_enrollment"] = Age_at_enrollment

with col4:
    Previous_qualification_grade = float(st.number_input(label='Previous qualification grade', value=111))
    data["Previous_qualification_grade"] = Previous_qualification_grade

st.subheader("1st semester curricular units")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:       
    Curricular_units_1st_sem_credited = int(st.number_input(label='Credited', value=0))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited

with col2:       
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Enrolled', value=0))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col3:       
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Evaluated', value=0))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

with col4:       
    Curricular_units_1st_sem_approved = int(st.number_input(label='Approved', value=0))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col5:       
    Curricular_units_1st_sem_grade = float(st.number_input(label='Grade', value=0))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

with col6:       
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Not evaluated', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations

st.subheader("2nd semester curricular units")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:       
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Credited', value=0, key=2))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited

with col2:       
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Enrolled', value=0, key=3))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col3:       
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Evaluated', value=0, key=4))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

with col4:       
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Approved', value=0, key=5))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col5:       
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Grade', value=0, key=6))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with col6:       
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Not evaluated', value=0, key=7))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

st.subheader("Others")

col1, col2, col3 = st.columns(3)

with col1:
    Inflation_rate = float(st.number_input(label='Inflation rate', value=0))
    data["Inflation_rate"] = Inflation_rate

with col2:
    GDP = float(st.number_input(label='GDP', value=0))
    data["GDP"] = GDP

with col3:       
    Unemployment_rate = float(st.number_input(label='Unemployment rate', value=0))
    data["Unemployment_rate"] = Unemployment_rate

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Prediction: {}".format(prediction(new_data)))
