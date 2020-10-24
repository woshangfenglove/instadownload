from django.shortcuts import render
import instaloader


L = instaloader.Instaloader()

class Download:

	def __init__(self):
		self.value = 1

	def get_post(self,url):
		# https://www.instagram.com/p/CGrbgvcszfV/?utm_source=ig_web_copy_link
		if "https://www.instagram.com/" in url:
			url = url.split('/')[-2]
		else:
			res = {
				'isset': False,
				'error':'Invalid url!'
			}
			return res
		post = instaloader.Post.from_shortcode(L.context, url)
		res = {
			'isset': True,
			'url': post.url,
			'video_url': post.video_url,
			'shortcode': post.shortcode,
			'mediaid': post.mediaid,
			'date_local': post.date_local,
			'profile': post.profile,
			'typename': post.typename,
			'sidecar_node': post.get_sidecar_nodes(),
			'is_video': post.is_video,

		}
		return res

def main(request):
	context = {}
	if request.method == 'POST':
		url = request.POST['url']
		download = Download()
		post = download.get_post(url)
		context["post"] = post

	return render(request, "instadownload/index.html", context)