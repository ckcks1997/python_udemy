import webbrowser

user_term = input("enter a search term:").replace(" ", "+")

webbrowser.open("https://google.com/search?q="+user_term)