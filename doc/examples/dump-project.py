import pyhuml
import sys
import pprint
pprint.pprint(pyhuml.loads(open(sys.argv[1],'r').read()))
