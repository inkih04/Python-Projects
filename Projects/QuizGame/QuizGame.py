


questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]


def main():
    score = 0
    for quests in questions:
        print(quests["prompt"])
        for opts in quests["options"]:
            print(opts)
        answer = input("").strip().upper()
        if answer == quests["answer"]:
            score +=1
            print("Correct")
        else: 
            print(f"Wrong\nThe correct answer was {quests['answer']}")
    print(f"Your score is {score} !!")


if __name__ == "__main__":
    main()