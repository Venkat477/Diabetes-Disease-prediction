# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 01:40:31 2020
@author: Venkata N Divi
"""
import sys,streamlit as st,pickle

def selectOptions():
    try:
        mlModel = open('DiabetesPredictionSVM.pkl','rb')
        svmModel_ = pickle.load(mlModel)
        pregnancies_ = st.text_input("No. of Pregnancies (Enter only numbers)*")
        glucose_ = st.text_input("Glucose (Enter only numbers)*")
        bp_ = st.text_input("Blood Pressure (Enter only numbers)*")
        skinThinkness_ = st.text_input("Skin Thickness (Enter only numbers)*")
        insulin_ = st.text_input("Insulin (Enter only numbers)*")
        BMI_ = st.text_input("Body Mass Index(BMI) (Enter only numbers)*")
        diabetesPedigreeFunction_ = st.text_input("Diabetes Pedigree Function (Enter only numbers)*")
        age_ = st.text_input("Age (Enter only numbers)*")
        
        if st.button('Predict Diabetes'):
            if pregnancies_ and glucose_ and bp_ and skinThinkness_ and insulin_ and BMI_ and diabetesPedigreeFunction_ and age_:
                data = [[pregnancies_,glucose_,bp_,skinThinkness_,insulin_,BMI_,diabetesPedigreeFunction_,age_]]
                myPred = svmModel_.predict(data)
                if myPred == 1:
                    st.success('Congrats!!! You don\'t have Diabetes')
                else:
                    st.error('Sorry!!! You have Diabetes, Please consult a Doctor')
            else:
                st.warning('Please enter all the details!!!')
    except Exception as e:
        st.warning('Please check and enter all the details properly!!!')
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno),Exception, e)
        
def main():
    try:
        selectOptions()
    except Exception as e:
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno),Exception, e)
    
if __name__ == '__main__':
    st.write('<!DOCTYPE html><html lang="en">   <head>      <meta charset="UTF-8">      <meta name="viewport" content="width=device-width, initial-scale=1.0">      <meta http-equiv="X-UA-Compatible" content="ie=edge">      <title>Responsive Navigation Bar - W3jar.Com</title>      <style>*,*::before,*::after {  box-sizing: border-box;  -webkit-box-sizing: border-box;}body {  font-family: sans-serif;  margin: 0;  padding: 0;}.container {  height: 80px;  background-color: #052252;  display: -webkit-box;  display: -ms-flexbox;  display: flex;  -ms-flex-wrap: wrap;  flex-wrap: wrap;  -webkit-box-align: center;  -ms-flex-align: center;  align-items: center;  overflow: hidden;}.container .logo {  max-width: 250px;  padding: 0 10px;  overflow: hidden;}.container .logo a {  display: -webkit-box;  display: -ms-flexbox;  display: flex;  -ms-flex-wrap: wrap;  flex-wrap: wrap;  -webkit-box-align: center;  -ms-flex-align: center;  align-items: center;  height: 60px;}.container .logo a img {  max-width: 100%;  max-height: 60px;}@media only screen and (max-width: 650px) {  .container {    -webkit-box-pack: justify;    -ms-flex-pack: justify;    justify-content: space-between;  }  .container .logo {    -webkit-box-flex: 1;    -ms-flex: 1;    flex: 1;  }}.body {  max-width: 700px;  margin: 0 auto;  padding: 10px;} .h1 { color:#FEFEFE; position: center; top: 10px; font-size:135px;font-family:verdana;    margin-top:0px;    margin:0px; line-height:50px; }</style>   </head>   <body>      <div class="container">      <div class="logo">    <a href="#"><img src="https://www.advancells.com/wp-content/uploads/2020/06/diabetes.png" alt="logo"></a>    </div> </body></html>', unsafe_allow_html=True)
    st.title("Diabetes Disease Prediction")
    st.markdown("You want to check whether you have Diabetes or not !!!")
    st.markdown("It's always suggestible to go to a Diagnostic Center and have a check, but before as a preliminary analysis you can use our service !!!")
    main()