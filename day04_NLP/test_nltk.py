import nltk
import nltk.tokenize as tk

# nltk.download()

with open("An article.txt","rb") as f:
    data = f.read()
    data = data.decode()

    sents = tk.sent_tokenize(data)
    for i in range(len(sents)):
        print(i + 1, ":", sents[i])