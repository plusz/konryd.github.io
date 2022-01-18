from random import shuffle

def get_random_set():
  all_options = [[a, b] for a in range(2, 6) for b in range(2, 10)]
  shuffle([shuffle(pair) for pair in all_options])
  all_lines = ["%s * &nbsp;&nbsp;&nbsp; = %s<br/>" % (a, a * b) for (a, b) in all_options]
  return "\n".join(all_lines[:10])


template = """
<html>
<head>
<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');


table.outer {
  font-family: 'Roboto Mono', monospace;
  border-collapse: collapse;
}

table.outer td {
    border:1px solid #000000;
}

table.inner td {
  border: none;
  font-size: 25px;
  line-height: 1.5;
  padding: 5px;
}

img {
  margin-left: 10px;
}

</style>
</head>
<body>
<table class="outer">
<tr>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img width="120" src="podium2.png"/></td> 
  </tr></table>
</td>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img width="120" src="podium2.png"/></td> 
  </tr></table>
</td>
</tr>
<tr>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img width="120" src="podium2.png"/></td> 
  </tr></table>
</td>
<td>
 <table class="inner"><tr>
    <td>%s</td>
    <td><img width="120" src="podium2.png"/></td> 
  </tr></table>
</td>
</tr>
</table>
</body>
</html>
"""

print(template % (
  get_random_set(),
  get_random_set(),
  get_random_set(),
  get_random_set()))
