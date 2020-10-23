# Sunset Walks

A simple script to send a text message and email to my wife about our evening walks. 

### Motivation

Each day, the sun sets at a different time, and in order to avoid our walk being too hot, too cold, too bright, or too dark, we try to leave approximately 75 minutes before sunset, as our walk takes about 1 hour. 

### Tools

- Mutt, a command line interface to access my gmail account from the terminal.
- Python's suntime library to compute the sunset based on our coordinates and local time zone.
- crontab, a file that allows for scheduling of scripts

### Method

1. Getting Mutt up and operational was by far the most challenging element of this project. After following the correct syntax in the .muttrc file, I had to add some parameters to allow for proper login, including changing my gmail account to a two factor authentification and generating a custom key for the script. 
2. The suntime library was not the first library I tried, but the first two failed because I had my coordinates as a positive instead of a negative value, because I missed the "W" vs. "E" label when I looked up my coordinates on google. I spent \~30 minutes troubleshooting and messing with date times only to find that I was consistently off by the same amount, which was the clue I needed to check my coordinates. 
3. I had to link up the bash script, and since I don't know how to pass a python script output directly to a bash script, I used "daily_message.log" as an intermediary to store the message. 
4. Finally, I set up the cron job with the correct [syntax](https://crontab.guru/#*_9_*_*_*).


## Hidden Files

The following bash script runs every morning according to the follwing files:

**file: crontab**
<pre><code>
9 \*/12 \* \* \* cd /path/to/file && ./sunset_walk.sh
</code></pre>

**file: sunset_walk.sh**
<pre><code>
python sunset_walks.py > daily_message.log 		# writes the message to the daily log for easy access
DOW=$(date +%A)
cat daily_log.log | mutt -s "${DOW} Sunset Walk Reminder" wife_email@gmail.com
cat daily_log.log | mutt -s "${DOW} Sunset Walk Reminder" wife_phone_number@vtext.com
</code></pre>

## Results:

#### Successfully sent email:

![Email](/images/jakebot_email.jpeg)

#### Successfully sent text message:

![Text Message](/images/jakebot_text.jpeg)