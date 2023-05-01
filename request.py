import requests

url="http://192.168.29.89:8080/"

resp=requests.post(url,json={"text":"""
Of the 226 sitting MPs in the Rajya Sabha  197 are crorepatis. According to a report by Association for Democratic Reforms titled "Analysis of Criminal Background  Financial  Education  Gender and other details of sitting Rajya Sabha MPs 2022 " 87% of sitting Rajya Sabha MPs are crorepatis."Out of 226 sitting MPs  197 are crorepatis."  the report said.[ADVT]172[/ADVT]Among the 226 MPs in the Rajya Sabha  86 MPs which comprise 38% of the total number of MPs have assets worth Rs 10 crore and above. 15% MPs have properties worth Rs 5 crore to Rs 10 crore  34% have assets worth Rs 1 crore to Rs 5 crore and 10% have assets worth Rs 20 lakh to Rs 1 crore and only 3% of sitting MPs in the Rajya Sabha have assets below Rs 20 lakh  the report said.Out of 85 Bharatiya Janata Party (BJP) Rajya Sabha MPs  74 are crorepatis. Congress has 29 Rajya Sabha MPs as crorepatis. The Congress has a total of 31 MPs. 10 out of 13 Trinamool MPs  9 out of 10 Dravida Munnetra Kazhagam (DMK) MPs and 8 out of 9 Yuvajana Shramika Rythu Congress Party (YSRCP) MPs have declared assets worth over Rs 1 crore.According to the report  the top three Rajya Sabha MPs with the highest assets are Dr Bandi Partha Saradhi from the TRS with over Rs 5300 crore  Alla Ayodhya Rami Reddy with assets worth Rs 2577 crore and Jaya Amitabh Bachchan from the Samajwadi Party (SP) with assets worth Rs 1001 crore.

"""})
print('response>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',resp)
print(resp.json())