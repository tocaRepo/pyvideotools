from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoClipExtractor:
    def __init__(self, input_video_path):
        """
        Initialize the VideoClipExtractor with the path to the input video.
        
        Parameters:
        - input_video_path: str, path to the input video file.
        """
        self.input_video_path = input_video_path

    def extract_clip(self, start_time, end_time, output_video_path):
        """
        Extracts a clip from the video.

        Parameters:
        - start_time: float, start time of the clip in seconds.
        - end_time: float, end time of the clip in seconds.
        - output_video_path: str, path to save the output clip.
        
        Returns:
        None
        """
        try:
            # Load the video
            with VideoFileClip(self.input_video_path) as video:
                # Cut the clip
                clip = video.subclip(start_time, end_time)
                # Write the result to the output file
                clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
            print(f"Clip saved successfully to {output_video_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the input video file
    input_path = "input.mp4"
    # Create an instance of the VideoClipExtractor
    extractor = VideoClipExtractor(input_path)
    # Define the start and end times for the clip (in seconds)
    start = 0  # Start time in seconds
    end = 10    # End time in seconds
    # Define the output path for the extracted clip
    output_path = "clip1.mp4"
    # Extract the clip
    extractor.extract_clip(start, end, output_path)
