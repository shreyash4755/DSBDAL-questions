#Q1
import numpy as np
sales_figures = [100, 200, 150, 300, 250, 400, 350]
sales_array = np.array(sales_figures)
print(sales_array)

#Q2
import numpy as np
store1_prices = np.array([10, 20, 30])
store2_prices = np.array([1, 2, 3])
added_prices = store1_prices + store2_prices
multiplied_prices = store1_prices * store2_prices
print("Element-wise addition:", added_prices)
print("Element-wise multiplication:", multiplied_prices)

#Q3
import numpy as np
sales_january = np.array([300, 400])
sales_february = np.array([500, 600])
combined_sales = np.concatenate((sales_january, sales_february))
print("Combined sales data:", combined_sales)

#Q4
import numpy as np
scores = np.array([[80, 90], [85, 95]])
scores_1d = scores.flatten()
print("1D array:", scores_1d)

#Q5
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
reshaped_data = data.reshape(2, 3)
print("Reshaped 2x3 matrix:")
print(reshaped_data)

