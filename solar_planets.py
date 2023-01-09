import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,200),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (20,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Venus",
            (60,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Earth",
            (100,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mars",
            (140,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Jupiter",
            (180,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Saturn",
            (220,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Uranus",
            (260,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Neptune",
            (300,100),
            cv2.FONT_HERSHY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.imshow("Display image",img)
cv2.waitKey(0)

