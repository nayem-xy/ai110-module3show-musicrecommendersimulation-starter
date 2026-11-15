
from src.recommender import load_songs, recommend_songs


def get_max_score(user_prefs):
    """Calculate the maximum possible score for this preference profile."""

    max_score = 9.5

    if user_prefs.get("target_popularity") is not None:
        max_score += 0.5

    if user_prefs.get("preferred_decade") is not None:
        max_score += 0.5

    if user_prefs.get("preferred_mood_tags"):
        max_score += 1.0

    if user_prefs.get("preferred_language") is not None:
        max_score += 0.5

    if user_prefs.get("target_instrumentalness") is not None:
        max_score += 0.5

    return max_score


def main():

    # Load song catalog
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Define user preference profiles
    user_profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.95,
            "target_tempo": 130,
            "target_valence": 0.90,
            "target_danceability": 0.90,
            "target_acousticness": 0.10
        },

        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.35,
            "target_tempo": 75,
            "target_valence": 0.60,
            "target_danceability": 0.55,
            "target_acousticness": 0.80
        },

        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_tempo": 155,
            "target_valence": 0.40,
            "target_danceability": 0.60,
            "target_acousticness": 0.10
        },

        "Advanced High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.95,
            "target_tempo": 130,
            "target_valence": 0.90,
            "target_danceability": 0.90,
            "target_acousticness": 0.10,

            # Advanced preferences
            "target_popularity": 85,
            "preferred_decade": 2020,
            "preferred_mood_tags": ["euphoric", "energetic"],
            "preferred_language": "English",
            "target_instrumentalness": 0.05
        },
    }

    # Test each profile and display its top 5 recommendations
    for profile_name, user_prefs in user_profiles.items():

        recommendations = recommend_songs(user_prefs, songs, k=5)
        max_score = get_max_score(user_prefs)

        print(f"\n{'=' * 55}")
        print(f"PROFILE: {profile_name}")
        print(f"{'=' * 55}")

        for rank, (song, score, explanation) in enumerate(
            recommendations, start=1
        ):
            print(
                f"{rank}. {song['title']} - "
                f"Score: {score:.2f}/{max_score:.1f}"
            )
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
