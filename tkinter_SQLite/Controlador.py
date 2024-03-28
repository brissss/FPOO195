from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex=sqlite3.connect("/Users/brissgarcia/Documents/GitHub/FPOO195/tkinter_SQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def encriptapass(self,cont):
        passPlana= cont
        passPlana= passPlana.encode()
        sal= bcrypt.gensalt()
        passHash= bcrypt.hashpw(passPlana, sal)
        
        
        return passHash
    
    def insertUsuario(self, nom, corr, cont):
        conexion= self.conexion() #Se declara la variable a la cual se le vincula el metodo que conecta a la base de datos 
        if (nom== "" or corr== "" or cont== ""):
            messagebox.showwarning("Cuidado","Inputs vacios")
            conexion.close()
            
        else:
            cursor= conexion.cursor()
            conH= self.encriptapass(cont)
            datos= (nom,corr,conH)
            sqlInsert= "insert into tbUsuarios(nombre, correo, contra) values(?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito", "Eso tilin!!!!")
    
    def buscarUsuario(self,id):
        conexion = self.conexion()
        if (id == ""):
            messagebox.showwarning("Cuidado","Ingrese un ID valido")
            conexion.close()
        else:
            try:
                cursor = conexion.cursor()
                sqlSelect= "select * from tbUsuarios where id=" + id
                cursor.execute(sqlSelect)
                usuario = cursor.fetchall()
                conexion.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la busqueda")


    def mostrarTodosUsuarios(self):
        conex = self.conexion()
        cursor = conex.cursor()
        try:
            cursor.execute("select * from tbUsuarios")
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError:
            print("Error", "No hay registros")
            conex.close()
            return []