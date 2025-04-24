from textblob import TextBlob
print("welcome to the AI mood detector")
name=input("whats your name")
print("nice to meet you ",name)
print("lets find out the sentiments of your sentences, type 'exit' to quit \n")
while True:
    sentence=input("enter your sentence:")
    if sentence.lower()=="exit":
        print("goodbye", name)
        break
    blob=TextBlob(sentence)
    sentiment=blob.sentiment.polarity
    if sentiment>0:
        print("positive sentiment detected. \n")
    elif sentiment<0:
        print("negative sentiment detected .\n")
    else:
        print("neutral sentiment detected")
    