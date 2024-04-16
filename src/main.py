import argparse

from data import data
from riddles import RiddleSource

def create_argparser():
    parser = argparse.ArgumentParser(description="Fetch and display riddles.")
    # Set default=1 to ensure that count defaults to 1 if not provided
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of riddles to retrieve, defaults to 1 if not provided.")
    return parser

def main():
    parser = create_argparser()
    args = parser.parse_args()

    # Initialize the RiddleSource object with data
    rsobj = RiddleSource(data)

    try:
        # Check for positive count
        if args.count < 1:
            raise ValueError("Count must be at least 1.")

        # Fetch one riddle if count is 1 or multiple riddles if count > 1
        if args.count == 1:
            riddle = rsobj.get_riddle()
        else:
            riddle = rsobj.get_riddles(count=args.count)
        
        # Output the riddle(s)
        if isinstance(riddle, list):
            for r in riddle:
                print(f"Riddle: {r['question']}")
                print(f"Answer: {r['answer'][0]}")
        else:
            print(f"Riddle: {riddle['question']}")
            print(f"Answer: {riddle['answer'][0]}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

if __name__ == "__main__":
    main()
