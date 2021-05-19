try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func 
           
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class helper : 
     def check_random_walk( start, n, p ) :
         fpos = random_walk( start, n, p ) 
         return (n+fpos-start) / 2

class UnitTests(unittest.TestCase) :
    def test_random_walk(self) : 
        inputs, variables = [], []
        for s in range(-2,2) : 
            for n in range(1,5) :
                for i in range(1,5) :
                    p = i*0.2
                    inputs.append((s,n,p,))
                    myvar = randomvar( n*p, variance=n*p*(1-p), vmin=0, vmax=n, isinteger=True )
                    variables.append( myvar )
        assert( check_func('check_random_walk',inputs, variables, modname=helper ) )
