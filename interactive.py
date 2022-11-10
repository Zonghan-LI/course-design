from sqlite3 import Row
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import random
import plotly.figure_factory as ff
import mpld3
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image
import altair as alt
from bokeh.plotting import figure
import time



# input_data = pd.read_csv("urt/clean_test.csv")
# target_data = pd.read_csv("urt/transformer.csv")
df = pd.read_csv("clean_test.csv", delimiter = ',',index_col=0)
df["ls"] = df.iloc[:,0:2].values.tolist()
# s = str(df["ls"])
# s = s.replace(',' , '') #name + description
df2 = pd.read_csv("transformer.csv", delimiter = ',',index_col=0)
df["trans"] = df2.iloc[:,0:2].values.tolist()
# t = str(df["trans"]) #label

st.write('Welcome to my application')
st.write(st.__version__)

def main():
    pd.options.display.float_format = '{:20,.2f}'.format
    st.title(" 应用类型识别挑战赛")
    TITLE_1 = 'Part I. 数据集介绍 '
    TITLE_2 = 'Part II. 可视化 '
    TITLE_3 = 'Part III. 交互界面'
    # TITLE_4 = 'Part IV. The Map'

    option = st.sidebar.selectbox('Table of Contents', (
        TITLE_1,
        TITLE_2,
        TITLE_3,
    ))

    if (option == TITLE_1):
        head1 = df.head()
        head2 = df2.head()
        st.markdown(f'## {TITLE_1}\n**项目背景简介.** ')
        st.markdown('应用类型的识别是分析开发者使用场景和行业使用场景的关键步骤，随着应用数量的不断增多， \
            如何快速精准的识别应用类型成为亟待突破的关键性问题。')

        st.markdown('应用类型的识别需要强大的数据作为支撑，本次大赛提供了讯飞开放平台海量的应用名称和应用描述数据作为训练样本， \
            参赛选手需要基于提供的样本构建模型，预测应用的相关类别。')
            
        st.write('Below is our clean dataset:', head1)
        st.write('Below is our transformer dataset:', head2)
        
    elif (option == TITLE_2):
        def count_rows(rows):
            return len(rows)
        st.markdown('**我们分别用饼图,柱状图,线图展示标签数量**')
        genres = ['Line_graph','Bar_chart','Pie_graph']
        genre = st.radio('Type of the Plot',genres)

        if (genre  == 'Line_graph'):
            st.markdown('**通过线图展现出不同标签之间的差异性**')
            fig = plt.figure()
            by_lab = df2.groupby('label').apply(count_rows)
            x = by_lab

            plt.plot(
                    x ,
                    linestyle = '-', 
                    linewidth = 2, 
                    color = 'steelblue', 
                    marker = 'o', 
                    markersize = 6, 
                    markeredgecolor='orange', 
                    markerfacecolor='steelblue', 
                    label='number of FLAG'#标签
                    )

            plt.title('Total number of OBS_FLAG with line graph')
            plt.xlabel('label')
            plt.ylabel('Total number ')
            plt.xticks(rotation = -60)
            plt.yticks(rotation = -60)

            plt.legend(loc='best',frameon=False)#图例，显示label，去掉边框
            st.pyplot(fig)



        elif (genre  == 'Bar_chart'):
            st.markdown("**我们可以通过柱状图直观的看出每一个标签的数量分类**")
            by_cat = df2.groupby('label').apply(count_rows)
            st.header('Count of name')
            st.bar_chart(by_cat)

            

        
        elif (genre  == 'Pie_graph'):
            fig1 = plt.figure(figsize=(20,20))  
            x1 = df2['label'].value_counts()['14726332 14728344 14854542 14844591']
            x2 = df2['label'].value_counts()['14782903 15634620 15638402 15706300']
            x3 = df2['label'].value_counts()['15632285 15706536 14721977 14925219']
            x4 = df2['label'].value_counts()['14786237 15697082 14722731 14924977']
            
            st.markdown ('**现在我们通过饼图展现出前4位占比最高的标签**')

            labels = '14726332', '14782903', '156322859', '14786237'
            sizes = [x1, x2, x3, x4]
            explode = (0, 0, 0, 0) 
           

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
            #x1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            fig_html = mpld3.fig_to_html(fig1)
            components.html(fig_html, height=600)
            




    elif (option == TITLE_3):
        st.markdown(
            f'## {TITLE_3}\n**Interactive**')
        head3 = df["ls"].head()
        head4 = df["trans"].head()
        st.write('我们从以下表格中挑选一组数据：', head3)
        st.write('我们需要找到对应的标签数据：',head4)
        # print(df.head())
        option = st.selectbox(
        '请选择一组数据',
        (df["ls"]))
        content = option[0] + " " + option[1]
        id = df[df["Train_info"] == content].index[0]
        label = df2['label'].loc[id]
        # print(label)
        # st.write('对应的标签是：',label)
        st.write('以下是你选择的数据:', option)
        st.write('返回的输出结果是:', label)



           



#print(t)
#print(df["ld"])
#print(df2)
if __name__ == "__main__":
    main()