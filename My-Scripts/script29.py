#!/usr/bin/env python -tt

'''
  Regular expressions : 
  Greedy vs Non-greedy

  Suppose you have text with tags in it: <b>foo</b> and <i>so on</i>

1)Suppose you are trying to match each tag with the pattern '(<.*>)' -- what does it match first?
  The result is a little surprising, but the greedy aspect of the .* causes it to match the whole 
  '<b>foo</b> and <i>so on</i>' as one big match. 
  The problem is that the .* goes as far as is it can, instead of stopping at the first > (aka it is "greedy").

2)There is an extension to regular expression where you add a ? at the end, such as .*? or .+?, changing them 
  to be non-greedy. Now they stop as soon as they can. So the pattern '(<.*?>)' will get just '<b>' as the 
  first match, and '</b>' as the second match, and so on getting each <..> pair in turn. 
  The style is typically that you use a .*?, and then immediately its right look for some concrete marker (> in this case) 
  that forces the end of the .*? run.

3)An older but widely used technique to code this idea of "all of these chars except stopping at X" uses the 
  square-bracket style. For the above you could write the pattern, but instead of .* to get all the chars, 
  use [^>]* which skips over all characters which are not > (the leading ^ "inverts" the square bracket set, 
  so it matches any char not in the brackets).
'''

# Import
import re

def main():
  tag = '<b>foo</b> and <i>so on</i>'
  tags = re.findall(r'<.*?>', tag)
  tags1 = re.findall(r'<[^>]*>', tag) 
  if tags and tags1:
    print tags
    print tags1
  else:
    print 'Not found'

  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  match = re.findall(r'([\w.-]+)@([\w-]+.com)', str)
  if match:
    print 'Found ID:', match
  else:
    print 'Not found'

  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
  ## \1 is group(1), \2 group(2) in the replacement
  str1 = re.sub(r'([\w.-]+)@([\w-]+.com)', r'\1@yo-yo-dyne.com', str)
  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher  
  match1 = re.findall(r'([\w.-]+)@([\w-]+.com)', str1)
  if match1:
    print 'Found ID:', match1
  else:
    print 'Not found'

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()