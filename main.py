# main.py preprocessing staat er nog in!!
from model import model_code_switching

tweets = []

# start by opening the data
with open("lid_spaeng/debug.conll") as data:
    # make list of tweets, first initiate empty tweet: 
    tweet = ""
    # loop over the data
    for line in data.readlines():
        # skip if empty line
        if len(line) == 0 or line.isspace():
            continue
        # check if new tweet is starting
        if "# sent_enum = " in line:
            # This check is nessesary because I dont want the initialized empty tweet to be appended to the dataset
            if not tweet == "":
                #append previous tweet to list of tweets
                tweets.append(tweet)
                # empty tweet variable for next tweet
                tweet = ""
        # Append word to tweet
        else:
            token = line.split()[0]
            tweet = tweet + " " + token

print(tweets)
# run the model on the data
predictions, tokens = model_code_switching(tweets)
i = 0
for val in predictions:
    print(tokens[i])
    print(val)
    i += 1
