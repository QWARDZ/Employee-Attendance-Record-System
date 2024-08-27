from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

class EmployeeAttendance:
    def __init__(self, name):
        self.app = Flask(name)
        
        # Connection to Database
        self.app.config['MYSQL_HOST'] = "localhost"
        self.app.config['MYSQL_USER'] = "root"
        self.app.config['MYSQL_PASSWORD'] = ""
        self.app.config['MYSQL_DB'] = "employee_db"
        self.mysql = MySQL(self.app)
        
        
#--------------------------------------------------------------------------------------------------------------------------------------        
        
    def setup_route(self):
        # Route to display all employees
        @self.app.route("/employees")
        def employees():
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM employees")
            employee_list = cursor.fetchall()
            return render_template("employee.html", employeesx=employee_list)
        
        
#--------------------------------------------------------------------------------------------------------------------------------------        
        
        # Route to add a new employee
        @self.app.route("/add_employee", methods=['GET', 'POST'])
        def add_employee():
            if request.method == 'POST':
                employee_no = request.form['employee_no']
                name = request.form['name']
                department = request.form['department']
                position = request.form['position']
                
                cursor = self.mysql.connection.cursor()
                cursor.execute("INSERT INTO employees (employee_no, name, department, position) VALUES (%s, %s, %s, %s)", (employee_no, name, department, position))
                self.mysql.connection.commit()
                return redirect(url_for('employees'))
            return render_template("add_employee.html")
        
 #--------------------------------------------------------------------------------------------------------------------------------------       
        
        # Route to update an employee
        @self.app.route("/update_employee", methods=['GET', 'POST'])
        def update_employee():
            if request.method == 'POST':
                id = request.form['id']
                employee_no = request.form['employee_no']
                name = request.form['name']
                department = request.form['department']
                position = request.form['position']
                cursor = self.mysql.connection.cursor()
                cursor.execute("UPDATE employees SET employee_no=%s, name=%s, department=%s, position=%s WHERE id=%s", (employee_no, name, department, position, id))
                self.mysql.connection.commit()
                return redirect(url_for('employees'))
            
            id = request.args.get('id')
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
            employee = cursor.fetchone()
            
            return render_template("update_employee.html", employee=employee)
        
#--------------------------------------------------------------------------------------------------------------------------------------
        
        # Route to delete an employee
        @self.app.route("/delete_employee", methods=['POST'])
        def delete_employee():
            id = request.form['id']
            if id:
                cursor = self.mysql.connection.cursor()
                cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
                self.mysql.connection.commit()
            return redirect(url_for('employees'))
        
        
#--------------------------------------------------------------------------------------------------------------------------------------
    
    def run(self):
        self.app.run(debug=True, port="3000")
    
x = EmployeeAttendance(__name__)
x.setup_route()
x.run()
