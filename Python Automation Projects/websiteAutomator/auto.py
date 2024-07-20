import sys
import webbrowser

urls = {
    "work": ["https://github.com/inkih04/Python-Automation-Projects/tree/main"],
    "personal": ["https://www.netflix.com/", "https://www.youtube.com/"]
}


def openWeb(urls):
    for url in urls: 
        print(f"oppening {url}")
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    key = ''
    if len(sys.argv) < 2:
        key = input("Chose between 'work' or 'personal':  \n").strip().lower()
        if key not in urls:
            print(f"{key} is not an available option the current options are:\nwork\npersonal")
            exit(1)
    elif len(sys.argv) == 2:
        key = sys.argv[1]
        if key not in urls:
            print(f"{key} is not an available option the current options are:\n work\npersonal")
            exit(1)
    else:
        print("Wrong usage\n Please choose 'work' or 'personal'. Example: python script.py work")
        sys.exit(1) 
    openWeb(urls[key])
