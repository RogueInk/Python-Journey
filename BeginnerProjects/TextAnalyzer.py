# 8. Text Statistics Analyzer
# Features: Word count, Character count, Most common word, Longest word
# Concepts: Strings, Dictionaries, Sorting
import string

# Renamed to text_data because it contains phrases, not a single word
text_data = [
    "PseudoCode", "Analyzer", "Formation", "Perfy", 
    "Rigged Up Shit", "Shit is Crazy", "Code", "Coder", 
    "shit", "Code", "Rigged Shit not peak Code"
]

# --- CORE ENGINE FUNCTIONS ---

def get_clean_words():
    """Sanitizer: Flattens phrases into a clean list of lowercase, punctuation-free words."""
    clean_words = []
    for phrase in text_data:
        # Remove punctuation by replacing it with nothing
        translator = str.maketrans('', '', string.punctuation)
        clean_phrase = phrase.translate(translator)
        
        # Split by spaces and convert to lowercase
        words = clean_phrase.lower().split()
        clean_words.extend(words)
    return clean_words

def get_character_count(include_spaces=False):
    """Calculates total characters across all text."""
    total = 0
    for phrase in text_data:
        if not include_spaces:
            # Replace spaces with nothing before counting
            phrase = phrase.replace(" ", "")
        total += len(phrase)
    return total

def get_most_common_word():
    """Uses a dictionary to count occurrences of each word."""
    words = get_clean_words()
    word_counts = {}
    
    # Tally up the words
    for w in words:
        if w in word_counts:
            word_counts[w] += 1
        else:
            word_counts[w] = 1
            
    # Find the key (word) with the highest value (count)
    if not word_counts:
        return "No words found."
    
    most_common = max(word_counts, key=word_counts.get)
    return f"'{most_common}' (appears {word_counts[most_common]} times)"

def get_longest_word():
    """Sorts the clean words by length and returns the longest."""
    words = get_clean_words()
    if not words:
        return "No words found."
    
    # max() using len as the sorting key
    longest = max(words, key=len)
    return f"'{longest}' ({len(longest)} characters)"

# --- MAIN LOOP ---

while True:
    print("\n===== Text Statistic Analyzer =====")
    print("1. Total Word Count (Actual Words)")
    print("2. Total Character Count (No Spaces)")
    print("3. Print Character Count of a specific word")
    print("4. Most Common Word")
    print("5. Longest Word in the list")
    print("6. Exit")
    
    choice = input("Enter Your Choice: ").strip()
    
    if choice == "1":
        actual_words = get_clean_words()
        print(f"✅ Total Words: {len(actual_words)}")
        
    elif choice == "2":
        chars = get_character_count(include_spaces=False)
        print(f"✅ Total Characters: {chars}")
        
    elif choice == "3":
        target = input("Type a word to count its characters: ").strip()
        print(f"✅ The word '{target}' has {len(target)} characters.")
        
    elif choice == "4":
        common = get_most_common_word()
        print(f"✅ Most Common: {common}")
        
    elif choice == "5":
        longest = get_longest_word()
        print(f"✅ Longest Word: {longest}")
        
    elif choice == "6":
        print("Exiting Analyzer. Goodbye!")
        break
        
    else:
        print("⚠️ Invalid choice. Please try again.")