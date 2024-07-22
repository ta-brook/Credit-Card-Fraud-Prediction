# install package for data preparation
pip install -r requirements.txt

# unzip raw data 
gzip -dk data/raw_card_transdata.csv.gzip data/raw_card_transdata.csv

# split data into train and test 
python utility/split_data.py

# generate new random dataset for model monitoring scenario
python utility/generate-random-dataset.py


