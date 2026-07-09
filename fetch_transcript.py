"""
fetch_transcript.py

Usage:
    python fetch_transcript.py <youtube_url> <expert-name-slug> "<Video Title>"

Example:
    python fetch_transcript.py https://www.youtube.com/watch?v=abc123 brennan-dunn "Email Automation for SaaS"

Saves the transcript as a markdown file in research/youtube-transcripts/
"""

import sys
import re
import os
from datetime import date

def get_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})", url)
    if not match:
        raise ValueError("Could not extract video ID from URL: " + url)
    return match.group(1)

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def main():
    if len(sys.argv) < 4:
        print('Usage: python fetch_transcript.py <youtube_url> <expert-name-slug> "<Video Title>"')
        sys.exit(1)

    url = sys.argv[1]
    expert_slug = sys.argv[2]
    title = sys.argv[3]

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("Missing dependency. Run: pip install youtube-transcript-api")
        sys.exit(1)

    video_id = get_video_id(url)

    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
    except Exception as e:
        print(f"Failed to fetch transcript for {url}: {e}")
        sys.exit(1)

    lines = [seg.text for seg in transcript_list]
    full_text = " ".join(lines)

    out_dir = os.path.join("research", "youtube-transcripts")
    os.makedirs(out_dir, exist_ok=True)

    filename = f"{expert_slug}-{slugify(title)}.md"
    filepath = os.path.join(out_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Expert:** {expert_slug}\n\n")
        f.write(f"**URL:** {url}\n\n")
        f.write(f"**Collected:** {date.today().isoformat()}\n\n")
        f.write("## Transcript\n\n")
        f.write(full_text)
        f.write("\n")

    print(f"Saved: {filepath}")

if __name__ == "__main__":
    main()
