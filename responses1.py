from datetime import datetime
def sample_responses(input_text):
    user_msg=str(input_text).lower()
    if user_msg in ('hii','hello','hi','hey','sup','hlw'):
        return "Hey!! How's it going?"
    if user_msg in ('who are you',"what's your name"):
        return "I am Ritul Bot"
    if user_msg in ("what's the time now?",'time','time now'):
        date_time=(datetime.now()).strftime("%d/%m/%y,%H:%M:%S")
        return date_time
    if user_msg in ('bye','bubye'):
        return "Bye! It was nice talking to you.."
    if user_msg in ('what are you doing'):
        return "Chatting with you!"
    else:
        return "I don't understand you!"


