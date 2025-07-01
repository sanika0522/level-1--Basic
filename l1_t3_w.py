def count_words_in_file(file_path):
         try:
             with open(file_path, 'r') as file:
                 content = file.read()
                 words = content.split()
                 return len(words)
         except FileNotFoundError:
             return "File not found."
file_path = 'sample.txt'  # Replace with your file path
print(f"Number of words in the file: {count_words_in_file(file_path)}")
     