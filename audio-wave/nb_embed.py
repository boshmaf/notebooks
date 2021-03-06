import random
from IPython.display import HTML

""" usage:
    
import nb_embed
nb_embed.html('<p>Hello World</p>')
"""

def randname(length=4):
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(0, length)])

def html(content):
    nspace = randname()
    toggle_html = '<div style="width: auto;"><a id="nb_embed_'+nspace+'" href="#nb_embed_'+nspace+'" style="display: block; background: rgb(200, 200, 200);">Show Code</a><script>$(document).ready(function(){ var toggleButton = $("#nb_embed_'+nspace+'"); var codeDiv = toggleButton.closest(".output_wrapper").prevAll(); toggleButton.on("click", function(){ codeDiv.toggle(); $("body").scrollTo("#nb_embed_'+nspace+'");  });   codeDiv.hide();   });  </script>'
    return HTML(toggle_html + '<div style="width: auto; border: 1px solid rgb(200, 200, 200); padding: 1em;">'+content+'</div></div>' )
