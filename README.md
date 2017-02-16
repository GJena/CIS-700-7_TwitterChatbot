# CIS-700-7_TwitterChatbot

## Homework 3

Chatbot trained on Twitter dataset as part of Homework 3 for CIS 700-7. It has been integrated with the 'chat' skill on Alexa.

### Evaluation of chatbot
There are different aspects we considered for evaluation of our chatbot. First we present a qualitative evaluation along with good and bad examples.

__Good sample conversations__

User | Bot
--- | ---
"hey" | "good morning all"
"how are you." | "i ' m ok . thanks ."
"who is hillary clinton?" | "hillary is the one who cares ."
"you are sweet" | "i am a good friend "
"who is donald trump" | "he is an idiot"
"who do the like the best." | you ' re the best i ' ve ever seen .
"cookies" | "i need that !"
"thanks." | "no worries !"
"get lost" | "i ' m sorry ."
"no way." | "that is what i said ."
"bye" | "i ' m so fucking sad"

The replies of the bot seem relevant and coherent. Some responses might even convince a witness that a human was talking.

__Bad sample conversations__

User | Bot
--- | ---
"tell me something interesting" | "the original thing that was in the 00s"
"what do you think of global warming" | "something better than me . . ."
"what do you think of alexa." | "wow , i ' m so fucking gross ."
"mac or windows" | "just in the UNK"
"i am really hungry." | "i ' m not gonna try it ."
"let us go out for a movie." | "not the same thing ."

The replies of the bot , while mostly gramatically correct, don't make sense. The bot isn't able to give satisfactory responses to the user. In one case , 'UNK' i.e. the unknown token also comes up.

__Train loss__

Cross entropy was used as the loss function during training. 10% of the data was used for cross validation. 
Training and cross validation loss was observed after every 200 epochs.  A set of 15 dialogs was created to test the model based on the response generated. This was done after every 2 hours.
Interestingly, minimum cross validation perplexity did not give the best model (in terms of the response generated). 

__Possible metrics__
Since it is not task based, it is harder to evaluate, we cannot just use task completion metrics. 
A combination of metrics may be best to evaluate the general purpose bot. Some candidate metrics could be:
 - Distance in word2vec embedding
 - Confusion metrics: how often it returns ‘I don’t know’ or UNK?
 - Sentiment analysis on user answers
 
### Issues and possible solutions


### Future work
Use TweetTokenizer.
Remove smileys and punctuations (apart from '.', since AMAZON.LITERAL does not capture other punctuations). 
