import re
import csv
#%matplotlib inline
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

#import beautifulsoup4
#import urllib3





def rejoin_text(list_of_text):
	"""
	Util function to put together text that's been fragmeted into lists	
	"""

	try:
		return " ".join(word for word in list_of_text)
	except TypeError:
		pass

	
class Content:
	"""
	A class to represent the contents on a news article
	"""
	
	def __init__(self, content, url=None):
		"""
		Connects the Comment class to the pands object
		"""
		self.content = content
		self.source = url
		self.pre_processed = None
		self.pre_process_status = {'tokenized': None, 'cleaned_content': None, 'POS_tagged': None, 'stemmed': None, 'stopwords_removed': None, 'sentiment_analyzed': None}
		self.counts = {'sentences': 0, 'words': 0, 'characters': 0}
		
		
	def pre_process(self, tokenize=True, POS_tagging = True, remove_stopwords = True, sentiment_analysis = True, stem=True, custom_regex=None) -> None:
		"""
			The order in which pre processing should occur is as follows,
				clean_content -> tokenize -> sentiment_analysis -> remove_stopwords -> POS_tagging -> stem
		"""
		#self.clean_content()
		rf_analysis = self.tokenize()
		print(rf_analysis)
		scnt_analyzed = self.sentiment_analysis(rf_analysis)
		self.clean_content()
		
		#self.remove_stopwords()

		#self.POS_tagging()
		#self.stem()
		#print(self.pre_processed)

	
	def tokenize(self) -> list():
		"""
		Given a text, this function will split the text into appropriate sentences.
		"""
		tokenized_content = nltk.sent_tokenize(self.content)
		self.counts['sentences'] = len(tokenized_content)
		self.pre_processed = rejoin_text(tokenized_content)
		self.pre_process_status['tokenized'] = True
		return tokenized_content


	def POS_tagging(self) -> None:
		"""
		Given a text of words, this function will assign part of speech tagging for each individual word
		"""
		pos_tagged = nltk.pos_tag(self.pre_processed.split())
		self.pre_processed = pos_tagged
		self.pre_process_status['POS_tagged'] = True
		#cfg_list = Counter(tag for word,tag in cleaned_text)
		return pos_tagged
		
	def stem(self) -> None:
		"""
		helps to classify words such as jump, jumpping, jumped etc into 
		one word jump.
		"""
		ss = nltk.stem.SnowballStemmer('english')
		stemmed = [(ss.stem(w[0]), w[1]) for w in self.pre_processed]
		self.pre_processed = stemmed
		self.pre_process_status['stemmed'] = True
		return stemmed
		

	def remove_stopwords(self) -> None:
		"""
		Removes unneccesary words such as in, the, at etc. The words that 
		are not very useful when trying to create a word cloud.
		"""
		stop_words = set(nltk.corpus.stopwords.words("english"))
		all_words = self.pre_processed.split()
		stopwords_removed = [w for w in all_words if not str(w).lower() in stop_words]
		self.counts['words'] = len(stopwords_removed)

		self.pre_processed = rejoin_text(stopwords_removed) 
		self.pre_process_status['stopwords_removed'] = True

		return stopwords_removed
		
	def calculate_ari(self) -> None:
		"""
		Calculate the artifical readability index for a given text
		This value approximates the level of reading difficulty of the text
		"""
		ARI = 4.71*(character_count/word_count) + 0.5*(word_count/sentence_count)-21.43
		return ARI

		
	def sentiment_analysis(self, sentences) -> list():	
		"""
		For a given group of sentences, it will indicate the polarity of the sentence.
		This method makes use of the SentimentIntensityAnalyzer from the NLTK library
		
		EXAMPLE:
		>>> The dog climbed up the bench today.
		>>> compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0
		
		>>> I just broke my leg.
		>>> compound: -0.4215, neg: 0.483, neu: 0.517, pos: 0.0
		
		>>> Flowers are beautiful.
		>>> compound: 0.5994, neg: 0.0, neu: 0.339, pos: 0.661
		
		>>> She was sick but atleast she got a day off from work.
		>>> compound: -0.2846, neg: 0.177, neu: 0.823, pos: 0.0
		"""
		polarity_calculated = dict()
		sid = SentimentIntensityAnalyzer()
		for sentence in sentences:
			polarity[sentence] = list()
			ss = sid.polarity_scores(sentence)
			for k in sorted(ss):
				polarity[sentence].append('{0}: {1}, '.format(k, ss[k]), end='')
				print('{0}: {1}, '.format(k, ss[k]), end='')
			print()

		
	def count_syllable(word) -> None:
		"""
		count the number of syllable in a given word
		
		EXAMPLE
		>>> word
		>>> sylabble
		"""
		word = word.lower()
		count = 0
		vowels = "aeiouy"
		if word[0] in vowels:
			count += 1
		for index in range(1, len(word)):
			if word[index] in vowels and word[index - 1] not in vowels:
				count += 1
		if word.endswith("e"):
			count -= 1
		if count == 0:
			count += 1
		return count

		
	def clean_content(self, punctuations=True, digits=True, custom_regex=None) -> None:
		"""
		Clean the text based on the given conditions, if puntuation
		and digits are specificed as false, then the clean will not eliminate those
		contents from the text.
		"""
		#letter = re.sub("\d+", " ", sentence)
		#letters_only = re.sub("[^\w\s]", " ", letter)
		content = self.pre_processed
		if punctuations:
			content = content.replace(r"[^\w\s]", "")
		
		if digits:
			content = content.replace(r"\d+", "")
		
		if custom_regex:
			content = content.replace(custom_regex, "")
			
		content = content.strip()
		tokenized_words = nltk.word_tokenize(content.lower())
		self.pre_processed = rejoin_text(tokenized_words)
		self.pre_process_status['cleaned_content'] = True

	def plot_word_cloud(self, title, width=600, height=400):
		"""
		Creates word cloud using the text from pre_processed
		
		"""
		wordcloud = WordCloud(width=width, height=height, background_color="white").generate(self.pre_processed)        
		fig, ax = plt.subplots()        
		ax.imshow(wordcloud, interpolation="bilinear")        
		plt.axis("off")        
		plt.tight_layout()        
		plt.title(title)        
		plt.savefig(title+ "_wordCloud.png")

		
		
if __name__ == "__main__":
#	text2Analyze = "Seoul, South Korea (CNN)South Korea is scrapping its military intelligence-sharing agreement with Japan, the latest escalation in a trade dispute that threatens global supply chains for smartphones and other gadgets. Kim You-geun, first deputy director of the Blue House National Security Office, said the move was in retaliation to Japans decision to exclude South Korea from its list of trusted trading partners.Under these circumstances, the government judged that it would not be in our national interest to keep the agreement in place, which was signed for the purpose of exchanging sensitive military information for security (purposes), Kim said.The rising tensions between the two countries have sparked worries around the world. We encourage Japan and Korea to work together to resolve their differences. I hope they can do this quickly, said Lt. Col. Dave Eastburn, a Pentagon spokesman. We are all stronger -- and northeast Asia is safer -- when the United States, Japan, and Korea work together in solidarity and friendship, he said, adding that intelligence sharing was key to developing common defense policy and strategy.The standoff between Tokyo and Seoul started last month when Japan placed new restrictions on the export of three chemical materials to South Korea. Those chemicals are used in computer chips manufacturing -- a key part of the South Korean economy. The new rules delay exports as Japanese companies must apply for licenses for each of the materials, a process that can take up to 90 days. But tension between the two countries has been rising for months, stemming in part from Japans colonial rule over the Korean peninsula in the early 20th century. South Koreas top court recently ruled that its citizens can sue Japanese companies for using forced Korean labor during World War II. Japan has denied that the two issues are linked."

	text2Analyze = "I just broke my leg. Flowers are beautiful. Today was my second day at work. Once upon a time there was a cat, but the cat had no fur. The dog climbed up the bench today. I bought a new bag today. She was sick but atleast she got a day off from work."
	paragraph = Content(text2Analyze)
	paragraph.pre_process()
	paragraph.plot_word_cloud()
	
