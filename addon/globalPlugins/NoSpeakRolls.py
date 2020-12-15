# NoSpeakRolls, an add-on to stop NVDA from speaking rolls.
# Using code from Unspoken.

import globalPluginHandler
import NVDAObjects
import config
import speech
import controlTypes
import sayAllHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		# Hook to keep NVDA from announcing roles.
		self._NVDA_getSpeechTextForProperties = speech.getPropertiesSpeech
		speech.getPropertiesSpeech = self._hook_getSpeechTextForProperties

	def _hook_getSpeechTextForProperties(self, reason=NVDAObjects.controlTypes.REASON_QUERY, *args, **kwargs):
		role = kwargs.get('role', None)
		if role:
			#NVDA will not announce roles if we put it in as _role.
			kwargs['_role'] = kwargs['role']
			del kwargs['role']
		return self._NVDA_getSpeechTextForProperties(reason, *args, **kwargs)
