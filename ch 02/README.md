# Project 02: Word Frequency Analyser

### Overview
This project focuses on advanced data manipulation, file handling, and the power of Python's functional tools (comprehensions and generators). You will build a tool that can take any text file—from a short poem to a massive novel—and extract meaningful statistical patterns.

### Technical Signposts & Friction Points

1. **Efficient Punctuation Stripping**
   Instead of looping through every character manually or using complex Regex, use the highly optimized C-backed string methods. This is the "Masterclass" way to handle character mapping:
   ```python
   import string
   clean_text = text.translate(str.maketrans('', '', string.punctuation))
   

```

2. **The `dict.get()` Counting Idiom**
Since `collections.Counter` is restricted for this project, you must manage the dictionary keys yourself. Initialize missing keys cleanly by providing a default value of `0` to the `.get()` method:
```python
counts[word] = counts.get(word, 0) + 1


```



```

3. **Sorting Dictionaries by Value**
   To sort a dictionary by its frequency (value) rather than the word (key), use the built-in `sorted()` function with a lambda as the sorting key:
   ```python
   sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)
   

```

4. **Bar Chart Scaling Math**
To ensure your text bars don't overflow the terminal screen, scale them relative to the most frequent word. If your maximum bar width is 20 characters, use this logic:
* Find the frequency of the #1 word (the `max_freq`).
* For every other word, the number of characters in the bar is:
`int((current_freq / max_freq) * 20)`


5. **Structural Pattern Matching**
Use the `match` statement (introduced in Python 3.10) to categorize the text length. This replaces long `if/elif` chains and is much more readable for range-based logic:
```python
match total_words:
    case x if x < 500:
        category = "Short"
    case x if 500 <= x <= 2000:
        category = "Medium"
    case _:
        category = "Long"


```



```

### Bonus Challenge: Bigram Analysis
To count word pairs (bigrams), you need to look at "word N" and "word N+1" simultaneously. A Pythonic way to do this without using index integers is to use `zip` on two versions of the same list, with one version shifted by one index:
```python
bigrams = zip(words, words[1:])

```

### Constraints Checklist

* [ ] No `collections.Counter` (Do it manually!)
* [ ] No third-party libraries (Standard Library only).
* [ ] Must handle `FileNotFoundError` gracefully.
* [ ] Must use at least one Generator Expression.
* [ ] Must use at least one List Comprehension.

```

---

### Pro-Tip for your Students
If they are testing with a very large file (like a text dump of *Pride and Prejudice*), remind them that using a **generator** for the top-N display is much more memory-efficient than slicing a massive sorted list!

```