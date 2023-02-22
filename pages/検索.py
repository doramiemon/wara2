import streamlit as st
from PIL import Image 

x = 20    #←問題数の合計を入力！　問題が増えたら、変更を！

k = st.selectbox('問題番号?',
    list(range(1,x+1)))

image = Image.open('./data/q'+str(k)+'.png')
st.image(image, caption='問題'+str(k),use_column_width=True)

image2 = Image.open('./data/a'+str(k)+'.png')
expander = st.expander('解答'+str(k))
expander.image(image2,use_column_width=True)

