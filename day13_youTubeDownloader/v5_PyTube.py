from pytube import YouTube

# YouTube object with the link
myVideo = YouTube('https://www.youtube.com/watch?v=8jQekSeFW9o')

# Title of the Video
print(f"Video Title: {myVideo.title}")
# URL of the Thumbnail of the video
print(f"Thumbnail Link: {myVideo.thumbnail_url}")
# ID of the Video
print(f"Video ID: {myVideo.video_id}")
# Description of the Video
print(f"Description: {myVideo.description}")
# Length of the Video in Seconds
print(f"Duration: {myVideo.length}")
# Total Views of the Video
print(f"Views: {myVideo.views}")
# Age Restricted Content
print(f"Age Restricted: {str(myVideo.age_restricted)}")

# #  ===================================================
myVideoStreams = myVideo.streams
print(myVideoStreams)


# #  ==============================================
# # Hd Stream is best quality video
myHDStream = YouTube('https://www.youtube.com/watch?v=8jQekSeFW9o').streams.first()
myAudioStream = YouTube('https://www.youtube.com/watch?v=8jQekSeFW9o').streams.last()
print(myHDStream, myAudioStream)

# # ==================================================

# # dwownload to a relative path
myHDStream.download("Videos/")

#  =============================================
