# AI Interaction Log – VibeFinder 1.0

## Challenge 1: Advanced Song Attributes

### Objective
Expand the music recommendation system by introducing at least five additional song attributes and incorporating them into the recommendation scoring algorithm.

### 1. Advanced Attributes Added

Five attributes were added to `data/songs.csv`:

| Attribute | Description |
|---|---|
| `popularity` | Song popularity score from 0–100 |
| `release_decade` | Decade in which the song was released |
| `mood_tags` | Multiple descriptive mood tags |
| `language` | Song language |
| `instrumentalness` | Degree to which a song is instrumental (0–1) |

The additional metadata in the demonstration dataset is illustrative and simulated.

### 2. AI Assistance

ChatGPT was used to:
- Brainstorm useful advanced song attributes.
- Help update the CSV structure.
- Modify `load_songs()` to parse the new attributes into appropriate Python data types.
- Extend `score_song()` to calculate similarity using the new attributes.
- Generate explanations showing why each song received additional points.
- Troubleshoot CSV formatting and Python implementation errors.

### 3. Scoring Implementation

The original scoring system had a maximum possible score of 9.5 points.

The advanced features introduced these additional weights:

| Feature | Maximum points |
|---|---:|
| Popularity similarity | 0.5 |
| Release decade match | 0.5 |
| Mood tag similarity | 1.0 |
| Language match | 0.5 |
| Instrumentalness similarity | 0.5 |
| **Total additional points** | **3.0** |

Advanced preferences are optional. The original profiles continue using the original scoring system, while profiles specifying advanced preferences receive additional scoring opportunities.

### 4. Testing and Verification

The following tests were completed:

- Successfully loaded all 18 songs from the updated CSV.
- Verified that the five new attributes were parsed correctly.
- Tested the original three user profiles.
- Created an advanced High-Energy Pop profile using all five new attributes.
- Verified that the advanced profile's maximum possible score was 12.5.
- Confirmed that recommendations included explanations for advanced feature matches.

**Example result:** Sunrise City ranked first for Advanced High-Energy Pop with a score of 11.69/12.5.

### 5. What I Learned

This challenge helped me understand how adding more meaningful features can improve a recommendation system. I also learned how optional user preferences without breaking its original behavior.

AI assistance was useful for brainstorming, implementation guidance, and debugging, but I manually ran the program and verified the resulting recommendations and scores.

---

## Challenge 2: Strategy Pattern

### Objective

Refactor the recommendation system to support multiple recommendation strategies using object-oriented programming and the Strategy design pattern.

### 1. Strategies Implemented

Four recommendation strategies were added:

| Strategy | Description |
|---|---|
| `BalancedStrategy` | Uses balanced weights across recommendation features |
| `GenreFirstStrategy` | Gives greater importance to matching the user's favorite genre |
| `MoodFirstStrategy` | Gives greater importance to matching the user's preferred mood |
| `EnergyFirstStrategy` | Gives greater importance to matching the user's target energy level |

A shared `ScoringStrategy` class provides the scoring structure. Each strategy uses different feature weights to influence the final ranking.

### 2. AI Assistance

ChatGPT was used to:
- Understand the Strategy design pattern and how it applies to recommendation systems.
- Plan the strategy class structure.
- Refactor the scoring logic into reusable classes.
- Implement the four recommendation strategies.
- Add the ability to change the active strategy using `set_strategy()`.
- Troubleshoot implementation issues while preserving the existing function-based API.

### 3. Implementation

The `Recommender` class accepts a strategy object and uses it to rank songs. The active strategy can be changed without rewriting the recommendation logic.

The existing functions, including `score_song()` and `recommend_songs()`, were preserved so the original application could continue working.

This design separates the recommendation process from the scoring weights. It makes the system easier to extend because a new strategy can be added without rewriting the entire recommender.

### 4. Testing and Verification

The following tests and experiments were completed:

- Tested all four strategies using the same songs and user profile.
- Compared the rankings produced by each strategy.
- Verified that different strategies could produce different recommendation orders.
- Confirmed that the application still ran successfully.
- Ran the automated test suite successfully: **2 tests passed**.

**Example results:**

| Strategy | First recommended song |
|---|---|
| Genre First | Pop Track |
| Mood First | Happy Rock |
| Energy First | Pop Track |
| Balanced | Pop Track |

The Mood First strategy ranked Happy Rock first, while Genre First ranked Pop Track first. This demonstrated how changing feature weights can influence recommendation results.

### 5. What I Learned

This challenge helped me understand how the Strategy design pattern can make a recommendation system more flexible and maintainable. I learned how to use classes and objects to separate scoring behavior from the main recommendation process.

I also learned that different recommendation strategies can use the same underlying features but prioritize them differently. This allows a system to support different recommendation approaches without duplicating the entire algorithm.

AI assistance helped me understand the design pattern, organize the implementation, and debug issues. I tested the strategies and verified the application and automated tests myself.
