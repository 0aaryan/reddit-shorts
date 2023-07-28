# YouTube Shorts and Reels Automation Bot

![Logo](./media/profile/profilePic.png)

## Introduction

This project is a Python bot designed to automate the creation of YouTube Shorts and Reels from Reddit posts. It utilizes various tools and libraries, such as Google Text-to-Speech (TTS), OpenAI's Whisper, MoviePy, and more, to create engaging and entertaining short videos.

## Features

- **Reddit Post Scraping:** The bot scrapes Reddit posts and their replies to gather interesting and engaging content for creating Shorts and Reels.

- **Google Text-to-Speech (TTS):** It uses Google TTS to convert the text-based content into speech, adding a voice narration to the video.

- **OpenAI's Whisper:** The bot leverages OpenAI's Whisper for generating natural-sounding voiceovers to enhance the video's audio quality.

- **Video Editing with MoviePy:** MoviePy is utilized for video editing tasks like cutting, merging, and adding text overlays to create visually appealing content.

- **Background Music:** The bot adds background music to the videos to make them more captivating.

## Requirements

Ensure you have the following installed on your system:

- Python 3.6+
- Required Python libraries: Google Cloud Text-to-Speech, OpenAI, MoviePy, and other dependencies.

## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/youtube-shorts-bot.git
cd youtube-shorts-bot
```

2. Set up a virtual environment (optional but recommended).

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Download and set up Google Cloud credentials for the Text-to-Speech API.

5. Obtain OpenAI API credentials for the Whisper model.

## Usage

The bot can be used in two ways:

### 1. Convert Reddit Post to Video

You can use the bot to convert a single Reddit post to a video. Provide the Reddit post URL, and the bot will scrape the post and its replies to create a video.

```bash
python main.py -ru <reddit_post_url> -n <number_of_videos> -w <word_limit> -i <input_video_folder> -o <output_video_folder>
```

- `<reddit_post_url>`: URL of the Reddit post you want to convert to a video.
- `<number_of_videos>`: Number of videos to create (default is 1).
- `<word_limit>`: Word limit for the text-to-speech conversion (default is 100).
- `<input_video_folder>`: Path to the folder containing input videos for the video creation (default is "media/gameplayVids/minecraft_oneMin").
- `<output_video_folder>`: Path to the folder where the generated videos will be saved (default is "output").

### 2. Convert Multiple Reddit Posts to Videos

You can also use the bot to convert multiple Reddit posts to videos by providing a file containing a list of Reddit post URLs.

```bash
python main.py -rus <reddit_post_url_file> -n <number_of_videos> -w <word_limit> -i <input_video_folder> -o <output_video_folder>
```

- `<reddit_post_url_file>`: Path to a text file containing a list of Reddit post URLs, one URL per line.
- `<number_of_videos>`: Number of videos to create for each Reddit post (default is 1).
- `<word_limit>`: Word limit for the text-to-speech conversion (default is 100).
- `<input_video_folder>`: Path to the folder containing input videos for the video creation (default is "media/gameplayVids/minecraft_oneMin").
- `<output_video_folder>`: Path to the folder where the generated videos will be saved (default is "output").

### 3. Convert Default Reddit Post Dictionary to Videos

If you want to use a default set of Reddit post dictionaries to create videos, you can use the following command:

```bash
python main.py -d default -n <number_of_videos> -w <word_limit> -i <input_video_folder> -o <output_video_folder>
```

- `<number_of_videos>`: Number of videos to create for each Reddit post (default is 1).
- `<word_limit>`: Word limit for the text-to-speech conversion (default is 100).
- `<input_video_folder>`: Path to the folder containing input videos for the video creation (default is "media/gameplayVids/minecraft_oneMin").
- `<output_video_folder>`: Path to the folder where the generated videos will be saved (default is "output").

## Customization

Feel free to customize the bot according to your needs. You can modify the voice settings, change the video editing parameters, add new features, or integrate other AI models for different effects.

## Credits

- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech): For providing high-quality text-to-speech conversion.

- [OpenAI's Whisper](https://openai.com): For generating natural-sounding voiceovers.

- [MoviePy](https://zulko.github.io/moviepy/): For powerful video editing capabilities.

## License

This project is licensed under the [MIT License](./LICENSE).

## Disclaimer

Please use this bot responsibly and ensure you comply with YouTube's community guidelines and copyright policies. The creators of this project are not responsible for any misuse or violations that may arise from its usage. Always respect the rights and permissions of content creators whose posts are used in the creation of YouTube Shorts and Reels.

Happy creating! 🎥🚀
