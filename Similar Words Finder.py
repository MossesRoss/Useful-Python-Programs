from nltk.corpus import wordnet as wn

def find_similar_words(target_word, txt_file):
  """
  Finds words similar to the target word in the given txt file.

  Args:
    target_word: The word to find similar words for.
    txt_file: The path to the text file.

  Returns:
    A list of similar words found in the text file.
  """
  similar_words = []
  with open(txt_file, 'r') as f:
    text = f.read()
      
  words = text.lower().split()

  # Find synonyms and lemmas for the target word
  for synset in wn.synsets(target_word):
    for lemma in synset.lemmas():
      # Check if the lemma is in the text and not the target word itself
      if lemma.name().lower() in words and lemma.name().lower() != target_word:
        similar_words.append(lemma.name())

  return similar_words

# Example usage
target_word = "love"
txt_file = "my_text.txt"

similar_words = find_similar_words(target_word, txt_file)

if similar_words:
  print("Similar words for", target_word, ":", ", ".join(similar_words))
else:
  print("No similar words found for", target_word)
