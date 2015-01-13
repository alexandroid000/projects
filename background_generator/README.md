# Background Generator

This is a program I have written that uses the Google Search API to search for
pictures and downloads them as well as the "title" information about them. It
then uses this title information to generate a "bag of words" ([see
here](http://en.wikipedia.org/wiki/Bag-of-words_model)) model for learning which
types of backgrounds the user likes.

User feedback comes in the form of a command-line argument to the program that
simply specifies whether they liked or disliked the background. This preference
information is used to update the bag-of-words / dictionary that the program
uses to make future searches.

# Dependencies

* This program is written in Python 3 with a Bash/Zsh wrapper
* Uses [feh](http://feh.finalrewind.org/) to update background image
* Has only been tested on arch/i3
* Uses Google API through AJAX (no extra download necessary) 

# Usage

* Download search_generator.py and set_background, make executable and in a
  searchable path
* Set the WORKING_DIR variable in both files to your desired directory for
  saving backgrounds and the tag dictionary
* Download a starting background, with a filename of the format
  tags_to_start_with (example: space_dark_1920x1080). This will be the initial
  set of training data.
* If desired, more training data can be specified in a file in
  WORKING_DIRECTORY. This data takes the format of $TAG $COUNT with each tag on
  its own line. See the example tags.txt in this repository.
* Don't store any files other than the current background and tags.txt in
  WORKING_DIRECTORY
* Run the command "set_background $PREFERENCE_VALUE" in your shell.
  $PREFERENCE_VALUE is 0 if the current background isn't good. $PREFERENCE_VALUE
  is one if the current background is good.
