import unittest

from project.social_media import SocialMedia


class TestSocialMediaMethods(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia(username="user1", platform="Instagram", followers=10000, content_type="image")

    def test_init(self):
        # Test case 1: Valid initialization
        self.assertEqual(self.social_media._username, "user1")
        self.assertEqual(self.social_media.platform, "Instagram")
        self.assertEqual(self.social_media.followers, 10000)
        self.assertEqual(self.social_media._content_type, "image")
        self.assertEqual(self.social_media._posts, [])

        # Test case 2: Invalid platform
        with self.assertRaises(ValueError):
            self.social_media.platform = "InvalidPlatform"

        # Test case 3: Negative followers
        with self.assertRaises(ValueError):
            self.social_media.followers = -10000

    def test_create_post(self):
        # Test case 1: Valid post creation
        self.assertEqual(self.social_media.create_post("This is a test post."), "New image post created by user1 on Instagram.")

        # Test case 2: Valid post creation with different content type
        video_social_media = SocialMedia(username="user2", platform="YouTube", followers=5000, content_type="video")
        self.assertEqual(video_social_media.create_post("This is a test video."), "New video post created by user2 on YouTube.")

    def test_like_post_happy_path(self):
        # Test case 1: Like post within the limit
        self.social_media.create_post("This is another test post.")
        self.assertEqual(self.social_media.like_post(0), "Post liked by user1.")
        self.assertEqual(self.social_media._posts[0]['likes'], 1)

    def test_like_post_bad_path(self):
        # Test case 1: Invalid post index
        self.assertEqual(self.social_media.like_post(0), "Invalid post index.")

        # Test case 2: Post index out of range
        self.assertEqual(self.social_media.like_post(1), "Invalid post index.")

        # Test case 3: Maximum likes reached
        self.social_media.create_post("Post with maximum likes.")


if __name__ == '__main__':
    unittest.main()
