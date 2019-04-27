import wolframalpha as wa
import datetime as dt
import getpass as gp
import wikipedia as wp

user = gp.getuser()

def getMessage():
    time = dt.datetime.now().hour
    message = "Good Morning, " if (time < 12) else ("Good Afternoon, " if (time < 18) else "Good Evening, ")
    message += user.capitalize()
    return message

def wolframQuestion(input):
    answer = "\n"
    app_id = "HJ2Q67-7A35YVXQ98"
    client = wa.Client(app_id)
    result = client.query(input)
    answer += next(result.results).text
    answer += "\nsource: WolframAlpha\n"
    return answer

def wikipediaQuestion(input):
    answer = "\n"
    answer += wp.summary(input, sentences=2)
    answer += "\nsource: Wikipedia\n"
    return answer

print getMessage()

want = "yes"

while want == "yes" or want == "y":
    input = raw_input("Question: ")
    try:
        print wolframQuestion(input)
    except:
        print wikipediaQuestion(input)
    want = raw_input("Wanna ask a question? (yes/no): ")
