import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit超入門')

st.write('progress bar')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

left_column, right_colmun = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_colmun.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text, 'です'

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション', condition


# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', option, 'です'


# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='XXX', use_column_width=True)




# st.write('DataFrame')

# #新宿付近（経度35,69、緯度139.70付近）のmapplot
# df = pd.DataFrame(
#     [35.69, 139.70] + np.random.rand(100,2)/[50,50],
#     columns=['lat','lon'])

# st.map(df)






# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# ) 

# st.line_chart(df)




# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

#st.dataframe(df.style.highlight_max(axis=0),width=500, height=500)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """