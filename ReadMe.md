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

