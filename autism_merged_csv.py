

import pandas as pd
import numpy as np

for _ in " " * int(input()):
  print("hi")

data = pd.read_csv ('/content/drive/My Drive/Autism CSV/Final_ds.csv')

data

# Total number of records
n_records = len(data.index)

# TODO: Number of records where individual's with ASD
n_asd_yes = len(data[data['Class'] == 'YES'])

# TODO: Number of records where individual's with no ASD
n_asd_no = len(data[data['Class'] == 'NO'])

# TODO: Percentage of individuals whose are with ASD
yes_percent = float(n_asd_yes) / n_records *100

# Print the results
print ("Total number of records: {}".format(n_records))
print ("Individuals diagonised with ASD: {}".format(n_asd_yes))
print ("Individuals not diagonised with ASD: {}".format(n_asd_no))
print ("Percentage of individuals diagonised with ASD: {:.2f}%".format(yes_percent))

data = pd.read_csv ('/content/drive/My Drive/Autism CSV/Final_ds.csv', na_values=['?'])
data.head(n=5)

print(data['A1'].isnull().values.any())
print(data['A2'].isnull().values.any())
print(data['A3'].isnull().values.any())
print(data['A4'].isnull().values.any())
print(data['A5'].isnull().values.any())
print(data['A6'].isnull().values.any())
print(data['A7'].isnull().values.any())
print(data['A8'].isnull().values.any())
print(data['A9'].isnull().values.any())
print(data['A10'].isnull().values.any())

print(data['Age'].isnull().values.any())
print(data['Gender'].isnull().values.any())
print(data['Ethnicity'].isnull().values.any())
print(data['Parent_ASD'].isnull().values.any())
print(data['Score'].isnull().values.any())
print(data['Class'].isnull().values.any())
print(data['Jaundice '].isnull().values.any())

# There are missing values in the Age, Ethnicity 
# LEt us check how many missing values are there in those 2 attributes
print (data['Age'].isnull().sum())
print (data['Ethnicity'].isnull().sum())

# As it is a medical data and we are dealing with the healthcare domain so instead of subscituting we are deleting the rows only
data.dropna(inplace=True)
data.describe()

# Total number of records
n_records = len(data.index)

# TODO: Number of records where individual's with ASD
n_asd_yes = len(data[data['Class'] == 'YES'])

# TODO: Number of records where individual's with no ASD
n_asd_no = len(data[data['Class'] == 'NO'])

# TODO: Percentage of individuals whose are with ASD
yes_percent = float(n_asd_yes) / n_records *100

# Print the results
print ("Total number of records: {}".format(n_records))
print ("Individuals diagonised with ASD: {}".format(n_asd_yes))
print ("Individuals not diagonised with ASD: {}".format(n_asd_no))
print ("Percentage of individuals diagonised with ASD: {:.2f}%".format(yes_percent))

data.drop(['Score'], axis=1, inplace= True)
data.drop(['Age'], axis=1, inplace= True)

data.head()

data['Gender'] = data['Gender'].map({'M': 0, 'F': 1})
data['Jaundice '] = data['Jaundice '].map({'NO': 0, 'YES': 1})
data['Parent_ASD'] = data['Parent_ASD'].map({'NO': 0, 'YES': 1})
data['Class'] = data['Class'].map({'NO': 0, 'YES': 1})

data.head()

data['Ethnicity'].unique()

data['Ethnicity'] = data['Ethnicity'].map({'others':'Others','Turkish':'Turkish','South Asian':'South Asian','Hispanic':'Hispanic','Pasifika':'Pasifika','Black' : 'Black','Aboriginal':'Aboriginal','Latino':'Latino','Asian':'Asian','White-European-European': 'White-European' ,'Others ' : 'Others','Middle Eastern ':'Middle Eastern' })

data['Ethnicity'].unique()

# Total number of records
n_records = len(data.index)

# TODO: Number of records where individual's with ASD
n_asd_yes = len(data[data['Class'] == 1])

# TODO: Number of records where individual's with no ASD
n_asd_no = len(data[data['Class'] == 0])

# TODO: Percentage of individuals whose are with ASD
yes_percent = float(n_asd_yes) / n_records *100

# Print the results
print ("Total number of records: {}".format(n_records))
print ("Individuals diagonised with ASD: {}".format(n_asd_yes))
print ("Individuals not diagonised with ASD: {}".format(n_asd_no))
print ("Percentage of individuals diagonised with ASD: {:.2f}%".format(yes_percent))

#data['Ethnicity'] = data['Ethnicity'].astype('str')
data['Ethnicity'] = data['Ethnicity'].astype(str)

#label encoding of ethnicity
object_cols = ['Ethnicity']

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

label_autism_data = data.copy()

for col in object_cols:
  label_autism_data[col] = label_encoder.fit_transform(data[col])

label_autism_data.head()

X = label_autism_data.iloc[:,0:14]
y = label_autism_data.iloc[:,14]

X

y

# Borderline smote
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import BorderlineSMOTE 
sm = BorderlineSMOTE(random_state=42)
X_res_borderline, y_res_bol = sm.fit_resample(X, y)

print('Resampled dataset shape %s' % Counter(y))
print('Resampled dataset shape %s' % Counter(y_res_bol))

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_res_borderline, y_res_bol, test_size=0.25, random_state=0)

len(X_train)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#kNN
# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=42) 
classifier.fit(X_train,Y_train)

# logistic
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)

#svm
# Fitting classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel= 'linear',random_state=0)
classifier.fit(X_train,Y_train)

# kernel svm
# Fitting classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf',random_state=0)
classifier.fit(X_train,Y_train)

#naive bayes
# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)

# decision tree
# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)

#random forest
# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10,random_state=0,criterion='entropy')
classifier.fit(X_train,Y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

from sklearn.metrics import accuracy_score 
acc = accuracy_score(Y_test,y_pred) 
cm = confusion_matrix(Y_test, y_pred) 
print(cm) 
print(acc)

from imblearn.over_sampling import ADASYN
ada = ADASYN(random_state=42)
X_res_ada, y_res_ada = ada.fit_resample(X, y)

print('Resampled dataset shape %s' % Counter(y))
print('Resampled dataset shape %s' % Counter(y_res_ada))

# Splitting the dataset into the Training set and Test set 
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train,Y_test = train_test_split(X_res_ada,y_res_ada, test_size = 0.25, random_state = 42)

len(X_train) , len(Y_train) , len(X_test) , len(Y_test)



# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

X_train=X_train.reshape((1797,14))

#knn
# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=42,metric='minkowski')
classifier.fit(X_train,Y_train)

# logistic
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)

#svm
# Fitting classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel= 'linear',random_state=0)
classifier.fit(X_train,Y_train)

# kernel svm
# Fitting classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf',random_state=0)
classifier.fit(X_train,Y_train)

#naive bayes
# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)

# decision tree
# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)

#randon forest
# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10,random_state=0,criterion='entropy')
classifier.fit(X_train,Y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

from sklearn.metrics import accuracy_score 
acc = accuracy_score(Y_test,y_pred) 
cm = confusion_matrix(Y_test, y_pred) 
print(cm) 
print(acc)

from imblearn.over_sampling import SMOTE 
smoteSampler = SMOTE(random_state=42)
X_res_smote, y_res_smote = smoteSampler.fit_resample(X,y)

print('Resampled dataset shape %s' % Counter(y)) 
print('Resampled dataset shape %s' % Counter(y_res))

#Splitting the dataset into the Training set and Test set 
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train,Y_test = train_test_split(X_res_smote,y_res_smote, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#knn
# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=42,metric='minkowski')
classifier.fit(X_train,Y_train)

# logistic
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)

#svm
# Fitting classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel= 'linear',random_state=0)
classifier.fit(X_train,Y_train)

# kernel svm
# Fitting classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf',random_state=0)
classifier.fit(X_train,Y_train)

#naive bayes
# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)

# decision tree
# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)

#random forest
# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10,random_state=0,criterion='entropy')
classifier.fit(X_train,Y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

from sklearn.metrics import accuracy_score 
acc = accuracy_score(Y_test,y_pred) 
cm = confusion_matrix(Y_test, y_pred) 
print(cm) 
print(acc)



