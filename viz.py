import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('시각화 예제')

optionx = None
optiony = None

with st.sidebar:
    file = st.file_uploader('파일 업로드', type=['csv'])

    if file:
        df = pd.read_csv(file)
        # st.dataframe(df)

        st.subheader('컬럼 선택')
        optionx = st.selectbox('x 컬럼 선택', tuple(df.columns))
        optiony = st.selectbox('y 컬럼 선택', tuple(df.columns))

if optionx and optiony:
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(10,6)
    sns.barplot(x=optionx, y=optiony, data=df, ax=ax)
    # sns.barplot(x='class', y='survived', data=df, ax=ax[0, 1])
    # sns.barplot(x='embarked', y='survived', data=df, ax=ax[1, 0])
    # sns.barplot(x='adult_male', y='survived', data=df, ax=ax[1, 1])
    st.pyplot(fig)
    