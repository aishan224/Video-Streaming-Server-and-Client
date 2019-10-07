__author__ = 'Tibbers'
class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
			print('vodeo file: |' + filename + '| read')
		except:
			print('read' + filename + 'failed')
			raise IOError
		self.frameNum = 0

	def nextFrame(self):
		"""Get next frame."""
		data = self.file.read(5) # Get the framelength from the first 5 bits
		
		if data:
			framelength = int(data)

			# Read the current frame
			data = self.file.read(framelength)
			if len(data) != framelength:
				raise ValueError('imcomplete frame data')
			self.frameNum += 1
			# print("当前帧为:", self.frameNum)
		return data

	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum

