from sklearn import tree
#[height, weight, shoe size]
X = [[181,80,44],[177,70,43],[160,60,38]]
Y=['M','M','F']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
result = clf.predict([[168,70,37]])
print(result)