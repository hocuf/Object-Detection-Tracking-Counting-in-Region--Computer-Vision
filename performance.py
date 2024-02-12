import time

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()  # Record the start time of the total process
        self.total_frames = 0  # Total number of processed frames
        self.total_process_time = 0  # Total processing time

    def start_frame(self):
        """Records the start time of processing for each frame."""
        self.frame_start_time = time.time()

    def end_frame(self):
        """Marks the end of processing for each frame and updates the total time."""
        self.total_frames += 1
        frame_process_time = time.time() - self.frame_start_time
        self.total_process_time += frame_process_time

    def summarize(self):
        """Calculates and prints the performance summary."""
        total_time_elapsed = time.time() - self.start_time
        if self.total_frames > 0:
            average_frame_time = self.total_process_time / self.total_frames
            fps = self.total_frames / total_time_elapsed
            print(f"Total Time Elapsed: {total_time_elapsed:.3f} seconds")
            print(f"Total Frames Processed: {self.total_frames}")
            print(f"Average Frame Process Time: {average_frame_time:.3f} seconds")
            print(f"FPS: {fps:.2f}")
        else:
            print("No frames processed.")

# Run the following test code when this file is executed directly.
if __name__ == "__main__":
    # Example usage
    performance_monitor = PerformanceMonitor()

    # Your video processing loop starts here
    # For example, loop over a video file or live camera feed
    # For each frame:
    #   performance_monitor.start_frame()
    #   # frame processing codes
    #   performance_monitor.end_frame()

    # After the loop ends
    performance_monitor.summarize()
