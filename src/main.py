
from src.recommender import load_songs, recommend_songs


def main():
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo": 120,
        "target_valence": 0.85,
        "target_danceability": 0.80,
        "target_acousticness": 0.20
    }

    recommendations = recommend_songs(user_prefs, songs, k=3)

    print("\nTop 3 Recommendations:\n")

    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}/9")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
