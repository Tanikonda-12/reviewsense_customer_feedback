import pandas as pd
from collections import Counter #counter(["good","bad","good"])------>{"good:2,"bad":1}
import re

# Keyword cleaning function
def extract_keywords(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", "", text)   # corrected regex
    words = text.split()
    return words

# Main execution
if __name__ == "__main__":
    # Input from Milestone 2
    df = pd.read_csv("Milestone2_sentiment_Results_new.csv")

    # Extract keywords from clean_feedback column
    all_words = []
    df["clean_feedback"].apply(lambda x: all_words.extend(extract_keywords(x)))

    # Count keyword frequency
    keyword_freq = Counter(all_words)

    # Convert to DataFrame
    keywords_df = pd.DataFrame(keyword_freq.items(), 
                               columns=["keyword", "frequency"]) \
                               .sort_values(by="frequency", ascending=False)

    # Save results
    keywords_df.to_csv("Milestone3_keyword_Insights.csv", index=False)

    print("Milestone 3 completed successfully!")
    print(keywords_df.head(10))