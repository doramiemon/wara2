import streamlit as st
from PIL import Image 

x = 6  #←問題数の合計を入力！　問題が増えたら、変更を！

st.title("問題一覧")

for n in range(1,x+1):
    image = Image.open('./data/q'+str(n)+'.png')
    st.image(image, caption='問題'+str(n),use_column_width=True)

    image2 = Image.open('./data/a'+str(n)+'.png')
    expander = st.expander('解答'+str(n))
    expander.image(image2,use_column_width=True)


