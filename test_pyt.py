import os
import pprint
env_var = os.environ
print("EV:")
pprint.pprint(dict(env_var),width=1)
