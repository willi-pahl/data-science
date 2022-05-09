import todo_lib.dataobject as daob

class SimpleTodo:
    dataObject = None
    
    def __init__(this):
        this.dataObject = daob.DataObject()
        this.dataObject.insert({'desc':'Start EA3 in data science', 'done': 0})
        this.dataObject.insert({'desc':'Submit EA2 in data science', 'done': 1})
        this.dataObject.insert({'desc':'Completing a first draft in scientific seminar', 'done': 0})
        this.getAllTodos()

    def run(this):
        while (True):
            select = input('select your next action:')
            if (select == '1'):
                this.addTodo()
            elif (select == '2'):
                this.updateTodo()
            elif (select == '3'):
                this.deleteTodo()
            elif (select == '4'):
                print('Bye bye')
                return

    def addTodo(this):
        desc = input('Description:')
        this.dataObject.insert({'desc': desc, 'done': 0})
        this.getAllTodos()
        return

    def updateTodo(this):
        id = input('Todo ID:')
        desc = input('Description (empty for not update):')
        done = input('Insert [y] todo is done:')

        object = this.dataObject.select(int(id))
        object['id'] = int(id)
        if desc != '':
            object['desc'] = desc
        if done == 'y':
            object['done'] = 1
        else:
            object['done'] = 0
        
        print(object)

#        this.dataObject.update({'desc': desc, 'done': done, 'id': id})

        this.getAllTodos()
        return

    def deleteTodo(this):
        id = input('Todo ID:')
        object = this.dataObject.delete(int(id))
        this.getAllTodos()
        return

    def getAllTodos(this):
        this.dataObject.selectAll()
        print('Select the next action, enter number: create Todo: 1, update Todo: 2, delete Todo: 3 or exit: 4')