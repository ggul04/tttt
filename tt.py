import matplotlib.pyplot as plt
import streamlit as st
fig,ax= plt.subplots()

c1= st.sidebar.radio('선의 색 선택',['red','blue'])
c2= st.sidebar.radio('선의 스타일 선택',[':','-'])
c3= st.sidebar.radio('마커의 스타일 선택',['p','s'])

a= []
b= []
for i in range(-20,21,3):
    a.append(i)
    b.append(-2*i*i+3*1+5)

plt.plot(a,b,color=c1, linestyle= c2, marker=c3)

st.pyplot(fig)
import sys
sys.exit()
