import unittest
from tweets import *

def map_lower(l):
    return list(map(lambda x: x.lower(), l))

class TestExtractMentions(unittest.TestCase):
    def test_extract_mentions_no_mention(self):
        tweet = 'jacky'
        actual = map_lower(extract_mentions(tweet))
        expect = []
        self.assertEqual(actual, expect)

    def test_extract_mentions_no_mention_2(self):
        tweet = '--@jacky'
        actual = map_lower(extract_mentions(tweet))
        expect = []
        self.assertEqual(actual, expect)

    def test_extract_mentions_empty_mention(self):
        tweet = '@'
        actual = map_lower(extract_mentions(tweet))
        expect = ['']
        self.assertEqual(actual, expect)

    def test_extract_mentions_empty_mention_2(self):
        tweet = '@@jacky'
        actual = map_lower(extract_mentions(tweet))
        expect = ['']
        self.assertEqual(actual, expect)

    def test_extract_mentions_one_mention_start_to_end(self):
        tweet = '@jacky'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky']
        self.assertEqual(actual, expect)

    def test_extract_mentions_one_mention_start_to_space(self):
        tweet = '@jacky 165cm'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky']
        self.assertEqual(actual, expect)

    def test_extract_mentions_one_mention_start_to_symbol(self):
        tweet = '@jacky, 165cm'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky']
        self.assertEqual(actual, expect)

    def test_extract_mentions_one_mention_in_middle(self):
        tweet = 'OMG it\'s @jacky LOL'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky']
        self.assertEqual(actual, expect)
    
    def test_extract_mentions_duplicate_mention(self):
        tweet = '@jacky @jacky little boy'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky', 'jacky']
        self.assertEqual(actual, expect)

    def test_extract_mentions_consecutive_test(self):
        tweet = '@jacky@jacky, little boy!'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky']
        self.assertEqual(actual, expect)

    def test_extract_mentions_mixed_test(self):
        tweet = '@jacky@jacky, @Henry @Teddy!'
        actual = map_lower(extract_mentions(tweet))
        expect = ['jacky', 'henry', 'teddy']
        self.assertEqual(actual, expect)


class TestExtractHashtags(unittest.TestCase):
    def test_extract_hashtags_no_hashtag(self):
        tweet = 'YOLO!!!!!'
        self.assertEqual(map_lower(extract_hashtags(tweet)), [])

    def test_extract_hashtags_no_hashtag_2(self):
        tweet = '--#MAGA'
        self.assertEqual(extract_hashtags(tweet), [])

    def test_extract_hashtags_empty_hashtag(self):
        tweet = '#'
        self.assertEqual(extract_hashtags(tweet), [''])

    def test_extract_hashtags_empty_hashtag_2(self):
        tweet = '##MakeGPA4.0Again'
        self.assertEqual(extract_hashtags(tweet), [''])

    def test_extract_hashtags_one_hashtag_start_to_end(self):
        tweet = '#jacky'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky'])

    def test_extract_hashtags_one_hashtag_start_to_space(self):
        tweet = '#jacky 165cm'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky'])

    def test_extract_hashtags_one_hashtag_start_to_symbol(self):
        tweet = '#jacky, 165cm'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky'])

    def test_extract_hashtags_one_hashtag_in_middle(self):
        tweet = 'OMG it\'s #jacky LOL'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky'])
    
    def test_extract_hashtags_duplicate_hashtag(self):
        tweet = '#jacky #jacky little boy'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky'])

    def test_extract_mentions_consecutive_test(self):
        tweet = '#jacky#jacky, little boy!'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky'])

    def test_extract_mentions_mixed_test(self):
        tweet = '#jacky#jacky, #Henry #Teddy!'
        self.assertEqual(map_lower(extract_hashtags(tweet)), ['jacky', 'henry', 'teddy'])


class TestCountWords(unittest.TestCase):
    def test_count_words_empty_dictionary_empty_tweet(self):
        tweet = ''
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {})

    def test_count_words_empty_dictionary_one_word(self):
        tweet = 'yummy yummy'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {'yummy': 2})

    def test_count_words_one_word_with_case(self):
        tweet = 'yummy Yummy'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {'yummy': 2})

    def test_count_words_multiple_words(self):
        tweet = 'yummy boy'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {'yummy': 1, 'boy': 1})

    def test_count_words_punctuation_sanitize(self):
        tweet = 'yummy --@yummy!'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {'yummy': 2})

    def test_count_words_updating_persistence(self):
        tweet = ''
        counts = {'yummy':1}
        count_words(tweet, counts)
        self.assertEqual(counts, {'yummy': 1})

    def test_count_words_updating_dictionary(self):
        tweet = 'yummy'
        counts = {'yummy':1}
        count_words(tweet, counts)
        self.assertEqual(counts, {'yummy': 2})

    def test_count_words_omit_hashtag(self):
        tweet = '#funky jacky'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {'jacky': 1})

    def test_count_words_omit_mention(self):
        tweet = 'funky @jacky'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {'funky': 1})

    def test_count_words_omit_url(self): # No URL (end)
        tweet = 'http://google.com'
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {})

    def test_count_words_omit_empty_string(self): # Empty string
        tweet = '  \n\n '
        counts = {}
        count_words(tweet, counts)
        self.assertEqual(counts, {})


class TestCommonWords(unittest.TestCase):
    def test_common_words_empty(self):
        counts = {}
        common_words(counts, 1)
        self.assertEqual(counts, {})

    def test_common_words_under_threshold(self):
        counts = {'gay': 5, 'jacky': 1}
        common_words(counts, 1)
        self.assertEqual(counts, {'gay': 5})

    def test_common_words_tie_at_threshold(self):
        counts = {'mocha': 10, 'gay': 5, 'jacky': 5}
        common_words(counts, 1)
        self.assertEqual(counts, {'mocha': 10})
    
    def test_common_words_tie_under_threshold(self):
        counts = {'mocha': 10, 'gay': 5, 'jacky': 5}
        common_words(counts, 3)
        self.assertEqual(counts, {'mocha': 10, 'gay': 5, 'jacky': 5})

class TestReadTweets(unittest.TestCase):
    results = [eval(c) for c in open('read_tweets_results.txt')]

    def test_read_tweets_empty(self):
        f = open('read_tweets_empty.txt')
        actual = read_tweets(f)
        f.close()
        expect = {} 
        self.assertEqual(actual, expect)

    def test_read_tweets_one_person_one_tweet(self):
        f = open('read_tweets_1_1.txt')
        actual = read_tweets(f)
        f.close()
        expect = self.results[0]     
        self.assertEqual(actual, expect)

    def test_read_tweets_one_person_three_tweet(self):
        f = open('read_tweets_1_3.txt')
        actual = read_tweets(f)
        f.close()
        expect = self.results[1]     
        self.assertEqual(actual, expect)

    def test_read_tweets_two_person_two_tweet(self):
        f = open('read_tweets_2_2.txt')
        actual = read_tweets(f)
        f.close()
        expect = self.results[2]     
        self.assertEqual(actual, expect)  
TWEETS = {'Jacky': [('Jacky', '#LOL', 1, '', 10, 10),
                    ('Jacky', 'Lalala #YOUXIU', 2, '', 10, 10),
                    ('Jacky', 'Wo #hao gao!', 3, '', 10, 10),
                    ('Jacky', 'Wo #hao shuai', 4, '', 100, 500),
                    ('Jacky', 'Wo #hao meng', 5, '', 200, 400)],
          'Teddy': [('Teddy', 'Yoyo', 1, '', 10, 10),
                    ('Teddy', 'Me Me Da', 2, '', 20, 20),
                    ('Teddy', 'Cuba! #LOL #LOL', 3, '', 20, 20),
                    ('Teddy', '#LifeScience', 4, '', 40, 60),
                    ('Teddy', '#MAGA #hao', 20, '', 40, 8)],
          'James': [('James', '#YOLO', 1, '', 10, 10),
                    ('James', 'Me Me Da', 2, '', 0, 0),
                    ('James', 'Cuba!', 3, '', 40, 40),
                    ('James', '#UofT', 4, '', 40, 60),
                    ('James', '#MAGA', 10, '', 40, 40)]}

class TestMostPopular(unittest.TestCase):
    def test_most_popular_test_inclusive(self):
        actual = most_popular(TWEETS, 2, 2)
        expect = 'Teddy'
        self.assertEqual(expect, actual)

    def test_most_popular_test_empty_tie(self):
        actual = most_popular(TWEETS, 99, 100)
        expect = 'Tie'
        self.assertEqual(expect, actual)

    def test_most_popular_test_two_people_tie(self):
        actual = most_popular(TWEETS, 1, 3)
        expect = 'Tie'
        self.assertEqual(expect, actual)

    def test_most_popular_test_more_people_tie(self):
        actual = most_popular(TWEETS, 1, 1)
        expect = 'Tie'
        self.assertEqual(expect, actual)

    def test_most_popular_test_some_people_no_tweets(self):
        actual = most_popular(TWEETS, 15, 21)
        expect = 'Teddy'
        self.assertEqual(expect, actual)

    def test_most_popular_test_general_test(self):
        actual = most_popular(TWEETS, 0, 110)
        expect = 'Jacky'
        self.assertEqual(expect, actual)


class TestDetectAuthor(unittest.TestCase):

    def test_detect_author_empty_input(self):
        actual = detect_author(TWEETS, '')
        expect = 'Unknown'
        self.assertEqual(actual, expect)
    
    def test_detect_author_no_hashtag(self):
        actual = detect_author(TWEETS, 'LifeScience')
        expect = 'Unknown'
        self.assertEqual(actual, expect)

    def test_detect_author_hashtag_not_contains(self):
        actual = detect_author(TWEETS, '#EASY4')
        expect = 'Unknown'
        self.assertEqual(actual, expect)
    
    def test_detect_author_hashtag_not_unique(self):
        actual = detect_author(TWEETS, '#MAGA')
        expect = 'Unknown'
        self.assertEqual(actual, expect)

    def test_detect_author_hashtag_not_unique_2(self): 
        actual = detect_author(TWEETS, '#LOL')
        expect = 'Unknown'
        self.assertEqual(actual, expect)

    def test_detect_author_one_hashtags_to_unqiue_person(self):
        actual = detect_author(TWEETS, '#YOUXIU')
        expect = 'Jacky'
        self.assertEqual(actual, expect)

    def test_detect_author_contains_hashtags_to_unqiue_person(self):
        actual = detect_author(TWEETS, '#LOL #hao #YOUXIU')
        expect = 'Jacky'
        self.assertEqual(actual, expect)

    def test_detect_author_contains_hashtags_to_different_person_same_count(self):
        actual = detect_author(TWEETS, '#UofT #YOUXIU')
        expect = 'Unknown'
        self.assertEqual(actual, expect)

    def test_detect_author_contains_hashtags_to_different_person_different_count(self):
        actual = detect_author(TWEETS, '#UofT #UofT #YOUXIU')
        expect = 'Unknown'
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    cont = True
    suites = {'1': TestExtractMentions,
              '2': TestExtractHashtags,
              '3': TestCountWords,
              '4': TestCommonWords,
              '5': TestReadTweets,
              '6': TestMostPopular,
              '7': TestDetectAuthor,
              '8': 'TestAll'}
    print('-'*70)
    print('Easy4.0 CSC108 2016 FALL tweets.py Unittest Module.')
    print('-'*70)
    print('''This is a complimentary unittest module for clients that helps you check the correctness
of your tweets.py file. This contains various unittest cases that would test all
your functions in tweets.py.
Please make sure you named the file correctly and place both test file and the tweets.py
in the same folder
''')
    while cont:
        print('''\n\nYou have following options : 
1. test extract_mentions
2. test extract_hashtags
3. test count_words
4. test common_words
5. test read_tweets
6. test most_popular
7. test detect_author
8. test ALL!''')
        number = input('\n Please indicate the number before the option:  ')
        while number not in suites:
            print('\n Invalid input.')
            number = input('\n Please indicate the number before the option:  ')
        if number == '8':
            unittest.main(verbosity=2, exit=False)
        else:
            suite = unittest.TestLoader().loadTestsFromTestCase(suites[number])
            unittest.TextTestRunner(verbosity=2).run(suite)
        
        cont = input('\n Do you want to continue? (Y to continue, others to exit.):  ').lower() == 'y'
    
    print('''\n\nSteps after your code passes:
1. Review your code, use meaningful variable names, simplify your alogrithm.
2. Leave some comments in your coding.
3. Check pep8 at pep8online.com.

Happy coding and best wishes to your assignments!''')
    try:
        input("\nPress enter to continue")
    except SyntaxError:
        pass
