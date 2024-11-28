#!/bin/bash

awk -F, '$20!="Out of SF"' no_commas.csv > SF_only.csv

