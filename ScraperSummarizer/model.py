import os
from summarizer import Summarizer

def summarize(text: str) -> str:
    os.system("cls")
    print("="*30)
    print("Processing summrize...".center(30))
    print("="*30)

    model = Summarizer()
    summary_text = model(text, ratio=0.2, min_length=15, max_length=80)

    os.system("cls")
    print("="*20)
    print("Summrize end!".center(20))
    print("="*20)

    return summary_text