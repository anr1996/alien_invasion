# More Conditional Tests
import sys

college_name = 'stem'

print(f"\nHere are the transfer requirements of the University of {college_name.title}:\n")

requirement_list = []
requirement_list.append('18 years or older.') 
requirement_list.append('between the ages of 16 and 17 with a high school diploma.')
requirement_list.append('gpa 3.0 or higher.') 
requirement_list.append('a resident of Oregon.')
requirement_list.append(f'an out of state scholarship to {college_name.title()}.')

num = 0
for requirements in requirement_list:
    num += 1
    print(f"{num}.) {requirements[0].upper()}{requirements[1:]}")
print("\n")

name = input("What is your name?\n")

age = int(input(f"{name.title()} how old are you?\n"))

if age < 16:
    print(f"Sorry {name} you must be atleast 16 years old to qualify for " + 
          f"{college_name.title()}.")


elif age >= 16 and age <= 17:
    response = input("Do you have a high school diploma?\n")
    
    if response.lower() == 'yes':
        response = input("Are you from Oregon?\n")
        
        if response.lower() == 'yes':
            response = input("Do you have a gpa of 3.0 or higher?\n")
        
            if response.lower() == 'yes':
                    print(f"{name.title()} you qualify for {college_name.title()} University!\n")
                   
        
            elif response.lower() == 'no':
                print(f"Sorry {name.title()} you do not qualify for " + 
                f"{college_name.title()} university.\n")
                sys.exit()
        
        elif response.lower() == 'no':
            print(f"Sorry {name.title()} you do not qualify for " + 
                 f"{college_name.title()} university.\n")
            sys.exit()
    
    
    elif response.lower() == 'no':
        print(f"Sorry {name.title()} you do not qualify for " + 
              f"{college_name.title()} university.\n")
        sys.exit()
    

    
else:
    
    is_a_local = False
    has_scholarship = False
    gpa_requirement = False
    
    response = input(f"{name.title()} are you from Oregon?\n")
    
    if response.lower() == 'yes':
        is_a_local = True
        
        response = input("Do you have a gpa of 3.0 or higher?\n")
        
        if response.lower() == 'yes':
            gpa_requirement = True
        
        elif response.lower() == 'no':
            print(f"Sorry {name.title()} you do not qualify for " + 
                  f"{college_name.title()} university.\n")
            sys.exit()
    
    if is_a_local == True and gpa_requirement == True:
        print(f"{name.title()} you qualify for {college_name.title()} University!\n")
  
    
    if response.lower() == 'no':
        response = input(f"{name.title()} do you have an out of state scholarship?\n")
        
        if response.lower() == 'yes':
            has_scholarship = True
            gpa_requirement = True
            
            if has_scholarship == True and gpa_requirement == True:
                print(f"{name.title()} you qualify for {college_name.title()} University!\n")
                
            
        elif response.lower() == 'no':
            print(f"Sorry {name.title()} you do not qualify for " + 
                  f"{college_name.title()} university.\n")
            sys.exit()



student_top_gpa = [4.0, 3.8, 3.8, 4.0, 3.9, 3.79, 3.5]

if student_top_gpa[0] != 4.0:
    print("the first gpa in the list is not a 4.0")
else:
    print("the first item in the list is a 4.0\n")

if student_top_gpa[1] == student_top_gpa[2]:
    print("these two gpas are equal to one another.\n")
else:
    print("they are not equal to each other.\n")

if student_top_gpa[0] > student_top_gpa[-1]:
    print("the gpa at the beginning of the list is greater than the one at the end of the list.\n")
else:
    print("the gpa at the end of the list is greater than the one at the beginning of the list.\n")

if '4.0' in student_top_gpa:
    print("atleast one person has a gpa of 4.0\n")
else:
    print("no one has a gpa of 4.0.\n")

if '3.0' not in student_top_gpa:
    print("no one has a gpa of 3.0\n") 
            
        
    
   


        
        
 