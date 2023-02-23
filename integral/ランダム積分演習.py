import streamlit as st
import random
from PIL import Image 

x = 20    # ←問題数の合計を入力！　問題が増えたら、変更を！

st.title("積分ランダム演習")

button = st.button('積分を出題しますか？')
if button: 
    n = str(random.randint(1,x))
    image = Image.open('./data/q'+n+'.png')
    st.image(image, caption='問題'+n,use_column_width=True)

    image2 = Image.open('./data/a'+n+'.png')
    expander = st.expander('解答'+n)
    expander.image(image2,use_column_width=True)

"""
## このページでは、ランダムで無限に積分の問題を演習することができます！
### Focus Goldの定積分の例題を、ランダムに掲載しました。
"""

