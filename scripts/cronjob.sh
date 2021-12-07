#!/bin/sh

# import the bashrc configs
. ~/.bashrc

# activate the conda environment
conda activate event-registry

# go to the root of the project
cd ~/Documents/code/event-registry-collector

# get current week (specify the interval of documents to collect)
CURRENT_WEEK=`date -d "-7days" +"%Y-%m-%d"`
echo $CURRENT_WEEK

# get the events about the Slovenian EU presidency
python -m collector \
    --max_repeat_request=5 \
    events \
    --concepts="Presidency of the Council of the European Union,Slovenia" \
    --date_start=$CURRENT_WEEK \
    --save_to_file="./data/eu2021sl/$CURRENT_WEEK.jsonl"

# get the articles of the events acquired with the above command
python -m collector \
    --max_repeat_request=5 \
    event_articles_from_file  \
    --event_ids_file="./data/eu2021sl/$CURRENT_WEEK.jsonl" \
    --save_to_file="./data/eu2021sl/$CURRENT_WEEK"
