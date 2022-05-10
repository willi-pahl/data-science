import copy

class DataObject:
    """Save data in data structor without persitent save."""
    
    # Data structur.
    # {
    #     'id': integer,
    #     'desc': string,
    #     'done': integer,
    #     'delete': integer,
    # }
    items = {}
    
    # Insert data in data structur.
    def insert(this,values):
        values['id'] = len(this.items)
        this.update(values)

    # Update existing data.
    def update(this, values):
        if values['id'] == None:
            return
        this.items[values['id']] = {
            'desc': values['desc'],
            'done': values['done'],
            'delete': 0
        }

    # Delete existing data.
    def delete(this, value):
        if value == None:
            return
        if  this.items[value] == None:
            return
        this.items[value]['delete'] = 1

    # Select item.
    def select(this, id):
        return copy.copy(this.items[id])

    # Get all data in structur.
    def selectAll(this):
        print ('id \t done \t Todo')
        for item in this.items:
            if this.items[item]['delete'] == 1:
                continue
            print ('%i \t [%i] \t %s' % (item, this.items[item]['done'], this.items[item]['desc']))
        print('\n')
