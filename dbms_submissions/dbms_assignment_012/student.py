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
        connection=sqlite3.connect("students.sqlite3")
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
            
            
            
            
            
            

    
            
        
        
        
        
        
        
        
        
        