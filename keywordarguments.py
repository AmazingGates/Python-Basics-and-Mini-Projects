# Keyword Arguments - Arguments that are preceded by an identifier when we pass them to a function. 
# The order of the arguments doesn't matter. Unlike positional arguments, Python knows the names of the
#arguments that our function receives.
def family(husband, wife, baby):
    print("These are the members of the Casa De Gates: " + husband + " " + wife + " " + "and " + baby,)

family(baby="Bam Bam", husband="Brian", wife="Alia",) # With the keywprd arguments, it doesn't matter how I 
#enter the arguments into the family(), they will return in the order in which the parameters are set.                                                     
