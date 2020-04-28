import re

COURSE = (
    "Introduction 1 Lecture 01:47"
    "The Basics 4 Lectures 32:03"
    "Getting Technical!  4 Lectures 41:51"
    "Challenge 2 Lectures 27:48"
    "Afterword 1 Lecture 05:02"
)
TWEET = (
    "New PyBites article: Module of the Week - Requests-cache "
    "for Repeated API Calls - http://pybit.es/requests-cache.html "
    "#python #APIs"
)
HTML = "<p>pybites != greedy</p>" "<p>not the same can be said REgarding ...</p>"


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    m = re.findall(r"\d\d:\d\d", course)
    return m


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    hashes = re.findall(r"#[A-Za-z]+", tweet)
    links = re.findall(r".*\.[A-Za-z]+", tweet)
 #   for hash in hashes:
 #       strip_hash = hash.strip(' ')
 #       links.append(strip_hash)
    links += hashes
    print(links)
    return links



def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    paragraph = re.findall(r"<p>[A-Za-z!=. ]+</p>", html)
    #print(paragraph)
    final_return = paragraph[0][3:-4]
    return(final_return)
    #print(final_return)


if __name__ == "__main__":
    # extract_course_times(course=COURSE)
    get_all_hashtags_and_links(tweet=TWEET)
    #match_first_paragraph()
