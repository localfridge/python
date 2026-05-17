medical_check=input("Do you have medical coverage? Y/N").strip().upper()

if medical_check=="Y":
    print("allowed to take the final exams")

else:
    days_took_off=int(input("how many days were you off?"))
    if days_took_off >=75:
      print("allowed")
    else:
        print(" not allowed")





        
