#!/bin/bash

seq 1 1000 | parallel 'python search.py > output/"out"{}.txt'
