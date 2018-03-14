import pandas as pd
import numpy as np

step_data = [3432,3532,6756,2343,4566,3214]
step_counts = pd.Series(step_data, name = 'Steps')

#print(step_counts)

step_counts.index = pd.date_range('20150329', periods = 6)

#print(step_counts)

#print(step_counts.dtypes)
#print(step_counts['2015-04-02'])

#print(step_counts['2015-04'])
step_counts = step_counts.astype(np.float)

#print(step_counts.dtypes)
step_counts[1:3] = np.NaN
#print(step_counts)

step_counts = step_counts.fillna(0.)

#print(step_counts)
cycling_distance = [10.7,0,None,15.3,10.9,12.3,None]
joined_data = list(zip(step_data,cycling_distance))

activity_df = pd.DataFrame(joined_data, index = pd.date_range('20150329',periods = 6), columns = ['Walking', 'Cycling'])

#print(activity_df)


file_path = 'data/Iris_Data.csv'
data = pd.read_csv(file_path)
#print(data.columns)
#print(data.sepal_length)

data['sepal_area'] = data.sepal_length * data.sepal_width

#print(data.iloc[:5,-3:])

data ['Abbrev'] = (data.species.apply(lambda x: x.replace('Iris-','')))

#print(data.iloc[:5,-3:])

small_data = pd.concat([data.iloc[:2],data.iloc[-2:]])

#print(small_data)

group_sizes = (data.groupby('species').size())

#print(group_sizes)

#print(data.describe())


#import matplotlib.pyplot as plt

#plt.plot(data.sepal_length,data.sepal_width,ls = '',marker='o')
print(data.shape[0])
print(data.columns.tolist())
#print(data.dtypes)
#data.species = data.species.str.replace('Iris-','')
#print(data.head())
#### The no of species present 

















