def word_search(doc_list, keyword): 
    """ 
    Takes a list of documents (each document is a string) and a keyword.  
    Returns list of the index values into the original list for all documents  
    containing the keyword. 
    Example: 
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"] 
    >>> word_search(doc_list, 'casino') 
    >>> [0] 
    """ 
    indexes=[]
    i=0
    while i < len(doc_list):
        s_list=doc_list[i]
        s_list=s_list.lower()
        s_list=s_list.replace(".","").replace("?","")
        # Here we have the strings without . or ?, but if we use in Casino is present in Casinoville, we have to work with list to use in
        words=s_list.split()
        # Using lists when we use in it only matches if a exactly match is found
        if keyword in words:
            indexes.append(i)
        i+=1
    print(indexes)
    return indexes

# Example doc_list works    
doc_list = ["The Learn Python Challenge Casino.?", "They bought a car", "Casinoville"] 
word_search(doc_list, 'casino')

def multi_word_search(doc_list, keywords): 
    """ 
    Takes list of documents (each document is a string) and a list of keywords.   
    Returns a dictionary where each key is a keyword, and the value is a list of indices 
    (from doc_list) of the documents containing that keyword 
    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"] 
    >>> keywords = ['casino', 'they'] 
    >>> multi_word_search(doc_list, keywords) 
    {'casino': [0, 1], 'they': [1]} 
    """ 
    dictionary={}
    for key in keywords:
        dictionary[key]=word_search(doc_list,key)
    print(dictionary)

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"] 
keywords = ['casino', 'they'] 
multi_word_search(doc_list, keywords) 
