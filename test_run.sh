#!/bin/bash

cd /wynton/home/baranzinilab/karthiksoman/test_wynton
. bin/activate

filename="text_file.txt" 
python3 test_compute_node_job.py $filename

cd $TMPDIR
mv $filename ~/test_wynton 
