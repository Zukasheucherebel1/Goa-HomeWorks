def manual_range(end, start = 0, step = 1):
    # ფუნქცია იღებს სამი არგუმენტს: 
     while start <= end:
        #სანამ საწყისი მნიშვნელობა ნაკლებია ან ტოლი დასრულება
        
        
        print(start)
        # დაბეჭდავს საწყის მნიშვნელობას
        
        start += step
        # ზრდის საწყის მნიშვნელობას start ნაბიჯის step ზომით.
    
manual_range(10, 1, 2)

# ფუნქციის გამოძახება, სადაც end = 10, start = 1 და step = 2.