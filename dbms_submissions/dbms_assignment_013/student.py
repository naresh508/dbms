class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.student_id=None
        self.age=age
        self.score=score
    
    @staticmethod
    def get(student_id=0,name='',age=0,score=-1,**kwargs):
        
        if student_id>0:
            Q=read_data("select * from Student where student_id={}".format(student_id))
        elif age>0:
            Q=read_data("select * from Student where age={}".format(age))
        elif score>0:
            Q=read_data("select * from Student where score={}".format(score))
        elif name!='':
            Q=read_data("select * from Student where name='{}'".format(name))
        else:
            raise InvalidField
        
        if len(Q)==0:
            raise DoesNotExist
            
        elif len(Q)>1:
            raise MultipleObjectsReturned
        else:
            output=Student(Q[0][1],Q[0][2],Q[0][3])
            output.student_id=Q[0][0]
            return output
            
    def delete(self):
        Q="delete from Student where student_id={}".format(self.student_id)
        write_data(Q)
        
    def save(self):
        import sqlite3
        connection=sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if self.student_id==None:
            q="insert into Student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(q)
            self.student_id=crsr.lastrowid
        else:
            # if self.checking(self.student_id):
            #     crsr.execute(f"UPDATE Student set name='{self.name}',age={self.age},score={self.score} where student_id={self.student_id}")
            # else:
            if self.checking(self.student_id):
                crsr.execute(f"UPDATE Student set name='{self.name}',age={self.age},score={self.score} where student_id={self.student_id}")
            else:
                crsr.execute(f"insert OR REPLACE into Student(student_id,name,age,score) values ({self.student_id},'{self.name}',{self.age},{self.score})")
                    
                
        connection.commit()
        connection.close()  
        
    
    def checking(self,student_id):
        q=read_data("select student_id from Student where student_id={}".format(self.student_id))
        if len(q)!=0:
            return True
        else:
            return False
    
    
    @classmethod    
    def filter(cls,**kwargs):
        
        fields_list=['student_id','name','age','score']
        
        for key,value in kwargs.items():
            k=key
            v=value
            field=k.split("__") 
            
            if (field[0] not in fields_list):
             raise InvalidField
        
            elif k in fields_list:
                if field[0]!='name':
                    query=(f"select * from student where {k}={v}")
                else:
                    query=(f"select * from student where {field[0]}='{v}'")
                record=read_data(query)
            
            elif field[0] in fields_list and field[1]=='lt':
                query=(f"select * from student where {field[0]}<{v}")
                record=read_data(query)
            
            elif field[0] in fields_list and field[1]=='lte':
                query=(f"select * from student where {field[0]}<={v}")
                record=read_data(query)        
                
            elif field[0] in fields_list and field[1]=='gt':
                query=(f"select * from student where {field[0]}>{v}")
                record=read_data(query)   
                
            elif field[0] in fields_list and field[1]=='gte':
                query=(f"select * from student where {field[0]}>={v}")
                record=read_data(query)    
                
            elif field[0] in fields_list and field[1]=='neq':
                if field[0]!='name':
                    query=(f"select * from student where {field[0]}!={v}")
                else:
                    query=(f"select * from student where {field[0]}!='{v}'")
                record=read_data(query) 
            
            elif field[0] in fields_list and field[1]=='in':
                query=(f"select * from student where {field[0]} in {tuple(v)}")
                record=read_data(query)  
                
            elif field[0] in fields_list and field[1]=='contains':
                query=(f"select * from student where {field[0]} like '%{v}%'")
                record=read_data(query)                                   
            
            records_list=[]
            
            if len(record)>0:
                for i in record:
                    result=Student(i[1],i[2],i[3])
                    result.student_id=i[0]
                    records_list.append(result)
            else:
                return records_list
    
        return records_list        
            
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)  



def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans            
            
#selected_students = Student.filter(age=40)
#Student.filter(year=80)
#selected_students = Student.filter(age=34, name="Jesse Couch")
#selected_students = Student.filter(age__lt=30)
#selected_students = Student.filter(age__lte=30)
#selected_students = Student.filter(score__gt=80)
#selected_students = Student.filter(age__neq=34)
#print(selected_students)


            
            
            
            
        
        
        
        

                        