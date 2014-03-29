#!/bin/bash

outdir=$1
export outdir

seq 1 1000 | parallel --env outdir 'python search.py > $outdir/"out"{}.txt; sleep 5'

