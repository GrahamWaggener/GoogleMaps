import plotly.express as px #For interactive map functionality
import pandas as pd #For reading the CSV file
#add time decoder to show place AND time from CSV on hover

if __name__ == '__main__':
    df = pd.read_csv("placesgoneto.csv")
    df = df.drop_duplicates(keep=False, subset=['lat', 'long'])
    df['displays'] = df['item']
    fig = px.scatter_geo(df,lat='long',lon='lat', hover_name='displays') #Plots the locations on a map with data when hovered over
    fig.update_layout(title = '2018-2022', title_x=0.5)
    fig.show()