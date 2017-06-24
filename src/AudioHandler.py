from cocos.audio.pygame.mixer import Sound


class Audio(Sound):
	def __init__(self,audio_file):
		super(Audio,self).__init__(audio_file)