"""
batch_fetch_transcripts.py

Usage:
    python batch_fetch_transcripts.py videos.json

videos.json format:
{
  "brennan-dunn": ["https://youtube.com/watch?v=xxxx", "https://youtube.com/watch?v=yyyy"],
  "val-geisler": ["https://youtube.com/watch?v=zzzz"]
}

Fetches the video title automatically (via YouTube's public oEmbed endpoint,
no API key required), then saves each transcript as a markdown file in
research/youtube-transcripts/. Skips videos that fail (no captions, bad URL,
etc.) and prints a summary at the end instead of stopping the whole batch.
"""

import sys
import re
import os
import json
import urllib.request
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

def get_title(url):
    """Fetch video title via YouTube's public oEmbed endpoint (no API key needed)."""
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
        with urllib.request.urlopen(oembed_url, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get("title", "untitled")
    except Exception:
        return "untitled"

def fetch_one(url, expert_slug, api):
    video_id = get_video_id(url)
    title = get_title(url)

    transcript_list = api.fetch(video_id)
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

    return filepath

def main():
    if len(sys.argv) < 2:
        print("Usage: python batch_fetch_transcripts.py videos.json")
        sys.exit(1)

    json_path = sys.argv[1]

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("Missing dependency. Run: pip install youtube-transcript-api")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    api = YouTubeTranscriptApi()

    succeeded = []
    failed = []

    for expert_slug, urls in data.items():
        for url in urls:
            try:
                filepath = fetch_one(url, expert_slug, api)
                print(f"[OK] {expert_slug}: {filepath}")
                succeeded.append((expert_slug, url))
            except Exception as e:
                print(f"[FAIL] {expert_slug}: {url} -> {e}")
                failed.append((expert_slug, url, str(e)))

    print("\n--- Summary ---")
    print(f"Succeeded: {len(succeeded)}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("\nFailed videos (likely no captions available or bad URL):")
        for expert_slug, url, err in failed:
            print(f"  - {expert_slug}: {url} ({err})")

if __name__ == "__main__":
    main()
