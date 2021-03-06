def in_blocklist(blocklist, sentence):
    for entry in blocklist:
        if entry in sentence:
            return True
        
    return False


def save_all(filename, authors):
    file = open(filename, 'w')
    for author, sentences in authors.iteritems():
        for sentence in sentences:
            file.write(author + ': ' + sentence)
            file.write('\n')

    file.close()
    print('Saved to ' + filename)
    
def save_posts(filename, posts):
    file = open(filename, 'w', encoding='utf-8')
    for post in posts:
        file.write(post)
        file.write('\n')
    file.close()
    print('Saved to ' + filename)