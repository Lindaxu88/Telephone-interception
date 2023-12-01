import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import plotly.express as px

os.getcwd()
df = pd.read_csv(f"data/rec.csv")

#Data Cleaning
# print(df.isnull().any())
tmp = df.isnull().mean()
print("Missing value ratio : %s" %tmp)
df.dropna(axis=0, how='any')
print(any(df.duplicated()))
df.drop_duplicates(inplace=True)
# df.to_csv(f"data/rec.csv")

# ## Data Distribution Visualization
plt.hist(df["maxl"], 10000)
plt.savefig(f"Distribution_Visualization/maxl_Hist.png")
plt.hist(df["avgl"], 10000)
plt.savefig(f"Distribution_Visualization/avgl_Hist.png")

plt.plot(df["maxl"], "r", linewidth=1, label="maxl")
plt.plot(df["avgl"], "b", linewidth=1, label="avgl")
plt.legend(loc="upper right", fontsize=14)
plt.xlabel("Training set size", fontsize=14)
plt.ylabel("accn", fontsize=14)
plt.axis([0, 10000, 0, 800])
plt.xticks(np.arange(0, 10000, step=1000))
plt.yticks(np.arange(0, 800, step=80))
plt.title("accn_Comparison")
plt.savefig(f"Distribution_Visualization/accn.png")
#
df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1,2,3,4])
df_pie['Category'] = ["type1","type2","type3","type4","type5"]
df_pie['Category_number'] = [0,0,0,0,0]
for i in range(len(df["ind"])):
    if df["ind"][i] == "type1":
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    elif df["ind"][i] == "type2":
        df_pie['Category_number'][1]=df_pie['Category_number'][1]+1
    elif df["ind"][i] == "type3":
        df_pie['Category_number'][2] = df_pie['Category_number'][2] + 1
    elif df["ind"][i] == "type4":
        df_pie['Category_number'][3] = df_pie['Category_number'][3] + 1
    else:
        df_pie['Category_number'][4] = df_pie['Category_number'][4] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "ind")
fig.update_layout(showlegend = True,
        title = {'text': "ind",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/ind_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1,2,3,4])
df_pie['Category'] = ["type1","type2","type3","type4","type5"]
df_pie['Category_number'] = [0,0,0,0,0]
for i in range(len(df["blcl"])):
    if df["catl"][i] == "type1":
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    elif df["catl"][i] == "type2":
        df_pie['Category_number'][1]=df_pie['Category_number'][1]+1
    elif df["catl"][i] == "type3":
        df_pie['Category_number'][2] = df_pie['Category_number'][2] + 1
    elif df["catl"][i] == "type4":
        df_pie['Category_number'][3] = df_pie['Category_number'][3] + 1
    else:
        df_pie['Category_number'][4] = df_pie['Category_number'][4] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "catl")
fig.update_layout(showlegend = True,
        title = {'text': "ind",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/catl_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1,2,3,4])
df_pie['Category'] = ["type1","type2","type3","type4","type5"]
df_pie['Category_number'] = [0,0,0,0,0]
for i in range(len(df["blcl"])):
    if df["blcl"][i] == "type1":
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    elif df["blcl"][i] == "type2":
        df_pie['Category_number'][1]=df_pie['Category_number'][1]+1
    elif df["blcl"][i] == "type3":
        df_pie['Category_number'][2] = df_pie['Category_number'][2] + 1
    elif df["blcl"][i] == "type4":
        df_pie['Category_number'][3] = df_pie['Category_number'][3] + 1
    else:
        df_pie['Category_number'][4] = df_pie['Category_number'][4] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "blcl")
fig.update_layout(showlegend = True,
        title = {'text': "ind",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/blcl_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1,2,3,4])
df_pie['Category'] = ["type1","type2","type3","type4","type5"]
df_pie['Category_number'] = [0,0,0,0,0]
for i in range(len(df["status"])):
    if df["status"][i] == "type1":
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    elif df["status"][i] == "type2":
        df_pie['Category_number'][1]=df_pie['Category_number'][1]+1
    elif df["status"][i] == "type3":
        df_pie['Category_number'][2] = df_pie['Category_number'][2] + 1
    elif df["status"][i] == "type4":
        df_pie['Category_number'][3] = df_pie['Category_number'][3] + 1
    else:
        df_pie['Category_number'][4] = df_pie['Category_number'][4] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "status")
fig.update_layout(showlegend = True,
        title = {'text': "status",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/status_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1,2,3,4])
df_pie['Category'] = ["type1","type2","type3","type4","type5"]
df_pie['Category_number'] = [0,0,0,0,0]
for i in range(len(df["trf"])):
    if df["trf"][i] == "type1":
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    elif df["trf"][i] == "type2":
        df_pie['Category_number'][1]=df_pie['Category_number'][1]+1
    elif df["trf"][i] == "type3":
        df_pie['Category_number'][2] = df_pie['Category_number'][2] + 1
    elif df["trf"][i] == "type4":
        df_pie['Category_number'][3] = df_pie['Category_number'][3] + 1
    else:
        df_pie['Category_number'][4] = df_pie['Category_number'][4] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "trf")
fig.update_layout(showlegend = True,
        title = {'text': "trf",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/trf_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1,2,3,4])
df_pie['Category'] = ["ne","nw","se","sw","ct"]
df_pie['Category_number'] = [0,0,0,0,0]
for i in range(len(df["region"])):
    if df["region"][i] == "ne":
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    elif df["region"][i] == "nw":
        df_pie['Category_number'][1]=df_pie['Category_number'][1]+1
    elif df["region"][i] == "se":
        df_pie['Category_number'][2] = df_pie['Category_number'][2] + 1
    elif df["region"][i] == "sw":
        df_pie['Category_number'][3] = df_pie['Category_number'][3] + 1
    else:
        df_pie['Category_number'][4] = df_pie['Category_number'][4] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "region")
fig.update_layout(showlegend = True,
        title = {'text': "region",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/region_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1])
df_pie['Category'] = ["True","FALSE"]
df_pie['Category_number'] = [0,0]
for i in range(len(df["trf"])):
    if df["ur"][i] :
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    else:
        df_pie['Category_number'][1] = df_pie['Category_number'][1] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "ur")
fig.update_layout(showlegend = True,
        title = {'text': "ur",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/ur_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1])
df_pie['Category'] = ["True","FALSE"]
df_pie['Category_number'] = [0,0]
for i in range(len(df["ots"])):
    if df["ots"][i] :
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    else:
        df_pie['Category_number'][1] = df_pie['Category_number'][1] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "ots")
fig.update_layout(showlegend = True,
        title = {'text': "ots",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/ots_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1])
df_pie['Category'] = ["True","FALSE"]
df_pie['Category_number'] = [0,0]
for i in range(len(df["pltrs"])):
    if df["pltrs"][i] :
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    else:
        df_pie['Category_number'][1] = df_pie['Category_number'][1] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "pltrs")
fig.update_layout(showlegend = True,
        title = {'text': "pltrs",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/pltrs_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1])
df_pie['Category'] = ["True","FALSE"]
df_pie['Category_number'] = [0,0]
for i in range(len(df["plts"])):
    if df["plts"][i] :
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    else:
        df_pie['Category_number'][1] = df_pie['Category_number'][1] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "plts")
fig.update_layout(showlegend = True,
        title = {'text': "plts",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/plts_pie.html")

df_pie = pd.DataFrame(columns=['Category', 'Category_number'], index=[0,1])
df_pie['Category'] = ["type1","type2"]
df_pie['Category_number'] = [0,0]
for i in range(len(df["plts"])):
    if df["cmt"][i]=="type1" :
        df_pie['Category_number'][0]=df_pie['Category_number'][0]+1
    else:
        df_pie['Category_number'][1] = df_pie['Category_number'][1] + 1
fig = px.pie( data_frame = df_pie, names = "Category", values = "Category_number" , color = "Category_number", color_discrete_sequence = px.colors.qualitative.Plotly)
fig.update_xaxes(title="Category")
fig.update_yaxes(title = "cmt")
fig.update_layout(showlegend = True,
        title = {'text': "cmt",'y':0.95,'x':0.5,'xanchor': 'center',
            'yanchor': 'top'})
fig.write_html(f"Distribution_Visualization/cmt_pie.html")