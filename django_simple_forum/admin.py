from .models import Tags, Badge, UserProfile, ForumCategory, Vote, Topic, UserTopics
from .models import Comment, Timeline, Attachment, Facebook, Google, GitHub, Twitter
from django.contrib import admin


admin.site.register(Tags)
admin.site.register(Badge)
admin.site.register(UserProfile)
admin.site.register(ForumCategory)
admin.site.register(Vote)
admin.site.register(Topic)
admin.site.register(UserTopics)
admin.site.register(Comment)
admin.site.register(Timeline)
admin.site.register(Attachment)
admin.site.register(Facebook)
admin.site.register(Google)
admin.site.register(GitHub)
admin.site.register(Twitter)

