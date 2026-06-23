# Quiz Application
# Features: Multiple questions, Score calculation, Timer, High-score storage
# Concepts: Lists, Dictionaries, Functions
# Challenge: Randomize questions

import random
import time

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Venus", "Jupiter"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Jane Austen", "Mark Twain"],
        "answer": "Harper Lee"
    },
    {
        "question": "Who is the main protagonist of 'Naruto'?",
        "options": ["Sasuke Uchiha", "Naruto Uzumaki", "Sakura Haruno"],
        "answer": "Naruto Uzumaki"
    },
    {
        "question": "What is the name of the demon slayer in 'Demon Slayer'?",
        "options": ["Tanjiro Kamado", "Inosuke Hashibira", "Zenitsu Agatsuma"],
        "answer": "Tanjiro Kamado"
    },
    {
        "question": "Who is the protagonist of 'One Piece'?",
        "options": ["Monkey D. Luffy", "Roronoa Zoro", "Nami"],
        "answer": "Monkey D. Luffy"
    },
    {
        "question": "Who is the main antagonist of 'Attack on Titan'?",
        "options": ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert"],
        "answer": "Eren Yeager"
    },
    {
        "question": "Who is the protagonist of 'My Hero Academia'?",
        "options": ["Izuku Midoriya", "Katsuki Bakugo", "Shoto Todoroki"],
        "answer": "Izuku Midoriya"
    }
]

# Stores all final scores across multiple quiz runs
high_scores = []

# ─────────────────────────────────────────────
def store_high_score(score):
    high_scores.append(score)
    print(f"🏆 New score recorded: {score}")
    print(f"🥇 Highest score so far: {max(high_scores)}")

# ─────────────────────────────────────────────
def quiz():
    score = 0
    total_questions = len(questions)
    max_score = total_questions * 5

    random.shuffle(questions)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1} of {total_questions}:")
        print(question["question"])

        options = question["options"]
        for j, option in enumerate(options):
            print(f"  {j + 1}. {option}")

        # Get valid input from user
        while True:
            user_input = input(f"Enter your answer (1-{len(options)}): ").strip()
            if user_input in [str(n) for n in range(1, len(options) + 1)]:
                break
            print(f"⚠️  Invalid input. Please enter a number between 1 and {len(options)}.")

        # Map the number they typed → actual answer text
        selected_option = options[int(user_input) - 1]

        # Check and give feedback
        if selected_option == question["answer"]:
            print("✅ Correct! +5 marks")
            score += 5
        else:
            print(f"❌ Incorrect! The correct answer was: {question['answer']} | 0 marks given")

        print(f"   Current score: {score}/{(i + 1) * 5} possible so far")

    # Quiz over — show final results
    print(f"\n{'='*40}")
    print(f"  Quiz Complete!")
    print(f"  Your final score: {score}/{max_score}")
    print(f"{'='*40}")

    store_high_score(score)
    return score

# ─────────────────────────────────────────────
# Main loop
while True:
    print("\n🎮 Welcome to the Quiz Application!")
    start_quiz = input("Do you want to start the quiz? (yes/no): ").strip().lower()

    if start_quiz == "yes":
        start_time = time.time()
        quiz()
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"⏱️  Time taken: {elapsed:.2f} seconds")
        break
    elif start_quiz == "no":
        print("Goodbye! Come back when you're ready 👋")
        break
    else:
        print("⚠️  Invalid input. Please type 'yes' or 'no'.")