import re
from threading import Thread
from settings_handler import config_get
from download_handler.downloader import downloadAction

def time_formatting( t):
	t = t.split(":")
	t = [int(i) for i in t]
	t.pop(0) if t[0] == 0 else None
	def minute(m):
		if m == 1:
			return _("دقيقة واحدة")
		elif m == 2:
			return _("دقيقتان")
		elif m >=3 and m <=10:
			return _("{} دقائق").format(m)
		else:
			return _("{} دقيقة").format(m)
	def second(s):
		if s == 1:
			return _("ثانية")
		elif s == 2:
			return _("ثانيتين")
		elif s >= 3 and s <= 10:
			return _("{} ثواني").format(s)
		else:
			return _("{} ثانية").format(s)
	def hour(h):
		if h == 1:
			return _("ساعة")
		elif h == 2:
			return _("ساعتان")
		elif h >= 3 and h <=10:
			return _("{} ساعات").format(h)
		else:
			return _("{} ساعة").format(h)
	if len(t) == 1:
		return second(t[0])
	elif len(t) == 2:
		return _("{} و{}").format(minute(t[0]), second(t[1]))
	elif len(t) == 3:
		return _("{} و{} و{}").format(hour(t[0]), minute(t[1]), second(t[2]))

def youtube_regexp(string):
	pattern = re.compile("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$") # youtube links regular expression pattern
	return pattern.search(string)

def direct_download(option, url, dlg):
	path = config_get("path")
	if option == 0:
		format = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4"
	else:
		format = "bestaudio[ext=m4a]"
	convert = True if option == 2 else False
	trd = Thread(target=downloadAction, args=[url, path, dlg, format, dlg.gaugeProgress, dlg.textProgress, convert])
	trd.start()
