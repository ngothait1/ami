def createRedirectScript():
    return '''
    <script>
        function redirect() {
          let url = document.getElementById('urlInput').value.toLowerCase();
          if (url) {
            window.location.href = '/login/' + url;
          }
        }
    </script>
    '''



