"""
Youtube and Vimeo Tags
---------
This implements a Liquid-style youtube tag for Pelican,
based on the jekyll / octopress youtube tag [1]_

"""
import re
from .mdx_liquid_tags import LiquidTags

FAIL = '\033[91m'
ENDC = '\033[0m'

TEMPLATE = "<iframe width='{width}' height='{height}' src='{service}/{video_id}' " \
           "frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>"

TEMPLATE_RESPONSIVE = "<div style='position: relative;padding-bottom: 56.25%;padding-top: 25px;height: 0;'>" \
                      "<iframe style='position: absolute; top: 0;left: 0;width: 100%;height: 100%' " \
                      "src='{service}/{video_id}' frameborder='0' " \
                      "webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>" \
                      "</div>"

SERVICES = {"vimeo": "//player.vimeo.com/video", "youtube": "//www.youtube.com/embed"}


@LiquidTags.register('youtube')
@LiquidTags.register('vimeo')
def youtube(preprocessor, tag, markup):
    video_parts = filter(None, re.split('\W+', markup))
    if video_parts:
        if len(video_parts) == 2 and re.match('', video_parts[1]):
            width, height = video_parts[1].split("x")
            return TEMPLATE.format(service=SERVICES.get(tag), video_id=video_parts[0], width=width, height=height)
        else:
            return TEMPLATE_RESPONSIVE.format(service=SERVICES.get(tag), video_id=video_parts[0])
    else:
        raise ValueError(FAIL + "Error processing video tag, expected syntax: \n"
                                "* for YouTube: {% youtube id %} or {% youtube id widthxheight %}, "
                                "e.g. {% youtube _2GKyorhHtc 640x360 %} \n"
                                "* for Vimeo: {% vimeo id %} or {% vimeo id widthxheight %}, "
                                "e.g. {%vimeo 46812816 %}" + ENDC)

#----------------------------------------------------------------------
# This import allows image tag to be a Pelican plugin
from liquid_tags import register
