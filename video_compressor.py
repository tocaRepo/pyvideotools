from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoCompressor:
    def __init__(self, input_video_path):
        """
        Initialize the VideoCompressor with the path to the input video.
        
        Parameters:
        - input_video_path: str, path to the input video file.
        """
        self.input_video_path = input_video_path

    def compress_video(self, output_video_path, target_bitrate='1000k'):
        """
        Compress the video by adjusting the bitrate, keeping the same resolution.

        Parameters:
        - output_video_path: str, path to save the compressed video.
        - target_bitrate: str, target bitrate for the video (e.g., '1000k' for 1000 kbps).
        
        Returns:
        None
        """
        try:
            with VideoFileClip(self.input_video_path) as video:
                # Write the compressed video to the output file with a target bitrate
                video.write_videofile(output_video_path, codec='libx264', audio_codec='aac', bitrate=target_bitrate)
                
            print(f"Compressed video saved successfully to {output_video_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the input video file
    input_path = "input.mp4"
    # Path to save the compressed video
    output_path = "compressed_video.mp4"
    # Create an instance of the VideoCompressor
    compressor = VideoCompressor(input_path)
    # Compress the video with the same resolution and a target bitrate
    compressor.compress_video(output_path, target_bitrate='500k')  # Example bitrate
