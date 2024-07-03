import cv2
import os


image_path = os.path.join('.', 'Images', 'messi.jpg')
img = cv2.imread(image_path)


if img is None:
    print("Error: Image not loaded. Please check the file path.")
else:
    
    img_display = img.copy()

    
    def get_pixel_value(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN: 
            
            pixel_value = img[y, x]
            text = f"({x}, {y}): {pixel_value}"
            print(text)
            
            
            cv2.putText(img_display, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

            
            cv2.imshow('Image', img_display)

    
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', get_pixel_value)

    while True:
        cv2.imshow('Image', img_display)
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
