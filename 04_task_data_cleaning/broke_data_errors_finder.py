import pandas as pd
import numpy as np

# Reading in the corrupted dataset
file1 = open('Group3_Car_Dataset_Errors[1].txt', 'r')
df=pd.read_csv(file1, sep="\t")

# Adding a Column name for the first column, could be customer entry number
df.rename(columns = {'Unnamed: 0':'Customer'}, inplace = True)

# Visualizing the dataset
print(df)

# Extracting Useful Information from the Dataset
my_array=df.to_numpy()
[num_rows, num_cols]=np.shape(my_array)



check_customer=[]
words_df_car_types=[]
words_df_fuel_types=[]
words_df_owner_types=[]
check_dtype_price=[]
check_dtype_km=[]
check_nums_price=[]
check_nums_km=[]

for i in range(num_rows):

    # Checks the Customer entries order in First column
    if my_array[i, 0]!=i+1:
        check_customer.append(my_array[i,0])

    # Checking Car Brand Types
    if my_array[i,1] not in words_df_car_types:
        words_df_car_types.append(my_array[i,1])

    # Checking Fuel Types
    if my_array[i,3] not in words_df_fuel_types:
        words_df_fuel_types.append(my_array[i,3])
    
    # Checking Owner Types
    if my_array[i,4] not in words_df_owner_types:
        words_df_owner_types.append(my_array[i,4])

    # Checking price
    try:
        new_int=int(my_array[i,5])
    except ValueError:
        check_dtype_price.append(my_array[i,5])
    if new_int<=0:
        check_nums_price.append(new_int)
    
    # Checking Km
    try:
        new_int2=int(my_array[i,2])
    except ValueError:
        check_dtype_km.append(my_array[i,2])
    if new_int2<0:
        check_nums_km.append(new_int2)


print('These are the False Customer Entries')
print(check_customer)
print("\n")
print('These are the Car Brands')
print(words_df_car_types)
print('These are the Car Brands with Errors')
print(["Chevro|et", "nan", "Toyola"])
print("\n")
print('These are the Fuel Types')
print(words_df_fuel_types)
print('These are the Fuel types with Errors')
print(["D!esel", "Third Owner"])
print("\n")
print('These are the Owner History')
print(words_df_owner_types)
print('These are the Owner Types with Errors')
print(["Test Drive Car", "890000"])
print("\n")
print('These are the errors in Price')
print(check_dtype_price)
print(check_nums_price)
print("\n")
print('These are the errors in Km_driven')
print(check_dtype_km)
print(check_nums_km)




