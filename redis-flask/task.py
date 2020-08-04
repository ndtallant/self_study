import time

def task_in_background(t):  
    delay = t  
         
    print("Running Task")  
    print("Simulates the {delay} seconds")  
                
    time.sleep(delay)  
                     
    print("Completed Task")  
                              
    return len(t)
