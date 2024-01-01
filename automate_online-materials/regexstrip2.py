import re

def regexStrip(x,y=''):


    if y!='':
        yJoin=r'['+y+']*([^'+y+'].*[^'+y+'])['+y+']*'
        cRegex=re.compile(yJoin,re.DOTALL)
        return cRegex.sub(r'\1',x)
    else:
        sRegex=re.compile(r'\s*([^\s].*[^\s])\s*',re.DOTALL)
        return sRegex.sub(r'\1',x)

text='  spmaHellow worldspam'
print(regexStrip(text,'spma'))

charLeft = re.compile(r'^([%s]+)' % 'abc')
print (charLeft.sub('',"aaabcfdsfsabcabc"))