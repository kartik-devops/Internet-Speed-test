import speedtest
import plotly.graph_objects as go
import os
import pyfiglet
def speedometer_representation(val , st ,su , ref):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = val,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': st + " in " + su, 'font': {'size': 24}},
        delta = {'reference': ref, 'increasing': {'color': "green"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
             'bgcolor': "white",
             'borderwidth': 2,
             'bordercolor': "gray",
             'steps': [
                 {'range': [0, 25], 'color': 'red'},
                 {'range': [25, 50], 'color': 'yellow'},
                 {'range': [50,100] , 'color':'green' }],
            }))
    fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "forte"})
    fig.show()


s = speedtest.Speedtest()
var1 = s.download()
var2 = s.upload()
servernames =[]  
s.get_servers(servernames)  
out = pyfiglet.figlet_format("Speed-Test", font="slant")
print(out)
ans=True
while ans:
    print("""
        1. Ping in ms
        2. Upload Speed
        3. Download Speed
        4. Server Details
        
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
    	#print(s.results.ping)
    	speedometer_representation(s.results.ping , "Time" , "ms" , 50)
    elif ans=="2":
    	speedometer_representation(var2/1000000 ,"Speed" ,"Mbps" , 10)
    elif ans=="3":
        speedometer_representation(var1/1000000 , "Speed"  , "Mbps", 25)
    elif ans=='4':
        best_server = s.get_best_server()
        for key, value in best_server.items():
            print(key, ' : ', value)    
    elif ans=="5":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")

