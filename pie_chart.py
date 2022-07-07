import numpy as np
import matplotlib.pyplot as plt

categories = ['No migraine', 'Minor migraine', 'Moderate migraine', 'Major migraine', 'God awful migraine']

amount = [0, 1, 9, 11, 9]

pieColor = ['MediumBlue', 'SpringGreen', 'BlueViolet', 'r']

plt.axis('equal')

plt.pie(amount, labels=categories, autopct='%1.1f%%', colors=pieColor)

plt.savefig('maddiemigraine')
