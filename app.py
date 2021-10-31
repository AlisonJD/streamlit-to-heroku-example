import streamlit as st
import datetime

import pandas as pd
import plotly.express as px

def main():
  st.title("New York City Yellow Taxi Trips")

  st.sidebar.title("Select boroughs and dates")

  boroughs = ['Bronx', 'Brooklyn', 'EWR', 'Manhattan','Queens','Staten Island']
  pick_up = st.sidebar.radio('Pick-up borough', boroughs)
  drop_off = st.sidebar.radio('Drop-off borough', boroughs)

  pick_up_id=boroughs.index(pick_up)
  drop_off_id=boroughs.index(drop_off)

  start_date = st.sidebar.date_input('Start date', min_value = datetime.date(2019,1,1), max_value = datetime.date(2019,12,31), value = datetime.date(2019, 1, 1))
  end_date = st.sidebar.date_input('End date', min_value = datetime.date(2019,1,1), max_value = datetime.date(2019,12,31), value = datetime.date(2019, 1, 31))

  start = start_date.strftime("%Y-%m-%d")
  end = end_date.strftime("%Y-%m-%d")

  text = "From " + pick_up + " to " + drop_off
  st.subheader(text)

  text = "in the period " + start + " to " + end
  st.subheader(text)

  output = 'https://api.tinybird.co/v0/pipes/taxi_boroughs_by_hr.csv?start_date='+start+'&end_date='+end+'&pick_up_id='+str(pick_up_id)+'&drop_off_id='+str(drop_off_id)+'&token=p.eyJ1IjogImNkMDZkYzdlLTA5NWEtNDA0YS1iODNkLWQ1NzUwNmViYWZlZCIsICJpZCI6ICJhYjE5YzU1Ny1mYzlkLTQ4MmUtOTY0NC00ZjNlYmIxNWE3ZjIifQ.xbE9Ht1ZxKUrcG2HpHclTBOjctlYSPUm_GYzlehow6o'
  df=pd.read_csv(output)
  
  plot = px.bar(
                data_frame=df,
                x = "hr",
                y = "trips",
                color = "percent",
                title="How trips vary over the day",
                labels={
                     "hr": "Hour of the day",
                     "trips": "Total number of trips"
                 }
            )
  st.plotly_chart(plot, use_container_width=True)

  text = "Compare this to total New York City trips over the same period"
  st.subheader(text)

  output = 'https://api.tinybird.co/v0/pipes/taxi_by_hr.csv?start_date='+start+'&end_date='+end+'&token=p.eyJ1IjogImNkMDZkYzdlLTA5NWEtNDA0YS1iODNkLWQ1NzUwNmViYWZlZCIsICJpZCI6ICIzMmVmYTZjMy1iY2Q4LTQxYTMtOTVkMy1iNWYyMDEyZmM5MmEifQ.6SsAU9SOROgPJN9jaZACb9Xqn-EKTL602xK0t0p2j8o'
  df=pd.read_csv(output)
  
  plot = px.bar(
                data_frame=df,
                x = "hr",
                y = "trips",
                color = "percent",
                title="How trips vary over the day",
                labels={
                     "hr": "Hour of the day",
                     "trips": "Total number of trips"
                 }
            )
  st.plotly_chart(plot, use_container_width=True)

  st.subheader("Note how Manhattan dominates the trips!")

  st.markdown('#### Example Tinybird node')

  st.markdown('''
  %

SELECT 

  toHour(tpep_pickup_datetime) as hr, 

  count() as trips 

FROM node_0

WHERE toDate(tpep_pickup_datetime) 

BETWEEN {{Date(start_date, '2019-01-01')}} AND {{Date(end_date, '2019-12-31')}}

AND puborough_id = {{UInt8(pick_up_id, 0)}} AND doborough_id = {{UInt8(drop_off_id, 0)}} 

GROUP BY hr

'''
)

if __name__ == '__main__':
	main()
