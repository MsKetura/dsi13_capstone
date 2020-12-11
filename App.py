import streamlit as st
import pickle

st.set_page_config(
    page_icon='',
    initial_sidebar_state='expanded')

st.title('Beyonce or Rihanna Lyrics Classifier')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'EDA', 'Make a prediction'))

@st.cache
def load_data():
     ladies = pd.read_csv('lyrics_and_artist.csv',encoding='latin-1')
     return ladies



if page == 'About':
    st.subheader('About this project')
    st.markdown('''This is a Streamlit app that hosts my Beyonce vs. Rihanna SVM model, with count vectorized text.
    For each of these artists, I gathered the lyrics for their top 75 most popular songs (not including remixes & features), according to the Genius song lyric site.



| Top 75 most popular songs for beyonce         | Top 75 most popular songs for Rihanna         |
|-----------------------------------------------|-----------------------------------------------|
| Song 1: "Drunk in Love"                       | Song 1: "Work"                                |
| Song 2: "Formation"                           | Song 2: "Love on the Brain"                   |
| Song 3: "Partition"                           | Song 3: "Needed Me"                           |
| Song 4: "Mine"                                | Song 4: "Stay"                                |
| Song 5: "Hold Up"                             | Song 5: "Kiss It Better"                      |
| Song 6: "Sorry"                               | Song 6: "Sex with Me"                         |
| Song 7: "If I Were a Boy"                     | Song 7: "Bitch Better Have My Money"          |
| Song 8: "Pray You Catch Me"                   | Song 8: "Consideration"                       |
| Song 9: "All Night"                           | Song 9: "Diamonds"                            |
| Song 10: "\*\*\*Flawless"                     | Song 10: "Desperado"                          |
| Song 11: "Halo"                               | Song 11: "Same Ol’ Mistakes"                  |
| Song 12: "Freedom"                            | Song 12: "What’s My Name?"                    |
| Song 13: "Don’t Hurt Yourself"                | Song 13: "Umbrella"                           |
| Song 14: "Rocket"                             | Song 14: "Loveeeeeee Song"                    |
| Song 15: "Blow"                               | Song 15: "Love the Way You Lie, Pt\. II"      |
| Song 16: "Sandcastles"                        | Song 16: "Higher"                             |
| Song 17: "7/11"                               | Song 17: "Yeah, I Said It"                    |
| Song 18: "6 Inch"                             | Song 18: "Close to You"                       |
| Song 19: "Love Drought"                       | Song 19: "Woo"                                |
| Song 20: "Pretty Hurts"                       | Song 20: "Man Down"                           |
| Song 21: "Listen"                             | Song 21: "Pour It Up"                         |
| Song 22: "XO"                                 | Song 22: "S&M"                                |
| Song 23: "Haunted"                            | Song 23: "Never Ending"                       |
| Song 24: "Jealous"                            | Song 24: "What Now"                           |
| Song 25: "Daddy Lessons"                      | Song 25: "We Found Love"                      |
| Song 26: "Heaven"                             | Song 26: "James Joint"                        |
| Song 27: "Countdown"                          | Song 27: "Pose"                               |
| Song 28: "Bow Down"                           | Song 28: "Take a Bow"                         |
| Song 29: "Irreplaceable"                      | Song 29: "Don’t Stop the Music"               |
| Song 30: "BLACK PARADE"                       | Song 30: "Unfaithful"                         |
| Song 31: "Crazy in Love"                      | Song 31: "Rude Boy"                           |
| Song 32: "Forward"                            | Song 32: "Love Without Tragedy / Mother Mary" |
| Song 33: "Blue"                               | Song 33: "Numb"                               |
| Song 34: "MOOD 4 EVA"                         | Song 34: "Rehab"                              |
| Song 35: "Lemonade Film \(Script\)"           | Song 35: "Only Girl \(In the World\)"         |
| Song 36: "Upgrade U"                          | Song 36: "Jump"                               |
| Song 37: "Superpower"                         | Song 37: "Disturbia"                          |
| Song 38: "No Angel"                           | Song 38: "Skin"                               |
| Song 39: "Love on Top"                        | Song 39: "Sledgehammer"                       |
| Song 40: "Resentment"                         | Song 40: "Talk That Talk"                     |
| Song 41: "Best Thing I Never Had"             | Song 41: "Russian Roulette"                   |
| Song 42: "SPIRIT"                             | Song 42: "Goodnight Gotham"                   |
| Song 43: "Single Ladies \(Put a Ring on It\)" | Song 43: "Birthday Cake"                      |
| Song 44: "Party"                              | Song 44: "Te Amo"                             |
| Song 45: "Back to Black"                      | Song 45: "Cockiness \(Love It\)"              |
| Song 46: "Die With You"                       | Song 46: "California King Bed"                |
| Song 47: "Run the World \(Girls\)"            | Song 47: "Get It Over With"                   |
| Song 48: "Dance for You"                      | Song 48: "Nobody’s Business"                  |
| Song 49: "Me, Myself and I"                   | Song 49: "American Oxygen"                    |
| Song 50: "Grown Woman"                        | Song 50: "You Da One"                         |
| Song 51: "Ave Maria"                          | Song 51: "No Love Allowed"                    |
| Song 52: "I Miss You"                         | Song 52: "Pon de Replay"                      |
| Song 53: "Dangerously In Love 2"              | Song 53: "Phresh Out the Runway"              |
| Song 54: "Ego"                                | Song 54: "Hard"                               |
| Song 55: "Before I Let Go"                    | Song 55: "Cheers \(Drink to That\)"           |
| Song 56: "Yoncé"                              | Song 56: "Hate That I Love You"               |
| Song 57: "1\+1"                               | Song 57: "Where Have You Been"                |
| Song 58: "I Was Here"                         | Song 58: "Watch n’ Learn"                     |
| Song 59: "Broken\-Hearted Girl"               | Song 59: "Shut Up and Drive"                  |
| Song 60: "Sweet Dreams"                       | Song 60: "Towards the Sun"                    |
| Song 61: "Diva"                               | Song 61: "SOS"                                |
| Song 62: "BIGGER"                             | Song 62: "Right Now"                          |
| Song 63: "MY POWER"                           | Song 63: "Stupid In Love"                     |
| Song 64: "Baby Boy"                           | Song 64: "Half of Me"                         |
| Song 65: "Hello"                              | Song 65: "Raining Men"                        |
| Song 66: "Ring the Alarm"                     | Song 66: "Do Ya Thang"                        |
| Song 67: "Déjà Vu"                            | Song 67: "Lost in Paradise"                   |
| Song 68: "I’d Rather Go Blind"                | Song 68: "Cry"                                |
| Song 69: "Denial \(Poem\)"                    | Song 69: "Red Lipstick"                       |
| Song 70: "Kitty Kat"                          | Song 70: "Good Girl Gone Bad"                 |
| Song 71: "OTHERSIDE"                          | Song 71: "Complicated"                        |
| Song 72: "I Care"                             | Song 72: "Drunk on Love"                      |
| Song 73: "Roc"                                | Song 73: "Answer"                             |
| Song 74: "Signs"                              | Song 74: "Dancing in the Dark"                |
| Song 75: "FIND YOUR WAY BACK"                 | Song 75: "ROCKSTAR 101"                       |

"

    ''')
elif page == 'EDA':
    st.subheader('Exploratory Data Analysis')
    st.write('''This model is trained on the top 75 most popular lyrics from both artists.''')
    st.write('''This bar chart is of the top 10 most common stopwords.''')
    st.write('''This model does not include the stopwords.''')

elif page == 'Make a prediction':
    st.subheader('Want to see if this model can predict which artist the lyrics you insert belong to?')
    st.write('''Enter some lyrics to make a prediction!''')
    with open('svc.pkl', 'rb') as pickle_in:
        svc = pickle.load(pickle_in)
    your_text = st.text_input(
        label='Please enter some text:',
        value='enter some text',
        max_chars=500)
    artist = svc.predict([your_text])[0]
    if artist == 0:
        artist = 'Beyonce'
    else:
        artist = 'Rihanna'
    st.subheader('Results:')
    st.write(f'This text is more like {artist.title()}.')
