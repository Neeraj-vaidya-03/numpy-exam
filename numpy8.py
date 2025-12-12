
import numpy as np

def create_array():
    print("\n --select the type of array to create---")
    print("1. 1D array")
    print("2. 2D array")
    print("3. 3D array")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        size = int(input("\n--Enter number of elements: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        arr = np.array(elements)
        print("\n--Array created successfully--")
        print(arr)
        return arr

    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        column = int(input("Enter number of columns: "))
        total = rows * column
        elements = list(map(int, input(f"Enter {total} elements separated by space: ").split()))
        arr = np.array(elements).reshape(rows, column)   
        print("\n--Array created successfully--")
        print(arr)
        return arr

    elif choice == 3:
        dim1 = int(input("Enter dimension 1: "))
        dim2 = int(input("Enter dimension 2: "))
        dim3 = int(input("Enter dimension 3: "))
        total = dim1 * dim2 * dim3
        elements = list(map(int, input(f"Enter {total} elements: ").split()))
        arr = np.array(elements).reshape(dim1, dim2, dim3)
        print("\n--Array created successfully--")
        print(arr)
        return arr

    else:
        print("\n--Invalid choice--")
        return None
    
create_array()

import numpy as np

def indexing_slicing(arr):
    print("\n chosse  an operation--")
    print("1.Indexing")
    print("2.slicing")
    print("3.Go back")
    choice = int(input("Enter the choice (1-3)"))
    
    if choice == 1:
        r =int(input("Enter number of row "))
        c = int(input("Enter number of column "))
        print(" index value:", arr[r][c])
        
    elif choice == 2:
        r = input("Enter number of row range (start :end): ")
        c = input("Enter number of column range (start : end): ")
        
        r1 , r2 = map(int, r.split())
        c1 , c2 = map(int, c.split())
        
        print("\n sliced array:")
        print(arr[r1:r2 , c1:c2])
        
    else:
        return 
    
import numpy as np

def math_operation(arr):
    print("\n--choose a mathematical operation--")
    print("1.Addition")
    print("2.substraction")
    print("3.Multiplication")
    print("4.Division")
    
    choice = int(input("Enter your choice : (1-4)"))
    num = float(input("Enter number:"))
    
    if choice == 1:
        print(arr + num)
    
    elif choice == 2:
        print(arr - num)
        
    elif choice == 3:
        print(arr * num)
        
    elif choice == 3:
        print(arr/num)
        
    else:
        print("invalid choice") 
        
import numpy as np

def combine_split():
    print("\n-- Combine array and Split array ---")
    print("1. Combine array")
    print("2. Split array")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        arr1 = list(map(int, input("Enter elements of first array: ").split()))
        arr2 = list(map(int, input("Enter elements of second array: ").split()))
        
        combined = arr1 + arr2
        
        print("\nFirst array:", arr1)
        print("Second array:", arr2)
        print("Combined array:", combined)

    elif choice == "2":
        arr = list(map(int, input("Enter array elements: ").split()))
        split_index = int(input("Enter split index: "))
        
        first_part = arr[:split_index]
        second_part = arr[split_index:]
        
        print("\nOriginal array:", arr)
        print("First part:", first_part)
        print("Second part:", second_part)
    
    else:
        print("Invalid choice.")
        print("Invalid choice.")
        
combine_split()


import numpy as np

def search_sort_filter():
    print("\n--choose an option--")
    print("1.Search a value")
    print("2.Sort a value")
    print("3.Filter a value")
    choice = int(input("Enter your choice (1-3)"))
    
    if choice == 1:
        arr = list(map(int,input("Enter array elements").split()))
        value = int(input("Enter value to search"))
        if value in arr:
            index = arr.index(value)
            print(value,"found at index",index)
        else:
            print("value not found in array")
            
    elif choice == 2:
        print("\nOriginal Array:")
        print(arr)
        print("\nSorted Array:")
        print(np.sort(arr))
        print("(Sorting applied row-wise.)")
        
    elif choice == 3:
        threshold = int(input("Enter threshold value: "))
        filtered = arr[arr > threshold]
        print(filtered)
        
    else:
        print("Invalid choice")
        

search_sort_filter()


import numpy as np

def math_operation(arr):
    print("\n--choose a mathematical operation--")
    print("1.Addition")
    print("2.substraction")
    print("3.Multiplication")
    print("4.Division")
    
    choice = int(input("Enter your choice : (1-4)"))
    num = float(input("Enter number:"))
    
    if choice == 1:
        print(arr + num)
    
    elif choice == 2:
        print(arr - num)
        
    elif choice == 3:
        print(arr * num)
        
    elif choice == 3:
        print(arr/num)
        
    else:
        print("invalid choice") 
        
import numpy as np

def aggregates(arr):
    print("\n---choose compute Aggregates and statistics--")
    print("1.Sum.")
    print("2.Mean.")
    print("3.Median.")
    print("4.Standard Deviation.")
    print("5.Variance.")
    
    choice = int(input("Enter your choice "))
    if choice == 1:
        print("Sum:", np.sum(arr))
    elif choice == 2:
        print("Mean:", np.mean(arr))
    elif choice == 3:
        print("Median:", np.median(arr))
    elif choice == 4:
        print("Standard Deviation:", np.std(arr))
    elif choice == 5:
        print("Variance:", np.var(arr))
    else:
        print("Invalid choice.")
               


def show():
    project = create_array()
    
    while True:
         print("\nWelcome to the NumPy Analyzer!")
         print("1.creat a numpy array")
         print("2.indexing and slicing")
         print("3.math operation")
         print("4.combine split")
         print("5.search sort and filter")
         print("6.aggregates")
         print("7.Exit")
         
         choice =int(input("Enter your choice:"))
         
    if choice == 1:
        arr = create_array()

    elif choice == 2:
        if arr is None:
            print("Create array first!")
        else:
            indexing_slicing(arr)

    elif choice == 3:
        if arr is None:
            print("Create array first!")
        else:
            math_operation(arr)

    elif choice == 4:
        combine_split()

    elif choice == 5:
        if arr is None:
            print("Create array first!")
        else:
            search_sort_filter(arr)

    elif choice == 6:
        if arr is None:
            print("Create array first!")
        else:
            aggregates(arr)

    elif choice == 7:
        print("\nThank you for using NumPy Analyzer!")
        breakpoint

    else:
        print("Invalid choice, try again.") 
        
show()
             
             

         
         