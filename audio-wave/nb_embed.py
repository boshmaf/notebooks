import random
from IPython.display import HTML

def randname(length=4):
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(0, length)])

def html(content):
    nspace = randname()
    toggle_html = '<div style="width: auto;"><a id="js_code_'+nspace+'" href="#" style="display: block; background: rgb(200, 200, 200);">Show Code</a><script>$(document).ready(function(){ var toggleButton = $("#js_code_'+nspace+'"); var codeDiv = toggleButton.closest(".output_wrapper").prevAll(); toggleButton.on("click", function(){ codeDiv.toggle();  });   codeDiv.hide();   });  </script>'
    return HTML(toggle_html + '<div style="width: auto; border: 1px solid rgb(200, 200, 200); padding: 1em;">'+content+'</div></div>' )