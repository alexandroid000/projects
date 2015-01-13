#!/usr/bin/python
# search_generator.py

# use python + libraries to search web for cool backgrounds
# learns from user-generated training set
# this python program updates the frequencies of observed image tags and returns
# a new optimal search
# uses a bag-of-words approach with the metadata of the images

# imports
import sys
import operator
import random
# for fetching web data:
import urllib.request
import simplejson

class search_generator():
    def __init__(self, filename):
        self.filename = filename

        self.tags = {}
        self.total_count = 0

    def import_tags(self):
        # dictionary of tags and associated counts
        # will default to blank if no file / tags exists
        keys = []
        counts = []

        # read in file into dictionary
        try:
            tags_file = open(self.filename, 'r')

            for line in tags_file:
                # parse lines and add to dictionary, self.tags
                keys.append(line.split()[0])
                # need to cast counts to ints, and strip newlines
                temp_count = int(line.split()[1].rstrip())
                self.total_count += temp_count
                counts.append(temp_count)

            # create dictionary
            self.tags = {keys[i]:counts[i] for i in range(len(keys))}


            tags_file.close()
        except:
            print ("error in file", self.filename)


    # write generated dictionary to file
    def export_tags(self):
        # open file
        try:
            tags_file = open(self.filename, 'w')

            # iterate through dictionary and write in key:value\n format
            for key in self.tags:
                line = ""
                line = key + " " + str(self.tags[key]) + "\n"
                tags_file.write(line)

            tags_file.close()
        except:
            print ("error in file", self.filename)


    # adds or subtracts frequencies
    # liked is a bool input from the user
    # tags_to_change is a list of tags associated with the new image
    # made this section very frequentist and general so we could work with more
    # sophisticated probability distributions and string generation functions
    # later if we want
    def change_frequencies(self, liked, tags_to_change):
        for i in tags_to_change:

            # if user does like the image, keep it, and add one to each associated tag count
            if (liked == 1):
                if (i in self.tags):
                    self.tags[i] += 1
                else:
                    self.tags[i] = 1
                
                self.total_count +=1

            # if user doesn't like the image, this will subtract one count from the tags
            # associated with this image
            # only changes count if that tag already existed
            else:
                if (i in self.tags):
                    self.tags[i] -= 1
                    self.total_count -=1
                    # delete if count reaches zero
                    if (self.tags[i] == 0):
                        del self.tags[i]

    # choose Nth number of tags with the highest scores
    # to start, concatenate them in order of frequency into a search, but we can make more
    # advanced ways of choosing order later (Markov chain based on text descriptions
    # of images for ordering?)
    # return string that wrapper shell script uses to perform next search
    def next_search(self, N):

        search_string = ""

        # make sure we are not making the search have more words than we've seen
        # so far
        if len(self.tags) < N:
            N = len(self.tags)

        # convert dictionary into a "bag of words" with repeats explicitly
        # listed
        all_words = [word for word in self.tags.keys() for i in range(self.tags[word])]

        # take a random sample from our bag of words and concatenate
        random_grab = [all_words[i] for i in
                random.sample(range(len(all_words)), N)]
        for term in random_grab:
            search_string += term + "+"

        # trim last plus sign
        search_string = search_string[:-1]
        
        # return result
        return search_string


if __name__ == "__main__":
    # working directory for images and tags
    working_dir = "/home/alli/media/pics/backgrounds/image/"

    # initialize class
    find = search_generator(working_dir + "tags.txt")

    # import tags from file
    find.import_tags()

    if(len(sys.argv) != 3):
        print("Incorrect number of input arguments")
        print("Correct syntax is: search_generator.py liked_value image_name")
        sys.exit()

    # first command line arg is 0 or 1, for disliked pic or liked pic
    liked = int(sys.argv[1])

    # second command line is filename of background image
    # from this, extract keywords associated with image
    # get string, remove file extension
    image_name = sys.argv[2].lower()
    # split on underscores
    words = image_name.split("_")

    print("Extracted tags: ", words)

    # change dictionary of words based on preference and tags
    find.change_frequencies(liked,words)

    # save new tags to file
    find.export_tags()

    # handle web requests to find new image:
    fetcher = urllib.request.build_opener()
    # generate search string, will print to standard output
    searchTerm = find.next_search(5)
    print("Searching for: ", searchTerm)
    startIndex = 0

    # build URL, using google search API
    searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)

    # get results, put in parseable JSON format
    f = fetcher.open(searchUrl)
    results = simplejson.load(f)

    # parse results for the first image's URL and title data
    data = results['responseData']
    dataInfo = data['results']
    
    image_url = dataInfo[0]['unescapedUrl']
    print("Found image: ",image_url)
    # split title on whitespace
    title = dataInfo[0]['titleNoFormatting'].split()

    # create image name
    # save in backgrounds folder
    image_name = working_dir
    for word in title[:8]:
        image_name += word + "_"

    image_name = str(image_name[:-1])

    # download image
    try:
        with urllib.request.urlopen(image_url) as response, open(image_name, 'wb') as out_file:
            print("Saving as ", image_name)
            data = response.read() # a `bytes object
            out_file.write(data)
            out_file.close()
    except:
        print("Could not open image URL for download, try again")
