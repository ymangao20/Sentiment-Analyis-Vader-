from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

obj = SentimentIntensityAnalyzer()

sentence = "Ram is really good "
sentiment_dict = obj.polarity_scores(sentence)
print(sentiment_dict)

sentence = "Rahul is really bad"
sentiment_dict = obj.polarity_scores(sentence)
print(sentiment_dict)

#with punctuations
print(obj.polarity_scores('Ram is good boy'))
print(obj.polarity_scores('Ram is good boy!'))
print(obj.polarity_scores('Ram is good boy!!'))
#with capitalizations
print(obj.polarity_scores('Ram is good'))
print(obj.polarity_scores('Ram is GOOD'))
#degree modifiers
print(obj.polarity_scores('Ram is good'))
print(obj.polarity_scores('Ram is very good'))
#with conjuctions
print(obj.polarity_scores('Ram is good'))
print(obj.polarity_scores('Ram is good,but he is also naughty sometimes'))
#slangs and emoticons
print(obj.polarity_scores("That Hotel"))
print(obj.polarity_scores("That Hotel : )"))