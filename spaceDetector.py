import cv2
import pickle

# Constants for the dimensions of parking spaces
PARKING_SPACE_WIDTH, PARKING_SPACE_HEIGHT = 107, 48

# Attempt to load existing parking positions from a file
try:
    with open('ParkingCoordinates', 'rb') as file:
        parking_positions = pickle.load(file)
except FileNotFoundError:
    parking_positions = []

# Function to handle mouse click events for marking parking spaces
def handle_mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left click to add a new parking space
        parking_positions.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:  # Right click to remove a parking space
        for i, (px, py) in enumerate(parking_positions):
            if px < x < px + PARKING_SPACE_WIDTH and py < y < py + PARKING_SPACE_HEIGHT:
                parking_positions.pop(i)
                break

    # Save the updated parking positions to a file
    with open('ParkingCoordinates', 'wb') as file:
        pickle.dump(parking_positions, file)

# Main loop to display the parking lot image and handle user interactions
while True:
    image = cv2.imread('ParkImg.png')
    for (x, y) in parking_positions:
        cv2.rectangle(image, (x, y), (x + PARKING_SPACE_WIDTH, y + PARKING_SPACE_HEIGHT), (255, 0, 255), 2)

    cv2.imshow("Parking Lot", image)
    cv2.setMouseCallback("Parking Lot", handle_mouse_click)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    

cv2.destroyAllWindows()
