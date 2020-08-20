import praw
import json
import acc
#refer: https://praw.readthedocs.io/en/latest 

def initialize_reddit():
	#global con
	con = praw.Reddit(username= acc.username, 
					  password= acc.password,
					  client_id = acc.client_id,
					  client_secret = acc.client_secret,
					  user_agent = "Reddit's resident Zen Master!")
	return con

	#print("abcd")



def process(con, subreddit, trigger):
	for submission in subreddit.stream.comments():
		if trigger in comment.body:
			try:
				reply = generate_quote()
				reply_to_comment(con, comment.id, reply, 1)
				print('posted')
			except:
				print('Might be too frequent')



def reply_to_comment(con, comment_id, bot_reply, iter):
    try:
        # use reddit API to reply to comment using comment id
        user_comment = con.Comment(id= comment_id)
        user_comment.reply(bot_reply)
        print("posted")

    except Exception as e:
    	#	Reddit bars from commentting for some time
        time_remaining = 10
        #Sometimes reddit does not allow replies to come quickly
        print (str(e.__class__.__name__) + ": " + str(e))
        for i in range(time_remaining, 0, -1):
            print ("Retrying in {} seconds..", i)
            time.sleep(1)
        if (iter<3): 
        	reply_to_comment(con, comment_id, bot_reply, iter+1)



def generate_quote():
	quoteRepository = open('quote.json')
	#print(len(quoteReository))
	zen_quote = quoteRepository[random.randrange(1,len(quoteRepository),1)]
	return zen_quote	



if __name__ == "__main__":
	#global con
    con = initialize_reddit()
    #print(y[random.randrange(1,90,1)])
    trigger = "!Zen_Quote"
    subreddit = con.subreddit("all")
    process(con, subreddit, trigger)