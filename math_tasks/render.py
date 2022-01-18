template = """
<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&display=swap" rel="stylesheet">

<style>

table.outer {
  font-family: 'Roboto Mono', monospace;
  border-collapse: collapse;
}

table.outer td {
    border:1px solid #000000;
}

table.inner td {
  border: none;
  font-size: 23px;
  line-height: 1.5;
  padding: 8px;

}

img {
  margin-left: 50px;
}

</style>
</head>
<body>
<table class="outer">
<tr>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img height="350" src="tygrys.png"/></td> 
  </tr></table>
</td>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img height="350" src="tygrys.png"/></td> 
  </tr></table>
</td>
</tr>
<tr>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img height="350" src="tygrys.png"/></td> 
  </tr></table>
</td>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img height="350" src="tygrys.png"/></td> 
  </tr></table>
</td>
</tr>
</table>
</body>
</html>
"""

def render_template(lines_generator):
  print template % (
    "\n".join(lines_generator()),
    "\n".join(lines_generator()),
    "\n".join(lines_generator()),
    "\n".join(lines_generator()))
