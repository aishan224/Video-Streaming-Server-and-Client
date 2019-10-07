__author__ = 'Tibbers'
import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:
	header = bytearray(HEADER_SIZE)

	def __init__(self):
		pass

	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload): # pyload:有效荷载 pt：有效荷载类型
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())  #时间戳就是记录当前时间的？？
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields

		# header[0] = ...
		# ...
		# 将对应的第一个字节放上V,P,X,CC(见文档的header)
		self.header[0] = version << 6
		self.header[0] = self.header[0] | padding << 5
		self.header[0] = self.header[0] | extension << 4 
		self.header[0] = self.header[0] | cc

		self.header[1] = marker << 7
		self.header[1] = self.header[1] | pt 

		self.header[2] = seqnum >> 8 
		self.header[3] = seqnum & 0xFF

		self.header[4] = (timestamp >> 24) & 0xFF
		self.header[5] = (timestamp >> 16) & 0xFF
		self.header[6] = (timestamp >> 8) & 0xFF
		self.header[7] = timestamp & 0xFF

		self.header[8] = ssrc >> 24
		self.header[9] = ssrc >> 16333
		self.header[10] = ssrc >> 8
		self.header[11] = ssrc

		# Get the payload from the argument
		# self.payload = ...
		self.payload = payload

	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])  # the prior part of vstream
		self.payload = byteStream[HEADER_SIZE:]

	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)

	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)

	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)

	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)

	def getPayload(self):
		"""Return payload."""
		return self.payload

	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload