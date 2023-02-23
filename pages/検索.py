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

zettai = [3, 12]
tikan = [4, 5, 8, 11, 13, 16]
bubun = [7, 10, 18]

genre = st.radio(
    "解法で調べる",
    ('絶対値付き', '置換積分', '部分積分'))

if genre == '絶対値付き':
    for n in range(len(zettai)):
        image = Image.open('./data/q'+str(zettai[n])+'.png')
        st.image(image, caption='問題'+str(zettai[n]),use_column_width=True)

        image2 = Image.open('./data/a'+str(zettai[n])+'.png')
        expander = st.expander('解答'+str(zettai[n]))
        expander.image(image2,use_column_width=True)
    
elif genre == '置換積分':
    for n in range(len(tikan)):
        image = Image.open('./data/q'+str(tikan[n])+'.png')
        st.image(image, caption='問題'+str(tikan[n]),use_column_width=True)

        image2 = Image.open('./data/a'+str(tikan[n])+'.png')
        expander = st.expander('解答'+str(tikan[n]))
        expander.image(image2,use_column_width=True)
    
else:
    for n in range(len(bubun)):
        image = Image.open('./data/q'+str(bubun[n])+'.png')
        st.image(image, caption='問題'+str(bubun[n]),use_column_width=True)

        image2 = Image.open('./data/a'+str(bubun[n])+'.png')
        expander = st.expander('解答'+str(bubun[n]))
        expander.image(image2,use_column_width=True)