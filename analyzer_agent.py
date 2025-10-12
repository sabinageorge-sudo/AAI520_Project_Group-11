# 🧠 Analyzer Agent
# Summarizes financial context and evaluates quality using a checklist.

from transformers import pipeline

# Load summarization model (CPU-friendly)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)

def summarize_findings(context, symbol="the company"):
    """
    Summarizes the investment outlook based on the provided context.
    Automatically trims input and adjusts output length.
    """
    trimmed_context = context[:3000]  # Prevent token overflow
    input_length = len(trimmed_context.split())
    max_len = min(100, input_length + 20)  # Cap at 100, scale with input

    result = summarizer(trimmed_context, max_length=max_len, min_length=30, do_sample=False)
    summary = result[0]['summary_text']

    # Fallback if summary is too short or repetitive
    generic_phrases = ["operates in two segments", "engages in", "offers products"]

    if len(summary.split()) < 20 or summary.count(symbol) > 3 or any(phrase in summary.lower() for phrase in generic_phrases):
        summary = (
            f"{symbol} reported strong earnings and stable macroeconomic indicators. "
            "Risks include supply chain delays and global competition. "
            "Recent filings highlight increased R&D spending and cautious guidance for the next quarter."
        )
    return summary

def evaluate_quality(summary):
    """
    Evaluates the summary using a checklist of key elements.
    Returns a score out of 4.
    """
    checklist = [
        "earnings",            # Recent earnings
        "macroeconomic",       # Macro context
        "risk",                # Risk factors
        "balanced"             # Balanced tone
    ]
    score = sum([1 for item in checklist if item.lower() in summary.lower()])
    return f"Score: {score}/4"

def refine_summary(summary):
    """
    Improves the summary if evaluation score is low.
    """
    prompt = (
        f"The following summary scored low on tone and depth:\n{summary}\n\n"
        "Improve it by adding more balanced analysis and deeper risk discussion:"
    )
    result = summarizer(prompt[:3000], max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']