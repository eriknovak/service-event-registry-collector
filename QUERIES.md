# Query Examples

This file contains examples of Event Registry queries. Feel free to change them
to fit your needs.



### Events about Luka Dončič (basketball player)

```bash
# get the events mentioning Luka Dončić (basketball player)
python -m collector \
    --max_repeat_request=5 \
    events \
    --concepts="Luka Dončić" \
    --languages=eng,slv \
    --date_start=2021-01-01 \
    --save_to_file=./data/events_sport_luka_doncic.jsonl

# get the articles of the events acquired with the above command
python -m collector \
    --max_repeat_request=5 \
    event_articles_from_file  \
    --event_ids_file=./data/events_sport_luka_doncic.jsonl \
    --save_to_file=./data/events_sport_luka_doncic
```



### Events about blockchain

```bash
# get the events mentioning blockchain
python -m collector \
    --max_repeat_request=5 \
    events \
    --concepts="blockchain" \
    --languages=eng,slv \
    --date_start=2021-01-01 \
    --save_to_file=./data/events_tech_blockchain.jsonl

# get the articles of the events acquired with the above command
python -m collector \
    --max_repeat_request=5 \
    event_articles_from_file  \
    --event_ids_file=./data/events_tech_blockchain.jsonl \
    --save_to_file=./data/events_tech_blockchain
```


### Events about journalism

```bash
# get the events mentioning journalism
python -m collector \
    --max_repeat_request=5 \
    events \
    --concepts="journalism,politics" \
    --languages=eng,slv \
    --date_start=2021-01-01 \
    --save_to_file=./data/events_politics_journalism.jsonl

# get the articles of the events acquired with the above command
python -m collector \
    --max_repeat_request=5 \
    event_articles_from_file  \
    --event_ids_file=./data/events_politics_journalism.jsonl \
    --save_to_file=./data/events_politics_journalism
```