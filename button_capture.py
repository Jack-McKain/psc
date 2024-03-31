from picamera2 import Picamera2, Preview
import time

def take_photo_and_show():
    picam2 = Picamera2()
    config = picam2.create_preview_configuration()
    config['controls']['AfTrigger'] = 1
    picam2.configure(config)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    
    print("Press Enter to take a photo...")
    input()  # Wait for Enter key to be pressed
    
    # Stop the preview to take a photo
    #picam2.stop_preview()
    picam2.capture_file("button_test.jpg")

    # Take a photo and save it
    #file_path = "/home/pi/Desktop/photo.jpg"  # Change this path as needed
    #picam2.capture_file(file_path)
    #print(f"Photo saved to {file_path}")

    # Start the preview again to show the photo taken
    # Since Picamera2 does not directly support showing an image file in the preview,
    # we recommend viewing the saved photo using another method after the script completes.
    # For instance, you can use an image viewer command in the terminal, such as:
    # eog /home/pi/Desktop/photo.jpg (for GNOME) or display /home/pi/Desktop/photo.jpg (ImageMagick)

if __name__ == "__main__":
    take_photo_and_show()
