# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---
## How The System Works

### Recommendation Approach

Our simulation uses **content-based filtering** to recommend songs based on a user's musical preferences. Rather than comparing users with similar listening histories, the system compares each song's characteristics against a predefined user profile.

The dataset contains 18 songs across different genres and moods. Each song includes attributes such as genre, mood, energy, tempo, valence, danceability, and acousticness.

### User Profile

For our initial simulation, we use the following user preferences:

| Preference | Target |
|---|---|
| Favorite Genre | Pop |
| Favorite Mood | Happy |
| Target Energy | 0.80 |
| Target Tempo | 120 BPM |
| Target Valence | 0.85 |
| Target Danceability | 0.80 |
| Target Acousticness | 0.20 |

### Finalized Algorithm Recipe

The recommender calculates a weighted similarity score for every song.

**1. Genre matching:** +2.0 points for an exact genre match.

**2. Mood matching:** +1.0 point for an exact mood match.

**3. Numerical feature similarity:** Songs receive partial points based on how close their audio characteristics are to the user's targets.

We use the following weights:

| Feature | Maximum Points |
|---|---:|
| Genre | 2.0 |
| Mood | 1.0 |
| Energy | 1.5 |
| Tempo | 1.5 |
| Valence | 1.0 |
| Danceability | 1.0 |
| Acousticness | 1.0 |
| **Maximum Total** | **9.0** |

For numerical features, similarity is calculated using:

**Similarity = 1 − (Absolute Difference / Feature Range)**

For energy, valence, danceability, and acousticness, the feature range is 1. For tempo, we use a comparison range of 120 BPM. Negative similarity values are treated as zero.

The similarity value is multiplied by the feature's maximum points to determine its contribution to the final score.

**4. Scoring and ranking:** The system adds all feature points to calculate each song's total score, sorts songs from highest to lowest, and returns the top three recommendations.

### Potential Biases and Limitations

Our scoring strategy has some potential limitations:

- **Genre bias:** Genre receives the highest individual weight (2 points). This may prioritize songs from a user's favorite genre even when songs from other genres better match their overall mood or audio preferences.
- **Mood limitations:** Exact mood matching gives no points to songs with different moods, even when their other characteristics closely match the user's taste.
- **Limited user profile:** Our initial profile uses one favorite genre and one favorite mood. Real listeners often enjoy multiple genres and moods.
- **Subjective weights:** The scoring weights are manually selected for this simulation and may not accurately represent every user's musical preferences.
- **Limited dataset:** Our 18-song dataset is relatively small and cannot represent the diversity of real-world music catalogs.

Future improvements could include multiple preferred genres and moods, adjustable feature weights, and a larger, more diverse dataset.

### Implementation Plan

The system is organized into the following stages:

1. Load song information from the CSV dataset.
2. Compare song attributes against the user's profile.
3. Calculate weighted similarity scores.
4. Rank songs by their total scores.
5. Return the three highest-scoring recommendations with explanations.

## Simulation Features

### Song Object

Each `Song` object will contain:

- `id`: Unique identifier for the song.
- `title`: Name of the song.
- `artist`: Name of the artist.
- `genre`: Musical genre (e.g., pop, rock, lofi).
- `mood`: Emotional character of the song (e.g., happy, chill, intense).
- `energy`: Energy level (0–1).
- `tempo_bpm`: Song tempo measured in beats per minute.
- `valence`: Musical positivity (0–1).
- `danceability`: Danceability score (0–1).
- `acousticness`: Acoustic character score (0–1).

### UserProfile Object

Each `UserProfile` object will contain:

- `preferred_genres`: Genres the user enjoys.
- `preferred_moods`: Moods the user prefers.
- `preferred_energy`: Desired energy level (0–1).
- `preferred_tempo`: Preferred tempo in BPM.
- `preferred_valence`: Desired musical positivity (0–1).
- `preferred_danceability`: Desired danceability level (0–1).
- `preferred_acousticness`: Desired acousticness level (0–1).

## Recommendation Logic

1. **Feature Comparison:** Compare each song's characteristics against the user's preferences.
2. **Similarity Scoring:** Calculate similarity for categorical and numerical features.
3. **Weighted Scoring:** Combine individual similarity scores using predefined feature weights.
4. **Ranking:** Sort songs from highest to lowest similarity score.
5. **Recommendations:** Return the top three songs, excluding songs the user has already selected as favorites.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

The following output was generated by running `python3 -m src.main` with the default pop/happy user profile.

```text
Loaded songs: 18

Top 3 Recommendations:

Sunrise City - Score: 8.91/9
Because: Genre match (+2.00), Mood match (+1.00), Energy similarity(+1.47), Tempo similarity (+1.47), Valence similarity (+0.99), Danceability similarity (+0.99), Acousticness similarity (+0.98)

Gym Hero - Score: 7.34/9
Because: Genre match (+2.00), Energy similarity (+1.30), Tempo similarity (+1.35), Valence similarity (+0.92), Danceability similarity (+0.92), Acousticness similarity (+0.85)

Rooftop Lights - Score: 6.68/9
Because: Mood match (+1.00), Energy similarity (+1.44), Tempo similarity (+1.45), Valence similarity (+0.96), Danceability similarity (+0.98), Acousticness similarity (+0.85)
```
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



