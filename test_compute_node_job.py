a = "Hello"
b = "I am Karthik"
c = [a, b]

scratch_path = '/wynton/scratch/ksoman/'
# scratch_path = '/Users/ksoman/Desktop/'
filename = scratch_path+'test_compute_node_job_out.txt'

out = open(filename, 'w')

for i in range(len(c)):
    out.write(c[i]+'\n')
out.close()


