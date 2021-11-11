from instapy import InstaPy

session = InstaPy(username='swtube', password= 'khuswtube20200324')
session.login()

session.set_relationship_bounds(enabled=True,
				 #potency_ratio=1.34,
				  delimit_by_numbers=True,
				   max_followers=1000,
				    max_following=4490,
				     min_followers=30,
				      min_following=20)

session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True)

session.set_do_follow(True, percentage=100, times=2)

# session.like_by_tags(['#채식주의','맞팔','선팔','좋아요', '#비건', '#비건푸드', '#비건레시피', '#자선단체','#선팔하면맞팔'], amount=50)
session.like_by_tags(['#공스타','#컴공','#소프트웨어','#경희대학교',
					  '#이과','#고3스타그램','#고3', '#소융'], amount=50)
# session.set_comments(["Good!, I love this!", 
#     "Nice!!", "Excellent :)", "Perfect :)", "멋저요!!", "Amazing!!", 
#     "Beautiful :)", "Wonderful!!", "Good job", "pretty good.", "It looks great!", 
#     "You must be a man of ability.", "I like this.", "Good.", "Sweet!", 
#     "Beautiful :heart_eyes:"
#     ])
# session.set_do_comment(True, percentage=40)

session.set_dont_like(['selfi','naked','nsfw'])

session.end()