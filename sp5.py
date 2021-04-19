from threading import Thread

def bigrams(word):
    from collections import Counter
    print(f"Thread {word}: multiplying")
    res=Counter(word[idx : idx + 2] for idx in range(len(word)-1))
    print(f"{word}: get ans = {res}")
    return res

def division_text(test_str):
     threads = []
     words = test_str.split()
     for word in words:
         thread = Thread(target=bigrams, args=(word, ))
         threads.append(thread)
         print(f"{thread.getName()}: starting")
         thread.start()   
     for thread in threads:
         print(f"{thread.getName()}: joining")
         thread.join()
         print(f"{thread.getName()}: done")
          
if __name__ == '__main__':
      test_str = input("Enter the string: ")
      res = division_text(test_str)  

