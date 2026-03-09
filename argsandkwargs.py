def args_example(*args):  
    for arg in args:  
        print(arg)

args_example(1, 2, 3)   

def kwargs_example(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}") 
kwargs_example(name="Alice", age=30, city="New York")       