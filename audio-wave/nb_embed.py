from IPython.display import HTML

def html(content):
    toggle_html = '''<div style="width: auto;"><a id='js_code_01' href='#' style="display: block; background: rgb(200, 200, 200);">Show Code</a>
        <script>
        $(document).ready(function(){
           var toggleButton = $('#js_code_01')
           var codeDiv = toggleButton.closest('.output_wrapper').prevAll()[1];
           toggleButton.on('click', function(){
              $(codeDiv).toggle();
           });
           $(codeDiv).hide();
        });
        </script>'''
    return HTML(toggle_html + '<div style="width: auto; border: 1px solid rgb(200, 200, 200); padding: 1em;">'+content+'</div></div>' )