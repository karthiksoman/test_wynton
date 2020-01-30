import os 
import sys
a = "Hello"
b = "I am Karthik"
c = [a, b]

#global scratch path
#scratch_path = '/wynton/scratch/ksoman/'

#local scratch path
scratch_path = os.environ['TMPDIR']
filename = scratch_path+'/'+sys.argv[1]
#print(filename)
#filename = scratch_path+'test_compute_node_job_out.txt'

out = open(filename, 'w')

for i in range(len(c)):
    out.write(c[i]+'\n')
out.close()

