import cv2
import mediapipe as mp
import time

def run_face_mesh():
    cap = cv2.VideoCapture(0)
    pTime = 0

    mpDraw = mp.solutions.drawing_utils
    mpFaceMesh = mp.solutions.face_mesh
    faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
    drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                mpDraw.draw_landmarks(img, faceLms,
                                      mpFaceMesh.FACEMESH_TESSELATION,
                                      drawSpec, drawSpec)
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    cx, cy = int(lm.x * iw), int(lm.y * ih)
                    print(id, cx, cy)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.imshow("Face Mesh", img)
        if cv2.waitKey(1) & 0xFF == 27:  # press ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()

# usage
# from facemesh_module import run_face_mesh
# run_face_mesh()

if __name__ == '__main__':
    run_face_mesh()