import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Scholarship_holder, encoder_International, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Gender, encoder_Tuition_fees_up_to_date, encoder_Educational_special_needs, encoder_Displaced
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Students Performance App (Prototype)')

data = pd.DataFrame()
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.classes_, index=0)
    data["Daytime_evening_attendance"] = Daytime_evening_attendance
 
with col2:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=0)
    data["Displaced"] = Displaced
 
with col3:
    Educational_special_needs = st.selectbox(label='Educational_special_needs', options=encoder_Educational_special_needs.classes_, index=0)
    data["Educational_special_needs"] = Educational_special_needs

with col4:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=0)
    data["Debtor"] = Debtor

col1, col2, col3, col4 = st.columns(4)

with col1:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=0)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]

with col2:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=0)
    data["Gender"] = Gender

with col3:
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=0)
    data["Scholarship_holder"] = [Scholarship_holder]

with col4:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=0)
    data["International"] = International

col1, col2, col3 = st.columns(3)

with col1:       
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular_units_1st_sem_credited', value=0))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited

with col2:       
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=0))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col3:       
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=0))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

col1, col2, col3 = st.columns(3)

with col1:       
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=0))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col2:       
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular_units_1st_sem_grade', value=0))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

with col3:       
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations

col1, col2, col3 = st.columns(3)

with col1:       
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=0))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited

with col2:       
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=0))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col3:       
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=0))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

col1, col2, col3 = st.columns(3)

with col1:       
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=0))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col2:       
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular_units_2nd_sem_grade', value=0))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with col3:       
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

col1, col2, col3, col4 = st.columns(4)
 
with col1:       
    Application_order = int(st.number_input(label='Application_order', value=0))
    data["Application_order"] = Application_order
 
with col2:       
    Admission_grade = int(st.number_input(label='Admission_grade', value=111))
    data["Admission_grade"] = Admission_grade

with col3:       
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=23))
    data["Age_at_enrollment"] = Age_at_enrollment

with col4:       
    Unemployment_rate = int(st.number_input(label='Unemployment_rate', value=0))
    data["Unemployment_rate"] = Unemployment_rate

col1, col2, col3 = st.columns(3)

with col1:
    Inflation_rate = int(st.number_input(label='Inflation_rate', value=0))
    data["Inflation_rate"] = Inflation_rate

with col2:
    GDP = int(st.number_input(label='GDP', value=0))
    data["GDP"] = GDP

with col3:
    Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=111))
    data["Previous_qualification_grade"] = Previous_qualification_grade

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Prediction: {}".format(prediction(new_data)))

