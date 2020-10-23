# Sunset Walks

A simple script to send a text message and email to my wife about our evening walks. 

### Motivation

Each day, the sun sets at a different time, and in order to avoid our walk being too hot, too cold, too bright, or too dark, we try to leave approximately 75 minutes before sunset, as our walk takes about 1 hour. 

### Method

The following bash script runs every morning according to the cron job here:

**file: crontab**
<pre><code>
9 \*/12 \* \* \* cd /path/to/file && ./sunset_walk.sh
</code></pre>

**file: sunset_walk.sh**
<pre><code>
python sunset_walks.py >> sunset_walks.log 	# writes the message to the log file for my records
python sunset_walks.py > daily_log.log 		# writes the message to the daily log for easy access
DOW=$(date +%A)
cat daily_log.log | mutt -s "${DOW} Sunset Walk Reminder" wife_email@gmail.com
cat daily_log.log | mutt -s "${DOW} Sunset Walk Reminder" wife_phone_number@vtext.com
</code></pre>