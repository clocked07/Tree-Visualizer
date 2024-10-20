#!/bin/bash

for file in *.dot
do
    filename="${file%.dot}$"
    dot -Tpdf "$file" -o "{$filename}.pdf"
    echo "Converted file {$filename}"

done
