from sklearn import linear_model

lr = linear_model.LinearRegression()
lr.fit(x, y)
predictions = lr.predict(x)