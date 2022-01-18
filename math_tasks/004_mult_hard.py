from random import shuffle
from render import render_template

def mult_2_5_9():
  all_options = [(a, b) for a in (3, 4, 5, 6, 7, 8, 9) for b in (4, 5, 6, 7, 8)]
  all_options = list(set(all_options + [(b, a) for (a, b) in all_options]))
  shuffle(all_options)
  shuffled_order_no_repeats = []
  seen = set()
  for pair in all_options:
    canonical_pair = tuple(sorted(pair))
    if canonical_pair not in seen:
      shuffled_order_no_repeats.append(pair)
      seen.add(canonical_pair)
  
  return ["%s &Cross; %s =   <br/>" % (a, b) for (a, b) in shuffled_order_no_repeats][:10]

if __name__ == "__main__":
  render_template(mult_2_5_9)
