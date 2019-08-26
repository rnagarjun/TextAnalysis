# Project Info

This is a simple high level class to help analysis english text data.
Given a piece of english text, the user can:

		* Tokenize the content by Sentence
		* Get word count, character count and sentence count	
		* Get POS tagging and count
		* Clean the text by removing digits, punctuations and any other regex form
		* Remove stopwords - (words that don't provide much meaning...in, at, the etc)
		* Calculate automatic readability index value
		* sentiment analysis - (findout if a statement is a good news or a bad news)
			* scored using values between [-1, 1] - the more negative, the worse the news.
		* Create a word cloud
	
### Author
Nagarjun Ratnesh

## Installation

1. Make sure python3 is download
2. Creating a Virtual Environment by the following command.

		$virtualenv -p locationOfPython3 nameOfVirtualEnv
		
		Example
		$virtualenv -p /usr/bin/python3 myVirtualEnv

	

3. Activating the virtual environment

		$. myVirtualEnv/bin/activate

or

		$source myVirtualEnv/bin/activate

4. Installing all dependencies found in the requirements.txt

		$pip install -r requirements.txt

## Usage
To use the library code
1. To import the class and it's methods, simply

		import textAnalysis.py

2. Create an object and make use of the functions as you wish

		new_content = Content("desired text")
		
The function can also be used individual text, not just the initial text the user input when creating the object. 
In other words, if the user needs a simple text POS Tagged, Sentiment Analysed, stemmed etc. Those tasks can be completed individually.
The user has the option to simply just include the text in the function as a parameter.
*If the parameter is not None, 
	the function will output the computation done on the input text
*if the function parameter is left empty
	the function will do the computation on the content value itself. (aka self.content)
	
	
	
	
	
	
	

		
if __name__ == "__main__":
#	text2Analyze = "Seoul, South Korea (CNN)South Korea is scrapping its military intelligence-sharing agreement with Japan, the latest escalation in a trade dispute that threatens global supply chains for smartphones and other gadgets. Kim You-geun, first deputy director of the Blue House National Security Office, said the move was in retaliation to Japans decision to exclude South Korea from its list of trusted trading partners.Under these circumstances, the government judged that it would not be in our national interest to keep the agreement in place, which was signed for the purpose of exchanging sensitive military information for security (purposes), Kim said.The rising tensions between the two countries have sparked worries around the world. We encourage Japan and Korea to work together to resolve their differences. I hope they can do this quickly, said Lt. Col. Dave Eastburn, a Pentagon spokesman. We are all stronger -- and northeast Asia is safer -- when the United States, Japan, and Korea work together in solidarity and friendship, he said, adding that intelligence sharing was key to developing common defense policy and strategy.The standoff between Tokyo and Seoul started last month when Japan placed new restrictions on the export of three chemical materials to South Korea. Those chemicals are used in computer chips manufacturing -- a key part of the South Korean economy. The new rules delay exports as Japanese companies must apply for licenses for each of the materials, a process that can take up to 90 days. But tension between the two countries has been rising for months, stemming in part from Japans colonial rule over the Korean peninsula in the early 20th century. South Koreas top court recently ruled that its citizens can sue Japanese companies for using forced Korean labor during World War II. Japan has denied that the two issues are linked."

	text2Analyze = "I just broke my leg! Flowers are beautiful! Today was my 2nd day at work. Once upon a time there was a cat, but the cat had no fur. The dog climbed up the bench today. I bought a new bag today. She was sick but atleast she got a day off from work. Finally, the quick brown fox jumped over the lazy dog."
	paragraph = Content(text2Analyze)
#	paragraph.pre_process()


	print('tokenized')
	print(paragraph.tokenize())
	
	print('sentiment_analysis')
	print(paragraph.sentiment_analysis())
	
	print('clean_content')
	print(paragraph.clean_content())
	
	print('remove_stopwords')
	print(paragraph.remove_stopwords())

	print('POS tag')
	print(paragraph.POS_tagging())

	print('Stem')
	print(paragraph.stem())


	#paragraph.pre_process()
	#paragraph.plot_word_cloud()
