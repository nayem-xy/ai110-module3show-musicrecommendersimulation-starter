# 🎧 VibeFinder 1.0 — Content-Based Music Recommender

VibeFinder is a Python-based music recommendation system that recommends songs based on a user's musical preferences. It uses content-based filtering and weighted similarity scoring to compare song characteristics with a user profile.

The project explores how recommendation systems turn data into personalized suggestions, how scoring weights influence results, and how different recommendation strategies can produce different rankings.

## ✨ Features

- **Content-based filtering:** Matches song characteristics against a user's preferences.
- **Weighted similarity scoring:** Evaluates genre, mood, energy, tempo, valence, danceability, and acousticness.
- **Advanced song attributes:** Incorporates popularity, release decade, mood tags, language, and instrumentalness.
- **Four recommendation strategies:** Balanced, Genre First, Mood First, and Energy First.
- **Recommendation explanations:** Shows why each song received its score.
- **Multiple user profiles:** Demonstrates how recommendations change for different listening preferences.
- **CSV dataset:** Loads song information from a structured dataset.

## 🧠 How It Works

### 1. Song Data

The dataset contains 18 illustrative songs. Each song includes:

| Attribute | Description |
|---|---|
| Genre | Musical category, such as pop, rock, or lofi |
| Mood | Emotional character of the song |
| Energy | Energy level (0–1) |
| Tempo | Beats per minute (BPM) |
| Valence | Musical positivity (0–1) |
| Danceability | Danceability score (0–1) |
| Acousticness | Acoustic character (0–1) |
| Popularity | Illustrative popularity score |
| Release decade | Song's release decade |
| Mood tags | Additional descriptive mood labels |
| Language | Song language |
| Instrumentalness | Estimated instrumental character (0–1) |

The additional metadata is illustrative and simulated for this project.

### 2. User Profile

A `UserProfile` represents a listener's preferences, including:

- Favorite genre and mood
- Target energy level
- Preferred tempo
- Target valence, danceability, and acousticness
- Optional preferences for popularity, release decade, mood tags, language, and instrumentalness

### 3. Recommendation Scoring

The system calculates a weighted score for each song based on how closely its characteristics match the user profile.

The standard scoring configuration uses these maximum weights:

| Feature | Maximum Points |
|---|---:|
| Genre | 1.0 |
| Mood | 1.0 |
| Energy | 3.0 |
| Tempo | 1.5 |
| Valence | 1.0 |
| Danceability | 1.0 |
| Acousticness | 1.0 |
| **Maximum Total** | **9.5** |

Numerical features receive partial credit based on similarity to the user's target values. The system combines the individual contributions to calculate each song's total score.

Advanced preferences can contribute up to an additional 3 points, bringing the maximum advanced score to **12.5**.

### 4. Recommendation Strategies

VibeFinder uses the **Strategy Design Pattern** to support different recommendation approaches.

| Strategy | Main Focus |
|---|---|
| Balanced | Distributes importance across the main features |
| Genre First | Gives genre matching greater priority |
| Mood First | Prioritizes mood similarity |
| Energy First | Gives energy similarity greater priority |

The `Recommender` class accepts a strategy and allows it to be changed using `set_strategy()`. This separates recommendation behavior from the rest of the application and makes it easier to experiment with different approaches.

The project also preserves the `score_song()` and `recommend_songs()` function-based API.

## 🛠️ Technologies

- Python
- CSV
- Object-Oriented Programming
- Content-Based Filtering
- Strategy Design Pattern
- Pytest

## 🚀 Getting Started

### Prerequisites

- Python 3
- Git

### 1. Clone the repository

```bash
git clone https://github.com/nayem-xy/ai110-module3show-musicrecommendersimulation-starter.git
cd ai110-module3show-musicrecommendersimulation-starter
```

### 2. Create and activate a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

From the project root:

```bash
python3 -m src.main
```

The application loads the CSV dataset and displays recommendations for four example user profiles.

## 🧪 Running Tests

Run the automated tests with:

```bash
python3 -m pytest -q
```

## 📊 Sample Output

Example from the completed application:

```text
Loaded songs: 18

PROFILE: High-Energy Pop

1. Sunrise City - Score: 8.71/9.5
2. Gym Hero - Score: 8.21/9.5
3. Rooftop Lights - Score: 7.44/9.5
4. Neon Fever - Score: 7.23/9.5
5. Funky Friday - Score: 6.93/9.5

PROFILE: Chill Lofi

1. Library Rain - Score: 9.37/9.5
2. Midnight Coding - Score: 9.05/9.5
3. Focus Flow - Score: 8.21/9.5
```

The application also demonstrates advanced scoring with additional user preferences, producing scores out of 12.5.

## 🔬 Experiments and Evaluation

Several experiments were conducted during development:

- Compared recommendation results across different user profiles.
- Adjusted scoring weights to examine how feature importance changes rankings.
- Added advanced song attributes to expand personalization.
- Implemented four recommendation strategies and compared their top-ranked songs.

One strategy experiment produced these top recommendations:

| Strategy | Top Recommendation |
|---|---|
| Genre First | Pop Track |
| Mood First | Happy Rock |
| Energy First | Pop Track |
| Balanced | Pop Track |

The different results demonstrate how changing the importance of features can influence recommendation behavior.

## ⚠️ Limitations

- The dataset contains only 18 songs and is not representative of a real streaming catalog.
- Some advanced song metadata is simulated.
- Scoring weights are manually selected rather than learned from real listening behavior.
- The system does not analyze lyrics, listening history, or user feedback.
- Content-based recommendations can limit discovery outside a user's stated preferences.
- The project is an educational simulation, not a production-ready recommendation platform.

## 🔮 Future Improvements

- Expand the dataset with real music metadata.
- Incorporate listening history and user feedback.
- Allow users to customize scoring weights.
- Build an interactive interface.
- Evaluate recommendations using larger datasets and more comprehensive metrics.

## 📁 Project Structure

```text
├── data/
│   └── songs.csv
├── src/
│   ├── main.py
│   ├── recommender.py
│   └── ai_interactions.md
├── tests/
│   └── test_recommender.py
├── model_card.md
├── requirements.txt
└── README.md
```

## 📚 Documentation

- [Model Card](model_card.md) — Detailed explanation of the model, evaluation, observed behavior, biases, and reflection.
- [AI Interaction Log](src/ai_interactions.md) — Documentation of AI-assisted development and implementation decisions.

## 💡 What I Learned

Building VibeFinder helped me understand how recommendation systems transform user preferences and item characteristics into personalized recommendations. Initially, I thought recommending music was mainly about matching a user's favorite genre and mood. However, experimenting with different scoring weights showed me that even small changes in feature importance can significantly affect recommendation rankings. Adding advanced attributes such as popularity, release decade, mood tags, language, and instrumentalness also helped me explore how a recommendation system can consider more than basic genre and audio preferences.

One of my biggest learning experiences was implementing the Strategy Design Pattern. Creating Balanced, Genre First, Mood First, and Energy First strategies taught me how object-oriented programming can separate an algorithm's behavior from the main recommendation system. Instead of rewriting the recommender whenever I wanted to experiment with a different approach, I could switch strategies while keeping the rest of the system consistent.

This project also made me think more critically about bias in AI systems. A recommendation system reflects the choices made by its developers, including which features receive more weight and which data is included. A system that prioritizes genre too heavily might repeatedly recommend similar music and limit opportunities for users to discover something new. I learned that building a recommendation system is not just about producing high scores; it is also about understanding the assumptions, limitations, and potential consequences behind those scores.
---

**Project:** VibeFinder 1.0  
**Language:** Python  
**Focus:** Content-Based Music Recommendation Systems