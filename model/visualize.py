import matplotlib.pyplot as plt

models = ['SVM', 'Decision Tree', 'Logistic Regression']
accuracy = [52, 55, 51]

plt.bar(models, accuracy)
plt.title("Model Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()
