
start_date = data.Date.loc[0]
end_date = data.Date.loc[len(data)-1]
start_year = start_date.year
start_month =  start_date.month
start_day = start_date.day
end_year = end_date.year
end_month =  end_date.month
end_day = end_date.day
number_of_days = abs((end_date-start_date).days)
start_date = datetime.date(start_date.year, start_date.month, start_date.day)
date_list = []
for day in range(number_of_days):
    a_date = (start_date + datetime.timedelta(days = day)).isoformat()
    date_list.append(a_date)
date_list = pd.to_datetime(date_list)
new_data = pd.DataFrame({'Date':date_list})
x = new_data.Date
old_x = data.Date
y = []
for i in range(len(x)):
    x_i = x.loc[i]
    diff_list = []
    for j in range(len(data)):
        diff_list.append(abs((x_i-old_x.loc[j]).days))
    diff_list = np.array(diff_list)
    y.append(data.Close[diff_list.argmin()])
        
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.title('Original Data',color='red',fontsize=20)
plt.scatter(data.Date,data.Close,s=2)
plt.xlabel('Date')
plt.ylabel('Close')
plt.subplot(1,2,2)
plt.title('Smoothed Data',color='navy',fontsize=20)

plt.scatter(x,y,s=2,color='navy')
plt.xlabel('Date')
plt.ylabel('Close')
