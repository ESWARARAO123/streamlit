import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
st.title("cal")
st.write("## input data")
col1,col2=st.columns(2)
home_val=col1.number_input("Home_val",min_value=0,value=500000)
deposit=col1.number_input("Deposit",min_value=0,value=100000)
int_rate=col2.number_input("Interesr Rate (in %)",min_value=0.0,value=5.5)
loan_term=col2.number_input("Loan term(in years)",min_value=1,value=30)
loan_amount=home_val-deposit
mon_int_rate=(int_rate/100)/12
no_of_payments=loan_term*12
monthly_payment=(loan_amount*(mon_int_rate*(1+mon_int_rate)** no_of_payments)/((1+mon_int_rate)**no_of_payments-1))
total_pay=monthly_payment*no_of_payments
total_int=total_pay-loan_amount
st.write("## Repayments")
col1,col2,col3=st.columns(3)
col1.metric(label="monthly repayment", value=f"${monthly_payment:,.2f}")
col2.metric(label="total repayment", value=f"${total_pay:,.0f}")
col3.metric(label="total intrest", value=f"${total_int:,.0f}")

schedule=[]
rem_bal=loan_amount
for i in range(1,no_of_payments+1):
    int_pay=rem_bal*mon_int_rate
    pri_pay=monthly_payment-int_pay
    rem_bal-=pri_pay
    year=math.ceil(i/12)
    schedule.append(
        [i,monthly_payment,pri_pay,int_pay,rem_bal,year]
    )
df=pd.DataFrame(schedule,columns=["month","payment",'principle','intrest','rem bal','year'])
st.write("## payment schedule")
pay_df=df[["year","rem bal"]].groupby("year").min()
st.line_chart(pay_df)