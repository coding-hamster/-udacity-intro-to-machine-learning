from sklearn.preprocessing import MinMaxScaler
import numpy as np

weight_of_people = np.array([115.0, 140.0, 175.0])
scaler = MinMaxScaler()
rescaled_weight_of_people = scaler.fit_transform(weight_of_people)
print(rescaled_weight_of_people)
