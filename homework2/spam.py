spam_corpus = [["i", "am", "spam", "spam", "i", "am"], ["i", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
combined_corpus = ["i", "am", "spam", "spam", "i", "am", "i", "do", "not", "like", "that", "spamiam", "do", "i",
                    "like", "green", "eggs", "and", "ham", "i", "do"]
combined_corpus = list(dict.fromkeys(combined_corpus))

hash_spam = {}
for i in spam_corpus:
    for j in i:
        if j not in hash_spam:
            hash_spam[j] = 1
        else:
            hash_spam[j] += 1

hash_ham = {}
for i in ham_corpus:
    for j in i:
        if j not in hash_ham:
            hash_ham[j] = 1
        else:
            hash_ham[j] += 1

hash_prob = {}
for i in combined_corpus:
    g = 0;
    b = 0;
    if i in hash_ham:
        g = 2 * hash_ham[i]
    if i in hash_spam:
        b = hash_spam[i]
    if g + b >= 1:
        hash_prob[i] = max(0.1,
                           min(.99,
                               min(1.0, b / len(spam_corpus)) /
                               (min(1.0, b / len(spam_corpus)) + min(1.0, g / len(ham_corpus)))))
print("Hash Table of Spam/Ham Corpus: ")
for i in hash_prob:
    print(i, hash_prob[i])
# Test spam e-mail
test_spam = ["i", "like", "spam", "i", "do", "not", "like", "ham"]
# Test ham e-mail
test_ham = ["i", "like", "ham", "i", "do", "not", "love", "eggs"]


def spam_test(message):
    prod = 1
    prod_complement = 1
    for i in message:
        if i in hash_prob:
            prod *= hash_prob[i]
            prod_complement *= 1 - hash_prob[i]
        else:
            prod *= 0.4
            prod_complement *= 0.6

    prob = prod / (prod + prod_complement)
    return prob

print("\n")
print("Spam:", spam_test(test_spam))
print("Ham:", spam_test(test_ham))