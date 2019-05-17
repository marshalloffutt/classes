from collections import OrderedDict

glossary = OrderedDict()

glossary['loop'] = 'a method of iteration'
glossary['list'] = 'a collection of data'
glossary['indentation'] = 'when you indent something'
glossary['tuple'] = 'an immutable list'

for word, definition in glossary.items():
    if word == 'indentation':
        print(word.title() + " is " + definition + ".")
    else:
        print("A " + word + " is " + definition + ".")