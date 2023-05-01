import os

runProgram = True
todoList = []


#Funcion para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("")
    print("Por favor seleccione una opcion")
    print("")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")

#funcion para mostrar todas las tareas
def showTodoList():
    global todoList
    print()
    print()
    print("*****************************")
    for todo in todoList:
        print(f"{todoList.index(todo) + 1}. {todo}")
    print("*****************************")
    print()
    print()

#Funcion para guardar las varibales
def createTodo():
    os.system("cls")
    global todoList
    print("Crear una nueva tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")
    todoList.append(todo)
    #Mostra la lista de tareas
    showTodoList()

#Funcion para marcar tarea como hecha
def updateTodo():
    global todoList
    print("Actualizar una tarea")
    todoId = int(input("Ingresa el numero de tarea que quieres marcar como hecha: "))
    todoList[todoId - 1] = todoList[todoId - 1] + "✅"
    showTodoList()

#Funcion que nos permite borrar una tarea
def deleteTodo():
    global todoList
    print("Borrar una tarea")
    todoId = int(input("Ingresa el numero de la tarea que deseas borrar: "))
    del todoList[todoId - 1]
    showTodoList()

def main():
    global runProgram
    print(".: WELCOME TO A PYTHON TO DO LIST :.")
    flag = True 
    
    while runProgram:
        while flag:
            showMenuOptions() #Invocamos la funcion del menu
            option = int(input("Ingresa el numero de la opcion: "))
            match option:
                case 1: 
                    createTodo()
                case 2: 
                    updateTodo()
                case 3:
                    deleteTodo()
                case 4:
                    print("Hasta luego!")
                    runProgram = False
                    flag = False
                case _:
                    print("Opcion no reconocida. Ingresa una opcion valida")
        
    
if __name__ == "__main__":
    main()