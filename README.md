# streamlit-to-heroku-example

### Heroku Cloud Application Platform

Web app: https://streamytaxis.herokuapp.com/

In the Google Colab notebook ["Dynamic plots in a web app"](https://github.com/AlisonJD/tb_examples/blob/main/Dynamic_plots_in_a_web_app.ipynb) ngrok is used to tunnel to a localhost running a web app developed in Streamlit with data from [Tinybird](https://www.tinybird.co/) APIs. The downside of the Colab/ngrok approach is that the web app is only alive for as long as the notebook is running.

An alternative to ngrok is [Heroku](https://www.heroku.com), which is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

My thanks to this blog post from [Sercan Gul](https://github.com/sercangul):
https://medium.com/nerd-for-tech/how-to-deploy-streamlit-dashboard-with-heroku-ca00064402e8
for guidance on writing the required files:
- Procfile
- setup.sh
- requirements.txt.

This repository uses app.py from ["Dynamic plots in a web app"](https://github.com/AlisonJD/tb_examples/blob/main/Dynamic_plots_in_a_web_app.ipynb) and the three files needed for Heroku. 

Simply open an account on Heroku, create an app on the dashboard, connect to your GitHub repository and deploy!

### Streamlit Community
Another option is to launch the app directly from the [Streamlit](https://streamlit.io) website. You will need to be connected to your GitHub and have the file `requirements.txt` in your repository. The 'Community' tier allows you to share up to three open-source apps for free.

https://share.streamlit.io/alisonjd/streamlit-to-heroku-example/main/app.py 


Date: 1 Nov 2021
