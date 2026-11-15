# 🎧 VibeFinder 1.0 – Music Recommender Model Card

## 1. Model Name

**VibeFinder 1.0 – Music Recommender Simulation**

VibeFinder is a content-based music recommendation system that suggests songs based on a user's musical preferences.

## 2. Goal / Task

The goal of VibeFinder is to recommend songs that match a user's preferences.

The user provides a favorite genre, favorite mood, and target values for different audio features. The system calculates a score for each song, ranks the songs, and returns the five highest-scoring recommendations with explanations.

This project demonstrates how a simple recommendation algorithm can use song characteristics to suggest music without needing listening history or information from other users.

## 3. Data Used

The model uses a CSV dataset containing **18 songs**.

Each song includes an ID, title, artist, genre, mood, and five numerical audio characteristics:

- Energy
- Tempo
- Valence
- Danceability
- Acousticness

Five additional attributes were introduced in Challenge 1:

- Popularity
- Release decade
- Mood tags
- Language
- Instrumentalness

These attributes allow the system to consider more detailed musical preferences. The additional metadata in the demonstration dataset is illustrative and simulated.

The catalog includes genres such as pop, rock, lofi, jazz, ambient, synthwave, indie pop, country, R&B, blues, reggae, metal, classical, funk, and house.

The dataset was expanded from 10 to 18 songs to include more genres and moods.

Although the dataset provides variety for experimentation, it is still small compared with real-world music catalogs. This limits the diversity of recommendations the system can provide.

## 4. Algorithm Summary

VibeFinder uses **content-based filtering**. Instead of comparing listening histories between users, it compares the characteristics of each song with a user's preferences.

The system considers seven features:

- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

### Baseline Scoring Rules

The original scoring configuration awards:

- 2.0 points for an exact genre match.
- 1.0 point for an exact mood match.
- Up to 1.5 points for energy similarity.
- Up to 1.5 points for tempo similarity.
- Up to 1.0 point each for valence, danceability, and acousticness similarity.

For numerical features, songs receive more points when their values are closer to the user's target values.

The points are added together to produce a maximum baseline score of 9.

The system then sorts songs from highest to lowest score and returns the top five recommendations with explanations.

Compared with the original starter logic, VibeFinder implements CSV loading, weighted scoring, ranking, and recommendation explanations.

### Advanced Attributes and Strategy Pattern

Challenge 1 expanded the scoring system with five optional attributes: popularity, release decade, mood tags, language, and instrumentalness. When a user provides preferences for these attributes, the system can award additional points based on how well a song matches them.

Challenge 2 introduced the **Strategy design pattern** to make recommendation behavior more flexible.

Four strategies are available:

- **BalancedStrategy:** Uses balanced weights across recommendation features.
- **GenreFirstStrategy:** Gives greater importance to matching the user's favorite genre.
- **MoodFirstStrategy:** Gives greater importance to matching the user's preferred mood.
- **EnergyFirstStrategy:** Gives greater importance to matching the user's target energy level.

A shared `ScoringStrategy` class provides the scoring structure, while the individual strategies use different weights to influence song rankings.

The `Recommender` class accepts a strategy object. Its `set_strategy()` method allows the active strategy to be changed without rewriting the recommendation process.

The original function-based API was also preserved so the existing application could continue working.

This design makes VibeFinder easier to extend and experiment with because recommendation priorities can change independently of the main recommendation logic.


## 5. Observed Behavior, Strengths, and Biases

VibeFinder provides a simple and understandable way to connect musical preferences with recommendations.

Its strengths include:

- It considers both categorical preferences, such as genre and mood, and numerical audio characteristics.
- It gives partial credit for numerical similarities instead of requiring exact matches.
- It uses weighted scoring to give different importance to different preferences.
- It ranks songs consistently based on their calculated scores.
- It explains which features contributed to each recommendation.

In the High-Energy Pop profile, Sunrise City received the highest baseline score because it closely matched the user's genre, mood, and numerical preferences.

However, testing revealed an important weakness: the recommender does not penalize songs for contradicting a user's preferences.

For example, Gym Hero ranked first for the High-Energy Melancholic profile even though its mood was intense rather than melancholic. Its genre and numerical similarities helped it receive a high score.

This shows that matching some features can outweigh an important preference that does not match.

Another limitation is the small dataset. The system may repeatedly recommend similar songs because it has only 18 songs to choose from.

The scoring weights can also influence the results. Features with higher weights have more influence on the final recommendations.

## 6. Evaluation Process

I tested VibeFinder using four different user profiles:

1. **High-Energy Pop:** Favorite genre pop, happy mood, high energy, fast tempo, and high danceability.
2. **Chill Lofi:** Favorite genre lofi, chill mood, low energy, slower tempo, and high acousticness.
3. **Deep Intense Rock:** Favorite genre rock, intense mood, high energy, and fast tempo.
4. **High-Energy Melancholic:** Favorite genre pop, melancholic mood, high energy, fast tempo, and low valence. This profile was designed to test conflicting preferences.

### Baseline Results

The original scoring configuration produced these top recommendations:

- High-Energy Pop: Sunrise City (8.40/9)
- Chill Lofi: Library Rain (8.87/9)
- Deep Intense Rock: Storm Runner (8.76/9)
- High-Energy Melancholic: Gym Hero (7.04/9)

The first three results generally matched the intended musical preferences. The most surprising result was Gym Hero ranking first for the High-Energy Melancholic profile despite having an intense mood instead of a melancholic mood.

### Baseline Terminal Output

The following output shows the top five recommendations and their scoring explanations for all four profiles using the original weights.

```text
=======================================================
PROFILE: High-Energy Pop
=======================================================
1. Sunrise City - Score: 8.40/9
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+1.30), Tempo similarity (+1.35), Valence similarity (+0.94), Danceability similarity (+0.89), Acousticness similarity (+0.92)
2. Gym Hero - Score: 7.75/9
   Because: Genre match (+2.00), Energy similarity (+1.47), Tempo similarity (+1.47), Valence similarity (+0.87), Danceability similarity (+0.98), Acousticness similarity (+0.95)
3. Rooftop Lights - Score: 6.22/9
   Because: Mood match (+1.00), Energy similarity (+1.22), Tempo similarity (+1.42), Valence similarity (+0.91), Danceability similarity (+0.92), Acousticness similarity (+0.75)
4. Neon Fever - Score: 5.84/9
   Because: Energy similarity (+1.40), Tempo similarity (+1.47), Valence similarity (+0.99), Danceability similarity (+1.00), Acousticness similarity (+0.98)
5. Funky Friday - Score: 5.58/9
   Because: Energy similarity (+1.35), Tempo similarity (+1.31), Valence similarity (+0.98), Danceability similarity (+0.96), Acousticness similarity (+0.98)

=======================================================
PROFILE: Chill Lofi
=======================================================
1. Library Rain - Score: 8.87/9
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+1.50), Tempo similarity (+1.46), Valence similarity (+1.00), Danceability similarity (+0.97), Acousticness similarity (+0.94)
2. Midnight Coding - Score: 8.66/9
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+1.40), Tempo similarity (+1.46), Valence similarity (+0.96), Danceability similarity (+0.93), Acousticness similarity (+0.91)
3. Focus Flow - Score: 7.78/9
   Because: Genre match (+2.00), Energy similarity (+1.42), Tempo similarity (+1.44), Valence similarity (+0.99), Danceability similarity (+0.95), Acousticness similarity (+0.98)
4. Spacewalk Thoughts - Score: 6.40/9
   Because: Mood match (+1.00), Energy similarity (+1.40), Tempo similarity (+1.31), Valence similarity (+0.95), Danceability similarity (+0.86), Acousticness similarity (+0.88)
5. Coffee Shop Stories - Score: 5.57/9
   Because: Energy similarity (+1.47), Tempo similarity (+1.31), Valence similarity (+0.89), Danceability similarity (+0.99), Acousticness similarity (+0.91)

=======================================================
PROFILE: Deep Intense Rock
=======================================================
1. Storm Runner - Score: 8.76/9
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+1.44), Tempo similarity (+1.46), Valence similarity (+0.92), Danceability similarity (+0.94), Acousticness similarity (+1.00)
2. Gym Hero - Score: 5.98/9
   Because: Mood match (+1.00), Energy similarity (+1.47), Tempo similarity (+1.21), Valence similarity (+0.63), Danceability similarity (+0.72), Acousticness similarity (+0.95)
3. Iron Thunder - Score: 5.74/9
   Because: Energy similarity (+1.48), Tempo similarity (+1.38), Valence similarity (+0.95), Danceability similarity (+0.99), Acousticness similarity (+0.94)
4. Night Drive Loop - Score: 4.80/9
   Because: Energy similarity (+1.20), Tempo similarity (+0.94), Valence similarity (+0.91), Danceability similarity (+0.87), Acousticness similarity (+0.88)
5. Neon Fever - Score: 4.73/9
   Because: Energy similarity (+1.40), Tempo similarity (+1.16), Valence similarity (+0.49), Danceability similarity (+0.70), Acousticness similarity (+0.98)

=======================================================
PROFILE: High-Energy Melancholic
=======================================================
1. Gym Hero - Score: 7.04/9
   Because: Genre match (+2.00), Energy similarity (+1.47), Tempo similarity (+1.27), Valence similarity (+0.43), Danceability similarity (+0.92), Acousticness similarity (+0.95)
2. Sunrise City - Score: 6.67/9
   Because: Genre match (+2.00), Energy similarity (+1.30), Tempo similarity (+1.10), Valence similarity (+0.36), Danceability similarity (+0.99), Acousticness similarity (+0.92)
3. Storm Runner - Score: 5.50/9
   Because: Energy similarity (+1.44), Tempo similarity (+1.47), Valence similarity (+0.72), Danceability similarity (+0.86), Acousticness similarity (+1.00)
4. Iron Thunder - Score: 5.38/9
   Because: Energy similarity (+1.48), Tempo similarity (+1.31), Valence similarity (+0.85), Danceability similarity (+0.79), Acousticness similarity (+0.94)
5. Neon Fever - Score: 4.79/9
   Because: Energy similarity (+1.40), Tempo similarity (+1.23), Valence similarity (+0.29), Danceability similarity (+0.90), Acousticness similarity (+0.98)
```

### Profile Comparisons

- **High-Energy Pop vs. Chill Lofi:** Sunrise City ranked first for the pop profile, while Library Rain ranked first for the lofi profile. Their different genre, mood, and energy preferences explain the different results.
- **High-Energy Pop vs. Deep Intense Rock:** Sunrise City ranked first for pop, while Storm Runner ranked first for rock. Storm Runner received points for matching both the rock genre and intense mood.
- **High-Energy Pop vs. High-Energy Melancholic:** Both profiles ranked Gym Hero and Sunrise City highly. However, Gym Hero won for the melancholic profile because its pop genre and numerical similarities outweighed the absence of a mood match.
- **Chill Lofi vs. Deep Intense Rock:** Library Rain ranked first for chill lofi, while Storm Runner ranked first for intense rock. Their different target energy and tempo values contributed to the results.
- **Chill Lofi vs. High-Energy Melancholic:** Library Rain ranked first for chill lofi, while Gym Hero ranked first for the melancholic profile. Their contrasting energy and valence preferences explain much of the difference.
- **Deep Intense Rock vs. High-Energy Melancholic:** Storm Runner ranked first for rock, while Gym Hero ranked first for the melancholic profile. Genre and mood matches influenced the results, while high energy benefited several songs in both profiles.

### Weight-Shift Experiment

I conducted an experiment by reducing the genre weight from 2 to 1 point and increasing the energy weight from 1.5 to 3 points.

The experimental scoring configuration became:

- Genre: 1.0 point.
- Mood: 1.0 point.
- Energy: up to 3.0 points.
- Tempo: up to 1.5 points.
- Valence: up to 1.0 point.
- Danceability: up to 1.0 point.
- Acousticness: up to 1.0 point.

The maximum possible experimental score increased from 9 to 9.5 points.

The experimental top recommendations remained the same for all four profiles:

- High-Energy Pop: Sunrise City (8.71/9.5)
- Chill Lofi: Library Rain (9.37/9.5)
- Deep Intense Rock: Storm Runner (9.20/9.5)
- High-Energy Melancholic: Gym Hero (7.51/9.5)

Although the top-ranked songs did not change, several lower-ranked songs became more competitive. For example, Iron Thunder increased from 5.74 to 7.22 for the Deep Intense Rock profile because of its high energy similarity.

The experiment showed that changing weights affects the importance of individual preferences, but does not necessarily improve recommendation quality. Higher scores do not automatically mean better recommendations.

### Experimental Terminal Output

The following output shows the top five recommendations and their scoring explanations for all four profiles after changing the genre and energy weights.

```text
=======================================================
PROFILE: High-Energy Pop
=======================================================
1. Sunrise City - Score: 8.71/9.5
   Because: Genre match (+1.00), Mood match (+1.00), Energy similarity (+2.61), Tempo similarity (+1.35), Valence similarity (+0.94), Danceability similarity (+0.89), Acousticness similarity (+0.92)
2. Gym Hero - Score: 8.21/9.5
   Because: Genre match (+1.00), Energy similarity (+2.94), Tempo similarity (+1.47), Valence similarity (+0.87), Danceability similarity (+0.98), Acousticness similarity (+0.95)
3. Rooftop Lights - Score: 7.44/9.5
   Because: Mood match (+1.00), Energy similarity (+2.43), Tempo similarity (+1.42), Valence similarity (+0.91), Danceability similarity (+0.92), Acousticness similarity (+0.75)
4. Neon Fever - Score: 7.23/9.5
   Because: Energy similarity (+2.79), Tempo similarity (+1.47), Valence similarity (+0.99), Danceability similarity (+1.00), Acousticness similarity (+0.98)
5. Funky Friday - Score: 6.93/9.5
   Because: Energy similarity (+2.70), Tempo similarity (+1.31), Valence similarity (+0.98), Danceability similarity (+0.96), Acousticness similarity (+0.98)

=======================================================
PROFILE: Chill Lofi
=======================================================
1. Library Rain - Score: 9.37/9.5
   Because: Genre match (+1.00), Mood match (+1.00), Energy similarity (+3.00), Tempo similarity (+1.46), Valence similarity (+1.00), Danceability similarity (+0.97), Acousticness similarity (+0.94)
2. Midnight Coding - Score: 9.05/9.5
   Because: Genre match (+1.00), Mood match (+1.00), Energy similarity (+2.79), Tempo similarity (+1.46), Valence similarity (+0.96), Danceability similarity (+0.93), Acousticness similarity (+0.91)
3. Focus Flow - Score: 8.21/9.5
   Because: Genre match (+1.00), Energy similarity (+2.85), Tempo similarity (+1.44), Valence similarity (+0.99), Danceability similarity (+0.95), Acousticness similarity (+0.98)
4. Spacewalk Thoughts - Score: 7.79/9.5
   Because: Mood match (+1.00), Energy similarity (+2.79), Tempo similarity (+1.31), Valence similarity (+0.95), Danceability similarity (+0.86), Acousticness similarity (+0.88)
5. Coffee Shop Stories - Score: 7.04/9.5
   Because: Energy similarity (+2.94), Tempo similarity (+1.31), Valence similarity (+0.89), Danceability similarity (+0.99), Acousticness similarity (+0.91)

=======================================================
PROFILE: Deep Intense Rock
=======================================================
1. Storm Runner - Score: 9.20/9.5
   Because: Genre match (+1.00), Mood match (+1.00), Energy similarity (+2.88), Tempo similarity (+1.46), Valence similarity (+0.92), Danceability similarity (+0.94), Acousticness similarity (+1.00)
2. Gym Hero - Score: 7.45/9.5
   Because: Mood match (+1.00), Energy similarity (+2.94), Tempo similarity (+1.21), Valence similarity (+0.63), Danceability similarity (+0.72), Acousticness similarity (+0.95)
3. Iron Thunder - Score: 7.22/9.5
   Because: Energy similarity (+2.97), Tempo similarity (+1.38), Valence similarity (+0.95), Danceability similarity (+0.99), Acousticness similarity (+0.94)
4. Neon Fever - Score: 6.12/9.5
   Because: Energy similarity (+2.79), Tempo similarity (+1.16), Valence similarity (+0.49), Danceability similarity (+0.70), Acousticness similarity (+0.98)
5. Night Drive Loop - Score: 6.00/9.5
   Because: Energy similarity (+2.40), Tempo similarity (+0.94), Valence similarity (+0.91), Danceability similarity (+0.87), Acousticness similarity (+0.88)

=======================================================
PROFILE: High-Energy Melancholic
=======================================================
1. Gym Hero - Score: 7.51/9.5
   Because: Genre match (+1.00), Energy similarity (+2.94), Tempo similarity (+1.27), Valence similarity (+0.43), Danceability similarity (+0.92), Acousticness similarity (+0.95)
2. Sunrise City - Score: 6.98/9.5
   Because: Genre match (+1.00), Energy similarity (+2.61), Tempo similarity (+1.10), Valence similarity (+0.36), Danceability similarity (+0.99), Acousticness similarity (+0.92)
3. Storm Runner - Score: 6.94/9.5
   Because: Energy similarity (+2.88), Tempo similarity (+1.47), Valence similarity (+0.72), Danceability similarity (+0.86), Acousticness similarity (+1.00)
4. Iron Thunder - Score: 6.86/9.5
   Because: Energy similarity (+2.97), Tempo similarity (+1.31), Valence similarity (+0.85), Danceability similarity (+0.79), Acousticness similarity (+0.94)
5. Neon Fever - Score: 6.19/9.5
   Because: Energy similarity (+2.79), Tempo similarity (+1.23), Valence similarity (+0.29), Danceability similarity (+0.90), Acousticness similarity (+0.98)
```

### Strategy Pattern Experiment

To evaluate the different recommendation strategies, I used the same user profile and song catalog with all four strategies.

The strategies produced the following top-ranked songs:

| Strategy | First recommended song |
|---|---|
| Genre First | Pop Track |
| Mood First | Happy Rock |
| Energy First | Pop Track |
| Balanced | Pop Track |

The Mood First strategy ranked Happy Rock first, while Genre First ranked Pop Track first. This showed that changing the importance of recommendation features can change the ranking of songs.

The experiment demonstrated that different recommendation strategies can prioritize different aspects of a user's musical preferences while using the same underlying recommendation system.

## 7. Intended Use and Non-Intended Use

**Intended Use**

VibeFinder is designed for classroom learning and experimentation. It demonstrates how a recommendation algorithm can compare item characteristics with user preferences.

It is useful for learning about content-based filtering, weighted scoring, and basic recommendation systems.

**Non-Intended Use**

VibeFinder is not designed to replace commercial music streaming platforms or provide large-scale personalized recommendations.

It does not learn from listening history, understand personal taste deeply, or consider the behavior of other users. Its small dataset also makes it unsuitable for real-world music recommendation at scale.

## 8. Ideas for Improvement

If I continued developing VibeFinder, I would:

- Increase the size and diversity of the music dataset.
- Add penalties for important preference mismatches.
- Allow users to adjust the importance of different music features.

I would also explore collaborative filtering to compare recommendations based on similarities between users.

## 9. Personal Reflection

Building VibeFinder helped me understand how recommendation systems work behind the scenes.

My biggest learning moment was discovering that changing the scoring weights could affect recommendation scores and make different songs more competitive. I initially thought matching a user's favorite genre would have the greatest influence. However, testing different profiles showed me that energy, tempo, and other features can also strongly influence the results.

Using AI tools helped me understand concepts, debug Python errors, improve my code, and explore different ways to implement the recommendation algorithm. However, I learned that I should not blindly trust AI-generated code or explanations. I needed to run the program, inspect the output, and double-check whether the recommendations and calculations actually made sense.

I was surprised that even a relatively simple scoring algorithm could produce recommendations that felt meaningful. By comparing song characteristics with user preferences, the system generated different results for different profiles without needing a complex machine learning model.

If I extended this project, I would increase the dataset, improve how the system handles conflicting preferences, and explore collaborative filtering. I would also try to make the recommendations more diverse so that users receive a wider variety of songs.

Overall, this project taught me that building an AI system is not just about making it work. It is also about testing its behavior, identifying its limitations, and understanding how design decisions affect its results.

The second challenge expanded my understanding of object-oriented programming and software design. Implementing the Strategy design pattern taught me how to separate recommendation behavior from the main recommendation process. I also learned that different scoring priorities can produce different rankings, even when the same dataset and user preferences are used. This made the system more flexible and easier to extend.