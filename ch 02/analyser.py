import sys
import string
import argparse

# --- CONSTANTS ---
BAR_CHAR = "█"  # Student can use '████' or '*' as required

def load_and_clean_text(filepath: str):
    """
    TODO: Read file, handle FileNotFoundError, lowercase everything, 
    and strip punctuation using str.translate() and str.maketrans().
    Return a list of cleaned words.
    """
    pass

def analyze_frequencies(words: list) -> tuple[dict, list]:
    """
    TODO: 
    1. Filter out words < 3 characters using a generator expression.
    2. Build a frequency map manually using a dict and dict.get().
    3. Use a list comprehension to extract 'hapax legomena' (words appearing exactly once).
    Return a tuple: (frequency_dict, hapax_list)
    """
    pass

def generate_report(words_list, freq_dict, hapax_list, top_n):
    """
    TODO:
    1. Categorize text length using a Python 'match' statement.
    2. Sort the frequencies in descending order.
    3. Use a generator to lazily yield the top-N words.
    4. Print the text stats and scale the text bar chart.
    """
    total_words = len(words_list)
    
    # Hint for Categorization:
    # match total_words:
    #     case x if x < 500: ...
    
    pass

def main():
    parser = argparse.ArgumentParser(description="Word Frequency Analyser")
    parser.add_argument("file", help="Path to the text file to analyse")
    parser.add_argument("--top", type=int, default=20, help="Number of top words to display")
    
    # For Bonus Challenge
    # parser.add_argument("--bigrams", action="store_true", help="Include bigram analysis")
    
    args = parser.parse_args()
    
    # Execute structural pipeline
    # words = load_and_clean_text(args.file)
    # ...
    
if __name__ == "__main__":
    main()