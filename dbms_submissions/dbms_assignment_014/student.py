class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.student_id=None
        self.age=age
        self.score=score
    
    @staticmethod    
    def filter(**kwargs):
        
        fields_list=['student_id','name','age','score']
        records_list=[]
        
        for key,value in kwargs.items():
            k=key
            v=value
            field=k.split("__") 
            
            if (field[0] not in fields_list):
             raise InvalidField
        
            elif k in fields_list:
                if field[0]!='name':
                    query=(f"{k}={v}")
                else:
                    query=(f"{field[0]}='{v}'")
            
            elif field[1]=='lt':
                query=(f"{field[0]}<{v}")
            
            elif field[1]=='lte':
                query=(f"{field[0]}<={v}")
                
                
            elif field[1]=='gt':
                query=(f"{field[0]}>{v}")
                
                
            elif field[1]=='gte':
                query=(f"{field[0]}>={v}")
                
                
            elif field[1]=='neq':
                if field[0]!='name':
                    query=(f"{field[0]}!={v}")
                else:
                    query=(f"{field[0]}!='{v}'")
                 
            
            elif field[1]=='in':
                query=(f"{field[0]} in {tuple(v)}")
                 
                
            elif field[1]=='contains':
                query=(f"{field[0]} like '%{v}%'")
            
                      
            records_list.append(query)
        l=' and '.join(records_list)
        return l
    
        
    @classmethod
    def avg(cls, field, **kwargs):
        
        p=['student_id','name','age','score']
        
        if (field not in p):
            raise InvalidField
        
        elif len(kwargs)==0:
            query=f"select avg({field}) from student"
        
            
        else:
            q=Student.filter(**kwargs)
            query=(f"select avg({field}) from student where {q}")
        record=read_data(query)
        return record[0][0]    
            
        
            
            
    @classmethod
    def min(cls, field, **kwargs):
        p=['student_id','name','age','score']
        
        if (field not in p):
            raise InvalidField
            
        elif len(kwargs)==0:
            query=f"select min({field}) from student"
        
            
        else:
            q=Student.filter(**kwargs)
            query=(f"select min({field}) from student where {q}")
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def max(cls, field, **kwargs):
        p=['student_id','name','age','score']
        
        if (field not in p):
            raise InvalidField
        
            
        elif len(kwargs)==0:
            query=f"select max({field}) from student"
            
        else:
            q=Student.filter(**kwargs)
            query=(f"select max({field}) from student where {q}")
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def sum(cls, field, **kwargs):
        p=['student_id','name','age','score']
        
        if (field not in p):
            raise InvalidField
            
        elif len(kwargs)==0:
            query=f"select sum({field}) from student"
            
        else:
            q=Student.filter(**kwargs)
            query=(f"select sum({field}) from student where {q}")
        record=read_data(query)
        return record[0][0]
    
    @classmethod
    def count(cls, field=None, **kwargs):
        p=['student_id','name','age','score']
        if field==None:
            query="SELECT count() FROM Student"
        elif (field not in p):
            raise InvalidField
            
        elif len(kwargs)==0:
            query=f"select count({field}) from student"
            
        else:
            q=Student.filter(**kwargs)
            query=(f"select count({field}) from student where {q}")
        record=read_data(query)
        return record[0][0]    
            
                
        
    '''@classmethod
    def avg(cls, field, **kwargs):
        
        fields_list=['student_id','name','age','score']
        
        for key,value in kwargs.items():
            
            k=key
            v=value
            q=k.split("__") 
            
            if (q[0] not in fields_list):
                raise InvalidField
            
            elif q[0] in fields_list and q[1]=='lt':
                query=(f"select avg({field}) from student where {q[0]}<{v}")
                record=read_data(query)
                
            elif q[0] in fields_list and q[1]=='lte':
                query=(f"select avg({field}) student where {q[0]}<={v}")
                record=read_data(query)        
                
            elif q[0] in fields_list and q[1]=='gt':
                query=(f"select avg({field}) from student where {q[0]}>{v}")
                record=read_data(query)   
                
            elif q[0] in fields_list and q[1]=='gte':
                query=(f"select avg({field}) from student where {q[0]}>={v}")
                record=read_data(query)    
            
            elif q[0] in fields_list and q[1]=='neq':
                query=(f"select avg({field}) from student where {q[0]}!={v}")
                record=read_data(query) 
            
            elif q[0] in fields_list and q[1]=='in':
                query=(f"select avg({field}) from student where {q[0]} in {tuple(v)}")
                record=read_data(query)  
                
            elif q[0] in fields_list and q[1]=='contains':
                query=(f"select avg({field}) from student where {q[0]} like '%{v}%'")
                record=read_data(query)     
             
        return record''' 
        
    '''
    @classmethod
    def filter(cls,**kwargs):
        dict={'lt':'<','lte':'<=','gt':'>','gte':'>=','neq':'!=','in':'in','contains':''}
        for key,value in kwargs.items():
            k=key.split('__')
            f=['student_id','name','age','scor']
            if k[0] not in f:
                raise InvalidField
                
    '''
    
        
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans        
	
#avg_age = Student.avg('age')
#print(avg_age)