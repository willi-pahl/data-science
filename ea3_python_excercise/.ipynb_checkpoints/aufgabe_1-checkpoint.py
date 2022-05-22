"""This file is for EA 3 in module data science."""

import platform as pf

class EA1:
    """Class for testing Python for data science."""

    # Generate output text.
    def get_output(self, data):
        out_put = '\nHello my name is {name}. I am using the IDE {ide} on a {os}.\n\n'

        return(out_put.format(
            name = data['name'],
            ide = data['ide'],
            os = data['os'] + ' ' + data['version']
            )
        )

    # Function for generate data.
    def getDatas(self):
        return {
            'name': 'W. Pahl',
            'ide': 'Visual Studio Code',
            'os': pf.system(),
            'version': pf.release(),
        }

ea = EA1()
output = ea.get_output(ea.getDatas())

print(output)

