import streamlit as st
from PIL import Image 
import random
import time

x = 20  #←問題数の合計を入力！　問題が増えたら、変更を！
mondai_su = 8 #出題する問題数を入力！
zikan = 900 # 制限時間を秒換算で入力！

st.title("積分タイムアタック")
st.write('問題数は、８題で、制限時間は、15分です。最後の問題のあとに、残りの制限時間が表示されています。')

@st.cache
def generate_random_list():
    return random.sample(range(1, x+1), mondai_su)

numbers = generate_random_list()


for n in range(0,mondai_su):
    image = Image.open('./data/q'+str(numbers[n])+'.png')
    st.image(image, caption='問題'+str(numbers[n]),use_column_width=True)



time_left = st.empty()
stop_button = st.button('解き終えた')

# 分のタイマー（1秒ごとに更新）
for i in range(900, -1, -1):
    if stop_button:
        st.write('解答を表示します')
        st.balloons()
        break

    m, s = divmod(i, 60)
    time_left.text(f'残り時間: {m:02d}:{s:02d}')
    time.sleep(1)

if not stop_button:
    st.write('時間切れ！')
    
for n in range(0,mondai_su):
    image2 = Image.open('./data/a'+str(numbers[n])+'.png')
    expander = st.expander('解答'+str(numbers[n]))
    expander.image(image2,use_column_width=True)

""""
システム上、一日に一回問題が入れ替わります。
"""
