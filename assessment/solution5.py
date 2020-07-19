# Given:
#     A list of "employee-manager-pairs" where the first element of each pair is an employee and
#     the second element of the pair is that employee's direct manager, come up with
#     a function that can take as input two employees, say empl and emp2, and
#     returns "True" if emp2 is in emp1's chain of command and returns "False" otherwise
__author__ = 'Onyedikachi Udeh'

tuplesList = [('Worker_1','Boss_1'), 
            ('Worker_2','Boss_2'), 
            ('Boss_1','Exec_1'),
            ('Boss_2','Exec_2'), 
            ('Exec_1','Director_1'), 
            ('Exec_2','Director_2'),
            ('Director_1', 'CEO'), 
            ('Director_2', 'CEO'), 
            ('CEO', None)]

def isInChain(empl1, empl2):
    first_chain = []
    second_chain = []
    
    count = 0
    while(count <= len(tuplesList)-1):
        if(count % 2 == 0):
            for i in tuplesList[count]:
                if i not in first_chain:
                    first_chain.append(i)
        elif(count % 2 != 0):
            for i in tuplesList[count]:
                if i not in second_chain:
                    second_chain.append(i)
        count += 1

    if(empl1.upper() == "CEO"):
        if(empl2 in first_chain):
            if(first_chain.index(empl1) > first_chain.index(empl2)):
                return True
            else:
                return False  
        elif(empl2 in second_chain):
            if(second_chain.index(empl1) > second_chain.index(empl2)):
                return True
            else:
                return False
        else:
            return False
    elif(empl1 in first_chain):
        if(empl2 not in first_chain):
            return False
        else:
            if(first_chain.index(empl1) > first_chain.index(empl2)):
                return True
            else:
                return False                    
    elif(empl1 in second_chain):
        if(empl2 not in second_chain):
            return False
        else:
            if(second_chain.index(empl1) > second_chain.index(empl2)):
                return True
            else:
                return False
    else:
        print("employee not found!")
        return False


empl1 = input("Enter employee 1 : ") # first input (for the first employee )
empl2 = input("Enter employee 2 : ") # second input (for the second employee)


var = isInChain(empl1, empl2) # calling the isInChain() function with empl1 and empl2 as args
print(var) # print the returned value



###############################################################
# TEST CASE
###############################################################

###############################################################
# INPUT 1
###############################################################
# Director_1

###############################################################
# INPUT 2
###############################################################
# Boss_1

###############################################################
# OUTPUT
###############################################################
# True