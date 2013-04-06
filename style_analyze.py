texts = []
for i in range(1, 31):
    f = open('%d.txt' % i)
    texts.append(f.read().strip())
    f.close()

def average_word_length(txt):
    total = 0
    words = txt.split()
    for word in words:
        total += len(word)
    return total / (len(words) * 1.0)
    
def average_sentence_length(txt):
    total = 0
    words = txt.split()
    num_sentences = 0
    curr_count = 0
    for word in words:
        if len(word) > 0 and word[-1] == '.':
            total += curr_count
            curr_count = 0
            num_sentences += 1
        else:
            curr_count += 1
    if curr_count > 0:
        total += curr_count
        num_sentences += 1
    return total / (num_sentences * 1.0)
    
import nltk
import string
    
def part_of_speech_prop(txt):
    tagged = nltk.pos_tag(nltk.word_tokenize(txt))
    num_nouns, num_verbs, num_adj, num_adv = 0,0,0,0
    num_words = 0
    for word, pos in tagged:
        if pos[0] in string.uppercase:
            num_words += 1
        if pos[0] == 'N':
            num_nouns += 1
        if pos[0] == 'J':
            num_adj += 1
        if pos[0] == 'R':
            num_adv += 1
        if pos[0] == 'V':
            num_adj += 1
    return num_nouns / (num_words * 1.0), num_verbs / (num_words * 1.0), num_adj / (num_words * 1.0), num_adv / (num_words * 1.0)
    
f = open("OUTPUT.txt", "w")
    
def match():
    text_scores = [(average_word_length(txt), average_sentence_length(txt)) for txt in texts]
    speech_counts = [part_of_speech_prop(txt) for txt in texts]
    all_num = range(30)
    matches = list()
    while len(all_num) > 0:
        ind1 = all_num[0]
        best_score = 38190283129038
        best_ind = ind1
        for ind2 in all_num[1:]:
            score = abs(text_scores[ind1][0] - text_scores[ind2][0]) + 5 * abs(text_scores[ind1][1] - text_scores[ind2][1])
            score += 1000 * abs(speech_counts[ind1][0] - speech_counts[ind2][0])
            score += 1000 * abs(speech_counts[ind1][1] - speech_counts[ind2][1])
            score += 1000 * abs(speech_counts[ind1][2] - speech_counts[ind2][2])
            score += 1000 * abs(speech_counts[ind1][3] - speech_counts[ind2][3])
            if score < best_score:
                best_ind = ind2
                best_score = score
        matches.append((ind1+1, best_ind+1))
        f.write("%d.txt,%d.txt\n" % (ind1+1, best_ind+1))
        all_num.remove(ind1)
        all_num.remove(best_ind)
    return matches
    
print match()
f.close()