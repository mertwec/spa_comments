import re
import pdb


text = "Sample text <div>with<div> HTML <br> <p class=''>tags</p> but <a href=”” title=””> sdsds <div>with in </div> </a> 10 <code>this</code> or <p>this <i>asdas</i> </p> "
text2 = "Sample text <p class=''>tags</p> but <a href=”” title=””>"
end_teg_pattern = re.compile(r"<(\w+)[^>]*>(.*?)<\/\1>")
any_html_pattern = re.compile(r"<(?!/?code\b)(?!/?p\b)(?!/?i\b)(?!/?a\b)(?!/?strong\b)[^>]+>")


ff = end_teg_pattern.findall(text)
fa = any_html_pattern.search(text)
fa2 = any_html_pattern.search(text2)

print(fa, "\n")

print(fa2)
pdb.set_trace()
