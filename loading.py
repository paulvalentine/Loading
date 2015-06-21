# module to calculate loading on structures

import xlrd

class BasicLoading:
    def __init__(self, loads, refs):
        self.loads=loads
        self.refs=refs # and array of strings to reference the components
        self.nature=loads[0] # first element in the array to be a string to give nature

    def results(self):
        text='The basic {} loadings used in the design are:'.format(self.nature)
        for i in range(1,len(self.loads)):
            text=text+'\n{} = {} kN/m2'.format(self.refs[i-1],self.loads[i])

        return text+'\n'

class Udl:
    def __init__(self, loads, lengths): # loads here is the full object from basic loading
        self.load = self.calc_load(loads.loads,lengths)
        self.ref = lengths[0] # first element of the array to be a string to reference the loading
        self.nature = loads.nature

    # method for calculating the udl
    def calc_load(self, loads, lengths):
        ld = 0
        for i in range(1, len(loads)):
            ld = ld + loads[i]*lengths[i]


        return ld




class Point:

        def __init__ (self,udl,span, ref):
            self.span = span
            self.udl = udl
            self.dead_reaction = udl.calc_dead_load()*span/2
            self.imposed_reaction = udl.calc_imposed_load()*span/2
            self.sls_reaction = udl.calc_sls_load()*span/2
            self.uls_reaction = udl.calc_uls_load()*span/2
            self.ref = ref

        def report (self):
            a = '''Load ref: {}
For a load length of {} m supporting gk = {} kN/m & qk = {} kN/m (ref: {})
The dead reaction = {} kN
The imposed reaction = {} kN
The sls reaction = {} kN
The uls reaction = {} kN \n
'''.format(self.ref,self.span, self.udl.calc_dead_load(),self.udl.calc_imposed_load(),self.udl.ref,self.dead_reaction,self.imposed_reaction,self.sls_reaction,self.uls_reaction)
            return a