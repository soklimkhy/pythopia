import re

def detect_social_platform(url):
    """Detect the social media platform from a given URL."""
    # Define patterns for different social media platforms
    patterns = {
        "YouTube Shorts": r"(?:https?://)?(?:www\.)?youtube\.com/shorts/.*",
        "Facebook Reels": r"(?:https?://)?(?:www\.)?facebook\.com/reel/.*",
        "Facebook": r"(?:https?://)?(?:www\.)?facebook\.com/.*",
        "Instagram": r"(?:https?://)?(?:www\.)?instagram\.com/.*",
        "YouTube": r"(?:https?://)?(?:www\.)?youtube\.com/.*",
        "Twitter": r"(?:https?://)?(?:www\.)?twitter\.com/.*",
        "TikTok": r"(?:https?://)?(?:www\.)?tiktok\.com/.*"
    }

    # Check the URL against each pattern
    for platform, pattern in patterns.items():
        if re.match(pattern, url):
            return platform

    return "Unknown platform"

# Example usage
if __name__ == "__main__":
    url_link = input("Enter a social media URL: ").strip()
    platform = detect_social_platform(url_link)
    print(f"The URL belongs to: {platform}")