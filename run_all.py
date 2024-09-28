import subprocess

def run_selenium_covers():
    print("Running selenium_covers.py...")
    subprocess.run(["python", "selenium_covers.py"], check=True)

def run_ai_book_desc():
    print("Running ai_book_desc.py...")
    subprocess.run(["python", "ai_book_desc.py"], check=True)

def main():
    try:
        run_selenium_covers()
        run_ai_book_desc()
        print("All processes completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()