import bs4
from gtts import gTTS

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    # Parse the HTML using BeautifulSoup
    soup = bs4.BeautifulSoup(text, 'html.parser')

    # Extract the title and teaser for each story
    stories = []
    for story_elem in soup.find_all('div', class_='story-text'):
        title_elem = story_elem.find('h3', class_='title')
        teaser_elem = story_elem.find('p', class_='teaser')

        title = title_elem.text.strip() if title_elem else ""
        teaser = teaser_elem.text.strip() if teaser_elem else ""

        stories.append((title, teaser))

    return stories

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    # Check if the requested index is within the range of the stories list
    if 0 <= n < len(stories):
        title, teaser = stories[n]

        # Combine title and teaser if teaser is present
        text_to_speak = f"{title}. {teaser}" if teaser else title

        # Use gTTS to synthesize the audio
        tts = gTTS(text_to_speak, lang='en')
        tts.save(filename)

        print(f"Story {n+1} saved to {filename}")
    else:
        print(f"Invalid story index: {n}")

