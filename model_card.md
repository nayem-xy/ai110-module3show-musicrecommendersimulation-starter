# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0 – Music Recommender Simulation**

VibeFinder is a content-based music recommendation system that suggests songs based on a user's musical preferences.

---

## 2. Intended Use

VibeFinder is designed to recommend songs from a small music catalog by comparing song characteristics with a predefined user profile.

It generates a ranked list of the three songs that best match the user's preferences.

The initial simulation assumes that the user has a favorite genre, a favorite mood, and target values for several audio characteristics.

This project is intended for classroom learning and experimentation with recommendation algorithms. It is not designed to replace commercial music streaming recommendation systems.

---

## 3. How the Model Works

VibeFinder uses **content-based filtering**. Instead of comparing listening histories between different users, it compares the characteristics of each song with the user's preferences.

The system considers seven features:

- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

Each song receives points based on how closely it matches the user's profile.

The scoring system awards:
- 2.0 points for an exact genre match.
- 1.0 point for an exact mood match.
- Up to 1.5 points for energy similarity.
- Up to 1.5 points for tempo similarity.
- Up to 1.0 point each for valence, danceability, and acousticness similarity.

For numerical features, the system awards more points when a song's value is closer to the user's target. The points are added together to produce a maximum possible score of 9.

Finally, the system ranks songs from highest to lowest score and returns the top three recommendations with explanations showing which features contributed points.

Compared with the original starter logic, which returned songs without calculating meaningful similarity scores, VibeFinder implements CSV loading, weighted scoring, ranking, and recommendation explanations.

---

## 4. Data

The model uses a CSV dataset containing **18 songs**.

Each song includes an ID, title, artist, genre, mood, and five numerical audio characteristics.

The catalog includes genres such as pop, rock, lofi, jazz, ambient, synthwave, indie pop, country, R&B, blues, reggae, metal, classical, funk, and house.

It also represents different moods, including happy, chill, intense, relaxed, moody, focused, nostalgic, romantic, melancholic, playful, aggressive, dreamy, confident, and euphoric.

The dataset was expanded beyond its initial 10 songs to include eight additional songs with different genres and moods.

Although the dataset provides variety for experimentation, it remains relatively small and does not represent the full diversity of music available in real-world streaming platforms.

---

## 5. Strengths

VibeFinder provides a simple and understandable way to connect musical preferences with recommendations.

Its strengths include:

- It considers both categorical preferences, such as genre and mood, and numerical audio characteristics.
- It gives partial credit for numerical similarities rather than requiring exact matches.
- It uses weighted scoring to give different importance to different preferences.
- It ranks songs consistently based on their calculated scores.
- It provides explanations that show why a song received its score.

In our initial pop/happy profile, Sunrise City received the highest score because it closely matched the user's genre, mood, and numerical preferences.

---

## 6. Limitations and Bias

VibeFinder has several limitations that may affect its recommendations.

**Genre bias:** Genre receives the highest individual weight. This may cause the system to prioritize songs from a favorite genre even when songs from other genres have stronger overall similarities.

**Strict mood matching:** Songs receive mood points only when their mood exactly matches the user's preferred mood. A song with a different but closely related mood receives no points for this feature.

**Limited user preferences:** The current profile supports only one favorite genre and one favorite mood. Real listeners often enjoy multiple genres and different moods depending on their activities.

**Small dataset:** The 18-song catalog does not adequately represent all musical genres, cultures, artists, or listening preferences.

**Limited audio characteristics:** The system does not consider lyrics, language, release date, artist popularity, listening history, or contextual information such as whether someone is studying, exercising, or relaxing.

**Subjective scoring weights:** The weights were selected manually for this classroom simulation. They may not reflect the actual preferences of every listener.

---

## 7. Evaluation

The recommender was evaluated by running the command-line simulation using a predefined pop/happy user profile.

The resulting recommendations were:

1. Sunrise City – 8.91/9
2. Gym Hero – 7.34/9
3. Rooftop Lights – 6.68/9

The results were reviewed to confirm that songs matching the user's preferred genre, mood, and numerical characteristics received higher scores.

The project also includes automated tests in `tests/test_recommender.py`. Both provided tests passed during verification.

The results demonstrate that the scoring and ranking logic works for the tested implementation, although further testing with different user profiles would be needed to evaluate recommendation quality more broadly.

---

## 8. Future Work

Possible improvements include:

- Supporting multiple favorite genres and moods.
- Allowing users to adjust the importance of different musical features.
- Testing additional user profiles to evaluate recommendation behavior.
- Increasing the size and diversity of the music catalog.
- Improving recommendation explanations to make every scoring contribution easier to understand.
- Introducing diversity into the top recommendations so that the system does not repeatedly suggest very similar songs.
- Exploring collaborative filtering as an alternative or complementary recommendation approach.

---

## 9. Personal Reflection

Building VibeFinder helped me understand how recommendation systems use item characteristics to identify content that may match a user's preferences.

One interesting discovery was that small changes in scoring weights can influence which songs appear at the top of the recommendation list. I also learned that recommending music is not simply about finding songs from the same genre; other characteristics, such as energy, tempo, and mood, can significantly influence the results.

This project gave me a better understanding of the logic behind music recommendation platforms and the importance of considering bias, diversity, and user preferences when designing recommendation systems.