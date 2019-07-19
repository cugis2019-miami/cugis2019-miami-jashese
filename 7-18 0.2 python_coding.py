# 7-18 



age = {"steve":32,"lia":28,"vin":45,"katie":38}
print(age)
agedata = [age]



print(agedata)



agedata



aged

import pandas

agedf = pandas.DataFrame(agedata)



print(agedf)







studentallinfo = [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"],["katie",38,"female"]]



print(studentallinfo)







df = pandas.DataFrame(studentallinfo)



print(df)


owo = "this aint it cheif"


\







df2= pandas.DataFrame(studentallinfo, columns=["Name","Age", "Gender"])



print(df2)



import plotly

studentlist = [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"],["katie",38,"female"]]
print(studentlist)


studentlistdf = pandas.DataFrame(studentlist, columns = ["name", "age","gender"],
                                     index = [1,2,3,4])
print(studentlistdf)

#graph our data
import plotly
dir(plotly)
  
import plotly.graph_objs as go 

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])
#qwertyuiopasdfghjklzxcvbnm
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

womenoccupation = go.Bar(x= df["occupation"], y=df["women"])

plot([womenoccupation])

fig = go.Figure(data=[womenoccupation])
plot(fig)

titles = go.Layout(title = "",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                        )
                    ),

                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                                   )
                      )
                    )





fig 
womenoccupation = go.Bar(x= df["occupation"], y=df["women"],
                         marker = {"color": df["women"], "colorscale":"YlOrRd"}
                         )

fig= go.Figure(data=[womenoccupation], layout = titles)

plot(fig)
















