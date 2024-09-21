import unittest
from EmotionDetection.emotion_detection import emotion_detector as emotion

class TestEmotion(unittest.TestCase):
    def test1(self):
        self.assertEqual(emotion("I am glad this happened"),"joy")
        self.assertEqual(emotion("I am really mad about this"),"anger")
        self.assertEqual(emotion("I feel disgusted just hearing about this"),"disgust")
        self.assertEqual(emotion("I am so sad about this"),"sadness")
        self.assertEqual(emotion("I am really afraid that this will happen"),"fear")
unittest.main()
