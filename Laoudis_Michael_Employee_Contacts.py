# Michael Laoudis 
# 4/8/2021


#Employee Class

class Employee:
 
    #Initalize employee data fields (Name ; ID ; Department ; Title)
    
    def attributes(self, name, employee_id, department, title):
        self.name = name                                       #Initialize employee name 
        self.employee_id = employee_id                         #Initialize employee ID
        self.department = department                           #Initialize employee department
        self.title = title                                     #Initialize employee title

    #Mutator methods (Name ; ID ; Department ; Title)
        
    def set_Name(self, name):
        self.name = name
        
    def set_ID(self, employee_id):
        self.employee_id = employee_id
    
    def set_Department(self, department):
        self.department = department
        
    def set_Title(self, title):
        self.title = title
        
    # Return employee attributes (Name ; ID ; Department ; Title)
    
    def get_Name(self):
        return self.name
    
    def get_ID(self):
        return self.employee_id
    
    def get_Department(self):
        return self.department
    
    def get_Title(self):
        return self.title
    
    
    #Convert data to string
    def convString(self):
        return " Employee Name: " + self.name + " \n " + \
               " ID Number: " + str(self.employee_id) + " \n " + \
               " Department: " + self.department + " \n " + \
               " Job Title: " + self.title
    
        
    
    