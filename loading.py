# module to calculate loading on structures

class BasicLoading:
    def __init__(self, loads, refs, nature):
        self.loads=loads
        self.refs=refs
        self.nature=nature

    def results(self):
        text='The basic {} loadings used in the design are:'.format(self.nature)
        for i in range(0,len(self.loads)):
            text=text+'\n{} = {} kN/m2'.format(self.refs[i],self.loads[i])

        return text+'\n'

class Udl:
    def __init__(this, basicdead, basicimposed, lengths, ref):
        this.basic_loading_dead = basicdead
        this.basic_loading_imposed = basicimposed
        this.load_lengths = lengths
        this.dead_load = this.calc_load(basicdead,lengths)
        this.imposeed_load = this.calc_load(basicimposed,lengths)
        this.imposed_load=this.calc_imposed_load()
        this.ref = ref

    def calc_load(this, loads, lengths):

        # could do with a error check on the length of the array
        load =0;
        for i in range(0,len(loads)):
            load = load + loads[i]*lengths[i]
        return load
        



    def report(self):

        a = '''Load ref:{}
The dead load = {} kN/m
The imposed load = {} kN/m
The sls load = {} kN/m
The uls load = {} kN/m \n
'''.format(self.ref,self.calc_dead_load(),self.calc_imposed_load(),self.calc_sls_load(),self.calc_uls_load())
        return a

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